from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.cultures import culture_router
from app.routes.dashboard import dash_router
from app.routes.farms import farm_router
from app.routes.producers import producer_router

app = FastAPI(
    title="Brain Agriculture API",
    description="API de produtores, areas e culturas"
)

app.include_router(culture_router)
app.include_router(dash_router)
app.include_router(farm_router)
app.include_router(producer_router)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)