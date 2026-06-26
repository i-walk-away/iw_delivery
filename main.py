from fastapi import FastAPI
from uvicorn import Config, Server

from cfg.cfg import settings
from src.iw_delivery.api.v1 import auth, items, orders, users


def build_app() -> FastAPI:
    app = FastAPI(
        title="IW Delivery",
        description="FastAPI backend service for a simple operator-assisted food delivery",
        version="0.1.0",
        swagger_ui_parameters={"operationsSorter": "method"},
    )

    app.include_router(items.router)
    app.include_router(users.router)
    app.include_router(orders.router)
    app.include_router(auth.router)

    return app


def main() -> None:
    config = Config(
        app=build_app(),
        host=settings.host,
        port=settings.port,
    )

    server = Server(config)
    server.run()


if __name__ == '__main__':
    main()
