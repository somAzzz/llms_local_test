#!/usr/bin/env python3
"""
LLM Performance Benchmark Script
Multi-model testing with automatic report generation
Reads configuration from benchmark_config.yaml
"""

import argparse
import os
import sys
import time
from datetime import datetime
from typing import Dict, List

import requests

try:
    import yaml
except ImportError:
    yaml = None

# Configuration file path
CONFIG_FILE = os.path.join(os.path.dirname(__file__), "benchmark_config.yaml")


def load_config() -> Dict:
    """Load configuration from YAML file"""
    if yaml is None:
        print("Warning: pyyaml not installed, using defaults")
        return {}

    if not os.path.exists(CONFIG_FILE):
        print(f"Warning: Config file not found: {CONFIG_FILE}")
        return {}

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config or {}
    except Exception as e:
        print(f"Warning: Failed to load config: {e}")
        return {}


def get_api_url(config: Dict) -> str:
    """Get API URL from config"""
    return config.get("api", {}).get("url", "http://localhost:8000/v1/chat/completions")


def get_api_timeout(config: Dict) -> int:
    """Get API timeout from config"""
    return config.get("api", {}).get("timeout", 300)


def get_default_model(config: Dict) -> str:
    """Get default model from config"""
    return config.get("model", {}).get("default", "Qwen/Qwen3-Coder-Next-FP8")


def get_test_cases(config: Dict, suite: str = "standard") -> List[Dict]:
    """Get test cases from config based on suite type"""
    test_config = config.get(f"{suite}_test_cases", [])
    if not test_config:
        print(f"Warning: {suite} test cases not found in config")
        return []
    return test_config


def get_model_config(config: Dict, model_name: str) -> Dict:
    """Get model-specific configuration"""
    models = config.get("models", {})
    return models.get(
        model_name,
        {
            "enabled": True,
            "test_suite": "standard",
            "prefer_lightweight": False,
            "is_reasoning_model": False,
        },
    )


