# LLM Benchmark

[中文文档](README_CN.md) | English

Local LLM model performance testing toolkit with multi-model comparison support.

## Features

- Multi-model support (Qwen, GLM, etc.)
- Multi-backend support (vLLM, SGLang)
- Standardized performance testing
- Auto-generated Markdown reports
- Complex comprehensive test scenarios
- Auto-update config for new models

## Environment Requirements

| Dependency | Version |
|------------|---------|
| Python | >= 3.10 |
| vLLM | 0.15.2.dev (nightly) |
| transformers | 5.2.0.dev |

## Supported Models

| Model | HF Link | Architecture | Speed (RTX PRO 6000) |
|-------|---------|---------------|---------------------|
| GLM-4.7-Flash | [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash) | Transformer | 112.9 tok/s |
| Qwen3.5-35B-A3B | [Qwen/Qwen3.5-35B-A3B](https://huggingface.co/Qwen/Qwen3.5-35B-A3B) | Transformer | 165.7 tok/s |
| Qwen3-Coder-Next-FP8 | [Qwen/Qwen3-Coder-Next-FP8](https://huggingface.co/Qwen/Qwen3-Coder-Next-FP8) | Mamba2 | 138.6 tok/s |

## Project Structure

```
llm/
├── scripts/           # Test scripts
│   └── benchmark.py   # Main benchmark script
├── .github/          # CI/CD configuration
│   └── workflows/
│       └── benchmark.yml
├── .gitignore
├── pyproject.toml    # Project configuration
└── README.md
```

## Quick Start

### Install uv (if not installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install Dependencies

```bash
# Using uv
uv sync

# Or run directly
uv run python scripts/benchmark.py -m "glm-4.7-flash"
```

### Create Virtual Environment

```bash
uv venv
source .venv/bin/activate
uv sync
```

## Usage

### Standard Test

```bash
# Auto-detect available models
python scripts/benchmark.py

# Specify model
python scripts/benchmark.py -m "glm-4.7-flash"
```

### Complex Comprehensive Test

```bash
# 10 comprehensive test scenarios
python scripts/benchmark.py -m "glm-4.7-flash" --complex
```

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-m, --model` | Model name | Auto-detect |
| `-u, --api-url` | Full API URL | Built from backend/port |
| `-b, --backend` | API backend (vllm/sglang) | vllm |
| `-p, --port` | API port | 8000 (vllm) / 30000 (sglang) |
| `-r, --report` | Report filename | Auto |
| `-c, --cases` | Number of test cases | 6 |
| `-x, --complex` | Complex test mode | False |
| `--config` | Config file path | scripts/benchmark_config.yaml |
| `--auto-update` | Auto-update config | Enabled |
| `--no-auto-update` | Disable auto-update | - |

## API Differences

### GLM-4.7-Flash

```json
{
  "model": "glm-4.7-flash",
  "messages": [{"role": "user", "content": "Hello"}],
  "max_tokens": 100
}
```

- **Special field**: Uses `reasoning` field for thought process
- **Response format**: `content` may be `null`, check `reasoning` field

### Qwen3-Coder-Next-FP8

```json
{
  "model": "Qwen/Qwen3-Coder-Next-FP8",
  "messages": [{"role": "user", "content": "Hello"}],
  "max_tokens": 100
}
```

- **Standard format**: Standard OpenAI-compatible response
- **Architecture**: Mamba2, slower inference but stronger coding ability

## Multi-Backend Usage

### Test with vLLM (default, port 8000)

```bash
# Auto-detect model
python scripts/benchmark.py

# Explicitly specify vLLM
python scripts/benchmark.py --backend vllm
python scripts/benchmark.py -b vllm

# With custom port
python scripts/benchmark.py --port 8000
python scripts/benchmark.py -p 8000
```

### Test with SGLang (port 30000)

```bash
# Using backend flag
python scripts/benchmark.py --backend sglang
python scripts/benchmark.py -b sglang

# Using port (auto-detects sglang)
python scripts/benchmark.py --port 30000
python scripts/benchmark.py -p 30000

# Complex test with sglang
python scripts/benchmark.py -x --backend sglang
python scripts/benchmark.py -x -b sglang

# Full URL (override)
python scripts/benchmark.py --api-url http://localhost:30000/v1/chat/completions
```

### Auto-Update Config

When a new model is detected, the script automatically adds it to the config file:

```bash
# Enable auto-update (default)
python scripts/benchmark.py --auto-update

# Disable auto-update
python scripts/benchmark.py --no-auto-update
```

## Start vLLM Server

```bash
# GLM-4.7-Flash
CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0 vllm serve zai-org/GLM-4.7-Flash \
  --speculative-config.method mtp \
  --speculative-config.num_speculative_tokens 1 \
  --tool-call-parser glm47 \
  --reasoning-parser glm45 \
  --enable-auto-tool-choice \
  --served-model-name glm-4.7-flash \
  --trust-remote-code \
  --gpu-memory-utilization 0.9

# Qwen3-Coder-Next-FP8 (Mamba2 architecture)
CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen3-Coder-Next-FP8 \
  --port 8000 \
  --tensor-parallel-size 1 \
  --enforce-eager \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --max-model-len 131072
```

## Start SGLang Server

```bash
# SGLang with Docker
docker run -d --gpus all \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  --network host \
  --name sglang \
  lmsysorg/sglang:latest \
  python -m sglang.launcher \
  --model Qwen/Qwen3-Coder-Next-FP8 \
  --port 30000

# Or run directly with sglang
python -m sglang.launcher \
  --model Qwen/Qwen3-Coder-Next-FP8 \
  --port 30000 \
  --max-model-len 131072
```

## License

MIT
