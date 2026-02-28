# LLM Benchmark

[English](README.md) | 中文文档

本地 LLM 模型性能测试工具集，支持多种模型对比测试。

## 功能特性

- 多模型支持（Qwen、GLM 等）
- 多后端支持（vLLM、SGLang）
- 标准化性能测试
- 自动生成 Markdown 报告
- 复杂综合测试场景
- 自动更新配置以支持新模型

## 环境要求

| 依赖 | 版本 |
|-----|------|
| Python | >= 3.10 |
| vLLM | 0.15.2.dev (nightly) |
| transformers | 5.2.0.dev |

## 支持的模型

| 模型 | HF 链接 | 架构 | 速度 (RTX 6000) |
|-----|--------|------|-----------------|
| GLM-4.7-Flash | [zai-org/GLM-4.7-Flash](https://huggingface.co/zai-org/GLM-4.7-Flash) | Transformer | ~110 tok/s |
| Qwen3-Coder-Next-FP8 | [Qwen/Qwen3-Coder-Next-FP8](https://huggingface.co/Qwen/Qwen3-Coder-Next-FP8) | Mamba2 | ~25 tok/s |

## 目录结构

```
llm/
├── scripts/           # 测试脚本
│   └── benchmark.py   # 主测试脚本
├── .github/          # CI/CD 配置
│   └── workflows/
│       └── benchmark.yml
├── .gitignore
├── pyproject.toml    # 项目配置
└── README.md
```

## 快速开始

### 安装 uv（如果未安装）

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 安装依赖

```bash
# 使用 uv
uv sync

# 或直接运行脚本
uv run python scripts/benchmark.py -m "glm-4.7-flash"
```

### 创建虚拟环境

```bash
uv venv
source .venv/bin/activate
uv sync
```

### 使用方法

#### 标准测试

```bash
# 自动检测可用模型并测试
python scripts/benchmark.py

# 指定模型测试
python scripts/benchmark.py -m "glm-4.7-flash"
```

#### 复杂综合测试

```bash
# 10个综合测试场景
python scripts/benchmark.py -m "glm-4.7-flash" --complex
```

## 命令行参数

| 参数 | 说明 | 默认值 |
|-----|------|-------|
| `-m, --model` | 模型名称 | 自动检测 |
| `-u, --api-url` | 完整 API 地址 | 根据 backend/port 构建 |
| `-b, --backend` | API 后端 (vllm/sglang) | vllm |
| `-p, --port` | API 端口 | 8000 (vllm) / 30000 (sglang) |
| `-r, --report` | 报告文件名 | auto |
| `-c, --cases` | 测试用例数量 | 6 |
| `-x, --complex` | 复杂测试模式 | False |
| `--config` | 配置文件路径 | scripts/benchmark_config.yaml |
| `--auto-update` | 自动更新配置 | 启用 |
| `--no-auto-update` | 禁用自动更新 | - |

## API 调用差异

### GLM-4.7-Flash

```json
{
  "model": "glm-4.7-flash",
  "messages": [{"role": "user", "content": "Hello"}],
  "max_tokens": 100
}
```

- **特殊字段**: 使用 `reasoning` 字段输出思考过程
- **响应格式**: `content` 可能为 `null`，需检查 `reasoning` 字段

### Qwen3-Coder-Next-FP8

```json
{
  "model": "Qwen/Qwen3-Coder-Next-FP8",
  "messages": [{"role": "user", "content": "Hello"}],
  "max_tokens": 100
}
```

- **标准格式**: 标准 OpenAI 兼容响应
- **架构**: Mamba2，推理速度较慢但代码能力强

## 多后端使用

### 使用 vLLM 测试（默认，端口 8000）

```bash
# 自动检测模型
python scripts/benchmark.py

# 显式指定 vLLM
python scripts/benchmark.py --backend vllm
python scripts/benchmark.py -b vllm

# 指定端口
python scripts/benchmark.py --port 8000
python scripts/benchmark.py -p 8000
```

### 使用 SGLang 测试（端口 30000）

```bash
# 使用 backend 参数
python scripts/benchmark.py --backend sglang
python scripts/benchmark.py -b sglang

# 使用端口参数（自动识别 sglang）
python scripts/benchmark.py --port 30000
python scripts/benchmark.py -p 30000

# 复杂测试 + sglang
python scripts/benchmark.py -x --backend sglang
python scripts/benchmark.py -x -b sglang

# 使用完整 URL（覆盖其他设置）
python scripts/benchmark.py --api-url http://localhost:30000/v1/chat/completions
```

### 自动更新配置

当检测到新模型时，脚本会自动将其添加到配置文件中：

```bash
# 启用自动更新（默认）
python scripts/benchmark.py --auto-update

# 禁用自动更新
python scripts/benchmark.py --no-auto-update
```

## 启动 vLLM 服务

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

# Qwen3-Coder-Next-FP8 (Mamba2 架构)
CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=0 vllm serve Qwen/Qwen3-Coder-Next-FP8 \
  --port 8000 \
  --tensor-parallel-size 1 \
  --enforce-eager \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --max-model-len 131072
```

## 启动 SGLang 服务

```bash
# 使用 Docker 运行 SGLang
docker run -d --gpus all \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  --network host \
  --name sglang \
  lmsysorg/sglang:latest \
  python -m sglang.launcher \
  --model Qwen/Qwen3-Coder-Next-FP8 \
  --port 30000

# 或直接运行 sglang
python -m sglang.launcher \
  --model Qwen/Qwen3-Coder-Next-FP8 \
  --port 30000 \
  --max-model-len 131072
```

## 许可证

MIT
