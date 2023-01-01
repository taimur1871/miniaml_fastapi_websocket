"""
Try to create and close websocket connection
"""
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware


def init_router():
    """
    include app routers
    """
    import app_info, websockets_router, csv_router

    router = APIRouter()
    # keep alphabetical order
    router.include_router(app_info.router)
    router.include_router(websockets_router.router)
    router.include_router(csv_router.router)

    return router


app = FastAPI(
    title='FastAPI Websocket'
)

app.include_router(init_router())

# enable CORS
origins = [
    "*",
    "http://localhost",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
