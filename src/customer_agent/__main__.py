"""Run the FastAPI service with ``python -m customer_agent``."""

from __future__ import annotations

import os

import uvicorn


def main() -> None:
    uvicorn.run(
        "customer_agent.api_server:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        workers=1,
    )


if __name__ == "__main__":
    main()
