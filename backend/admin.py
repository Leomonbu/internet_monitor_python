from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from backend.database import logs_collection
import os
from fastapi.templating import Jinja2Templates

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

router = APIRouter()

templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "admin-ui"))


@router.get("/admin")
def panel_admin(request: Request, usuario: str = None, dominio: str = None):

    query = {}

    if usuario:
        query["usuario"] = usuario

    if dominio:
        query["dominio"] = dominio

    logs = list(
        logs_collection.find(query, {"_id": 0})
        .sort("fecha_servidor", -1)
        .limit(100)
    )

    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
            "logs": logs,
            "usuario": usuario,
            "dominio": dominio
        }
    )


@router.get("/admin/top-sites")
async def top_sites(request: Request):
#async def top_sites():


    pipeline = [
        {
            "$group": {
                "_id": "$dominio",
                "total_visits": {"$sum": 1}
            }
        },
        {"$sort": {"total_visits": -1}},
        {"$limit": 20}
    ]

    results = list(logs_collection.aggregate(pipeline))

    return templates.TemplateResponse(
        "top_sites.html",
        {
            "request": request,
            "sites": results
        }
    )