def get_available_models(api_url: str) -> List[str]:
    """Get list of available models"""
    try:
        base_url = api_url.replace("/v1/chat/completions", "")
        resp = requests.get(f"{base_url}/v1/models", timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return [m["id"] for m in data.get("data", [])]
    except Exception:
        pass
    return []


def check_api_status(api_url: str, model_name: str) -> bool:
    """Check if API is available"""
    try:
        base_url = api_url.replace("/v1/chat/completions", "")
        resp = requests.get(f"{base_url}/v1/models", timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            models = [m["id"] for m in data.get("data", [])]
            if model_name in models:
                return True
            elif models:
                print(f"  Available models: {models}")
    except Exception as e:
        print(f"  API connection failed: {e}")
    return False


def run_test(
    api_url: str,
    model_name: str,
    timeout: int,
    prompt: str,
    max_tokens: int,
    name: str,
    is_reasoning_model: bool = False,
) -> Dict:
    """Run a single test"""
    data = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.7,
    }

    start = time.time()
    try:
        resp = requests.post(api_url, json=data, timeout=timeout)
        elapsed = time.time() - start
        result = resp.json()

        if resp.status_code != 200:
            return {
                "name": name,
                "success": False,
                "error": result.get("error", {}).get("message", "Unknown error"),
            }

        usage = result.get("usage", {})
        prompt_tokens = usage.get("prompt_tokens", 0)
        completion_tokens = usage.get("completion_tokens", 0)
        total_tokens = usage.get("total_tokens", 0)

        ttft_estimate = elapsed * 0.1
        generation_speed = completion_tokens / elapsed if elapsed > 0 else 0

        # GLM series may use reasoning field
        content = result.get("choices", [{}])[0].get("message", {}).get("content")
        if is_reasoning_model:
            reasoning_content = (
                result.get("choices", [{}])[0].get("message", {}).get("reasoning")
            )
            if not content and reasoning_content:
                content = reasoning_content

        response_preview = (content or "")[:300]

        return {
            "name": name,
            "success": True,
            "elapsed": elapsed,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "generation_speed": generation_speed,
            "ttft_estimate": ttft_estimate,
            "response_preview": response_preview,
        }
    except Exception as e:
        return {"name": name, "success": False, "error": str(e)}


def generate_markdown_report(
    model_name: str,
    results: List[Dict],
    gpu_info: Dict = None,
    api_url: str = "",
    config: Dict = None,
) -> str:
    """Generate Markdown report"""
    successful = [r for r in results if r.get("success")]
    failed = [r for r in results if not r.get("success")]

    avg_speed = (
        sum(r["generation_speed"] for r in successful) / len(successful)
        if successful
        else 0
    )
    total_time = sum(r.get("elapsed", 0) for r in results)
    total_tokens = sum(r.get("completion_tokens", 0) for r in successful)

    peak_memory = "N/A"
    try:
        import subprocess

        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=memory.used",
                "--format=csv,noheader,nounits",
                "-d",
                "MONITOR",
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            memory_used = [
                int(x) for x in result.stdout.strip().split("\n") if x.strip()
            ]
            if memory_used:
                peak_memory = f"{max(memory_used)} MB"
    except Exception:
        pass

    test_mode = "Complex Comprehensive" if len(results) > 8 else "Standard"

    report = f"""# {model_name} Performance Benchmark Report

## Test Information

- **Test Time**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **Model**: {model_name}
- **API URL**: {api_url}
- **Test Cases**: {len(results)}
- **Test Mode**: {test_mode}

"""

    if gpu_info:
        report += f"""## GPU Information

- **Model**: {gpu_info.get("name", "Unknown")}
- **Memory**: {gpu_info.get("memory", "Unknown")}
- **Driver**: {gpu_info.get("driver", "Unknown")}
- **Peak Memory (est.)**: {peak_memory}

"""

    report += f"""## Test Results Summary

| Metric | Value |
|--------|-------|
| Successful Tests | {len(successful)}/{len(results)} |
| **Avg Generation Speed** | **{avg_speed:.1f} tok/s** |
| Total Time | {total_time:.2f}s |
| Total Tokens | {total_tokens} |

### Speed Statistics

- **Max**: {max((r["generation_speed"] for r in successful), default=0):.1f} tok/s
- **Min**: {min((r["generation_speed"] for r in successful), default=0):.1f} tok/s
- **Median**: {sorted([r["generation_speed"] for r in successful])[len(successful) // 2] if successful else 0:.1f} tok/s

"""

    if avg_speed > 50:
        performance = "Excellent"
    elif avg_speed > 30:
        performance = "Good"
    elif avg_speed > 15:
        performance = "Average"
    else:
        performance = "Slow"

    report += """## Detailed Results

| Test Case | Time | Prompt | Completion | Speed |
|-----------|------|--------|------------|-------|
"""
    for r in results:
        if r.get("success"):
            report += f"| {r['name']} | {r['elapsed']:.2f}s | {r['prompt_tokens']} | {r['completion_tokens']} | **{r['generation_speed']:.1f}** tok/s |\n"
        else:
            report += f"| {r['name']} | FAILED | - | - | - |\n"

    report += "\n## Test Details\n\n"

    for r in successful:
        report += f"""### {r["name"]}

- **Time**: {r["elapsed"]:.2f}s
- **Speed**: {r["generation_speed"]:.1f} tok/s
- **TTFT (est.)**: {r["ttft_estimate"]:.3f}s

**Response Preview:**
```
{r["response_preview"]}...
```

---

"""

    if failed:
        report += "## Failed Tests\n\n"
        for r in failed:
            report += f"- **{r['name']}**: {r.get('error', 'Unknown error')}\n"

    report += f"""
## Conclusion

**Performance Rating**: {performance}

- Average Speed: {avg_speed:.1f} tok/s

---
*Generated by benchmark script*
"""

    return report


def get_gpu_info() -> Dict:
    """Get GPU information"""
    try:
        import subprocess

        result = subprocess.run(
            [
                "nvidia-smi",
                "--query-gpu=name,memory.total,driver_version",
                "--format=csv,noheader,nounits",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            lines = result.stdout.strip().split("\n")
            if lines:
                parts = lines[0].split(", ")
                return {
                    "name": parts[0].strip(),
                    "memory": f"{parts[1].strip()} MB",
                    "driver": parts[2].strip() if len(parts) > 2 else "Unknown",
                }
    except Exception:
        pass
    return {}


def main():
    parser = argparse.ArgumentParser(description="LLM Performance Benchmark Script")
    parser.add_argument("--api-url", "-u", default=None, help="API URL")
    parser.add_argument("--model", "-m", default=None, help="Model name to test")
    parser.add_argument("--report", "-r", default=None, help="Report output filename")
    parser.add_argument(
        "--complex", "-x", action="store_true", help="Use complex test suite"
    )
    parser.add_argument(
        "--cases", "-c", type=int, default=None, help="Number of test cases"
    )
    parser.add_argument(
        "--config",
        default=CONFIG_FILE,
        help=f"Config file path (default: {CONFIG_FILE})",
    )
    args = parser.parse_args()

    config = load_config()

    api_url = args.api_url or get_api_url(config)
    timeout = get_api_timeout(config)
    default_model = args.model or get_default_model(config)

    # Create reports directory if it doesn't exist
    reports_dir = os.path.join(os.path.dirname(__file__), "..", "reports")
    os.makedirs(reports_dir, exist_ok=True)

    report_file = args.report or os.path.join(
        reports_dir, f"benchmark_{default_model.replace('/', '_')}.md"
    )

    if not args.model:
        available = get_available_models(api_url)
        if available:
            auto_priority = config.get("model", {}).get(
                "auto_detect_priority", ["glm", "qwen"]
            )
            for prefix in auto_priority:
                for m in available:
                    if prefix in m.lower():
                        args.model = m
                        break
                if args.model:
                    break
            if not args.model:
                args.model = available[0]
        else:
            args.model = default_model

    model_cfg = get_model_config(config, args.model)
    is_reasoning_model = model_cfg.get("is_reasoning_model", False)

    if args.complex:
        test_suite = "complex"
        test_cases = get_test_cases(config, "complex")
        test_cases = test_cases[
            : args.cases or config.get("test", {}).get("complex_cases_max", 10)
        ]
        print(f"  Test mode: Complex ({len(test_cases)} comprehensive tests)")
    elif model_cfg.get("prefer_lightweight", False):
        test_suite = "lightweight"
        test_cases = get_test_cases(config, "lightweight")
        test_cases = test_cases[
            : args.cases or config.get("test", {}).get("default_cases", 6)
        ]
        print("  Test mode: GLM Lightweight")
    else:
        test_suite = "standard"
        test_cases = get_test_cases(config, "standard")
        test_cases = test_cases[
            : args.cases or config.get("test", {}).get("default_cases", 6)
        ]
        print("  Test mode: Standard")

    print("=" * 60)
    print(f"LLM Performance Benchmark - {args.model}")
    print("=" * 60)
    print()
    print(f"API: {api_url}")
    print(f"Model: {args.model}")
    print(f"Test Cases: {len(test_cases)}")
    print()

    print("Checking API connection...")
    if not check_api_status(api_url, args.model):
        print(f"[X] Cannot connect to {api_url} or model {args.model}")
        print("Please ensure vLLM server is running")
        sys.exit(1)
    print("[OK] API available")
    print()

    print("Getting GPU info...")
    gpu_info = get_gpu_info()
    if gpu_info:
        print(f"  GPU: {gpu_info.get('name', 'Unknown')}")
        print(f"  Memory: {gpu_info.get('memory', 'Unknown')}")
    print()

    print("Starting tests...")
    print("-" * 60)
    results = []

    for i, tc in enumerate(test_cases, 1):
        print(f"[{i}/{len(test_cases)}] {tc['name']}...", end=" ", flush=True)
        result = run_test(
            api_url,
            args.model,
            timeout,
            tc["prompt"],
            tc["max_tokens"],
            tc["name"],
            is_reasoning_model,
        )
        results.append(result)
        if result.get("success"):
            print(f"{result['elapsed']:.2f}s, {result['generation_speed']:.1f} tok/s")
        else:
            print("[X] Failed")
        time.sleep(0.3)

    print("-" * 60)
    print()

    print("Generating report...")
    report = generate_markdown_report(args.model, results, gpu_info, api_url, config)

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"[OK] Report saved to: {os.path.abspath(report_file)}")
    print()

    successful = [r for r in results if r.get("success")]
    if successful:
        avg_speed = sum(r["generation_speed"] for r in successful) / len(successful)
        print("=" * 60)
        print("Benchmark Complete!")
        print(f"Model: {args.model}")
        print(f"Average Speed: {avg_speed:.1f} tok/s")
        print("=" * 60)

    print()
    print(report)


if __name__ == "__main__":
    main()
