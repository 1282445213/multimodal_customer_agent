# Multimodal Customer Agent

一个面向产品说明书问答的多模态客服智能体代码项目。系统将通用客服与产品技术问题分流，并在技术链路中结合产品路由、BM25、向量检索、重排、父章节返回以及图片锚点生成回答。

本仓库只公开代码，不包含比赛题目、产品手册、图片、检索索引、提交结果或任何 API 密钥。

## 代码结构

```text
src/customer_agent/       API、Agent、检索、路由与输出格式化
tools/data_pipeline/      手册解析、章节总结与索引构建
tools/generation/         离线和 API 批量生成工具
tools/local_services/     可选的本地 embedding/rerank 服务
tools/validation/         代码结构与交付验证工具
scripts/                  PowerShell 和 Bash 启动脚本
```

## 环境要求

- Python 3.10 或 3.11
- 依赖见 `requirements.txt`
- 单独准备手册、图片和检索索引等运行资产

```bash
pip install -e .
```

## 运行资产

通过 `KBRAG_ASSET_ROOT` 指向外部资产目录。目录至少应按需包含：

```text
data/
  catalog.json
  section_chunks.json
  retrieval_chunks.json
  image_captions_v4_final.json
  index/
    dense.faiss
    retrieval_index.pkl
手册_v4/
手册/插图/
```

## 环境变量

运行前通过系统环境变量或本地 `.env` 提供私密配置，不要提交真实值：

```text
KAFU_API_TOKEN=<service-token>
DEEPSEEK_API_KEY=<classifier-key>
SILICONFLOW_BASE_URL=<openai-compatible-endpoint>
SILICONFLOW_API_KEY=<answer-model-key>
SILICONFLOW_MODEL=<answer-model-name>
EMBEDDING_API_KEY=<embedding-key>
RERANK_API_KEY=<rerank-key>
KBRAG_ASSET_ROOT=<absolute-asset-directory>
```

## 启动

Windows PowerShell：

```powershell
.\scripts\run_api.ps1
```

Linux/macOS：

```bash
./scripts/run_api.sh
```

接口默认监听 `http://127.0.0.1:8000`，健康检查为 `GET /health`，对话接口为 `POST /chat`。

## 本地静态检查

```powershell
$env:PYTHONPATH = "$PWD\src"
python -m tools.validation.validate_code_layout
```

静态检查不访问外部模型服务。

## 安全说明

- 不要把 `.env`、访问令牌、用户对话日志或原始客户图片提交到仓库。
- 上传图片会发送给配置的多模态模型服务，生产部署前需确认隐私、数据保留和跨境传输策略。
- `retrieval_index.pkl` 使用 Python pickle 格式，只应加载可信来源生成的索引。
