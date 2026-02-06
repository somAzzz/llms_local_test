# LLM Benchmark

本地 LLM 模型性能测试工具集，支持多种模型对比测试。

## 功能特性

- 多模型支持（Qwen、GLM 等）
- 标准化性能测试
- 自动生成 Markdown 报告
- 复杂综合测试场景

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
| `-u, --api-url` | API 地址 | http://localhost:8000/v1/chat/completions |
| `-r, --report` | 报告文件名 | auto |
| `-c, --cases` | 测试用例数量 | 6 |
| `-x, --complex` | 复杂测试模式 | False |

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

## 许可证

MIT
