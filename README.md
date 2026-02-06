# LLM Benchmark

Local LLM model performance testing toolkit with multi-model comparison support.

## Features

- Multi-model support (Qwen, GLM, etc.)
- Standardized performance testing
- Auto-generated Markdown reports
- Complex comprehensive test scenarios

## Environment Requirements

| Dependency | Version |
|------------|---------|
| Python | >= 3.10 |
| vLLM | 0.15.2.dev (nightly) |
| transformers | 5.2.0.dev |

## Supported Models

| Model | HF Link | Architecture | Speed (RTX 6000) |
|-------|---------|---------------|-------------------|
| GLM-4.7-Flash | [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash) | Transformer | ~110 tok/s |
| Qwen3-Coder-Next-FP8 | [Qwen/Qwen3-Coder-Next-FP8](https://huggingface.co/Qwen/Qwen3-Coder-Next-FP8) | Mamba2 | ~25 tok/s |

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
python scripts/benchmark.py -m "glm-4.7-flash --complex
```

## Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-m, --model` | Model name | Auto-detect |
| `-u, --api-url` | API URL | http://localhost:8000/v1/chat/completions |
| `-r, --report` | Report filename | Auto |
| `-c, --cases` | Number of test cases | 6 |
| `-x, --complex` | Complex test mode | False |

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

## License

MIT
