from fastapi import FastAPI
from datetime import datetime, timezone
from backend.database import logs_collection
from backend.admin import router as admin_router
from fastapi.responses import Response

app = FastAPI()
app.include_router(admin_router)


@app.get("/")
def root():
    return {"status": "API funcionando"}


@app.post("/log")
async def registrar_log(data: dict):

    data["fecha_servidor"] = datetime.now(timezone.utc)

    logs_collection.insert_one(data)

    return {"status": "log guardado"}

@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)