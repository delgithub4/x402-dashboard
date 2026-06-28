from fastapi import APIRouter

from services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

dashboard = DashboardService()


@router.get("/")
def overview():

    return dashboard.overview()
