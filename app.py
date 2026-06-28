from fastapi import FastAPI

from routes.dashboard import router as dashboard_router
from routes.health import router as health_router

app = FastAPI(
    title="x402-dashboard",
    version="1.0.0"
)

app.include_router(dashboard_router)
app.include_router(health_router)


@app.get("/")
def home():

    return {

        "service":"x402-dashboard",

        "status":"running"

    }
