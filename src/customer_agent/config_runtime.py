"""V6 初赛提交版默认运行配置。

该文件只保存非敏感默认值：`api_server.py` / `llm_router.py` 会在启动时
调用 `apply_default_env()`，把这里的配置写入尚未设置的环境变量。

API key、服务端 Bearer Token 和私有 endpoint 必须通过环境变量或 `.env`
提供，不应写入源码。
"""
from __future__ import annotations

import os


DEFAULT_ENV = {
    # 在线接口超时：公网/评审环境保守放宽，减少上游波动导致的误判。
    "CHAT_TIMEOUT_S": "50",
    "CHAT_MULTIMODAL_TIMEOUT_S": "60",
    "CHAT_MAX_IMAGES": "3",
    "CHAT_MAX_IMAGE_BYTES": str(5 * 1024 * 1024),

    # 无 qid 在线场景的 service / tech 二分类路由器。
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
    "DEEPSEEK_BINARY_MODEL": "deepseek-v4-flash",
    "DEEPSEEK_BINARY_TIMEOUT": "3",
    "DEEPSEEK_BINARY_MAX_TOKENS": "4",

    # 主回答模型的 endpoint、key 和 model 由部署环境显式提供。
    "SILICONFLOW_ONLY": "1",
    "SILICONFLOW_MAX_CONCURRENCY": "3",
    "AGENT_MAX_TOKENS": "8192",
    "LLM_TIMEOUT_SECONDS": "30",
    "LLM_TRANSIENT_RETRY_ATTEMPTS": "3",

    # 检索：默认使用硅基流动远程 embedding / rerank，评审不需要本地启动 8091/8090。
    "EMBEDDING_BASE_URL": "https://api.siliconflow.cn/v1",
    "EMBEDDING_MODEL": "Pro/BAAI/bge-m3",
    "EMBEDDING_MAX_CONCURRENCY": "4",
    "RERANK_BASE_URL": "https://api.siliconflow.cn/v1",
    "RERANK_MODEL_ALIAS": "BAAI/bge-reranker-v2-m3",
    "RERANK_ENABLED": "1",

    # chunk 命中后返回完整 parent section。
    "RETURN_PARENT_SECTION": "1",
}


def apply_default_env() -> None:
    """Apply delivery defaults without overriding variables already set by the caller."""
    for key, value in DEFAULT_ENV.items():
        os.environ.setdefault(key, value)
