from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from routes.furniture import furniture_router
from routes.comment import comment_router
from config import HOST, PORT, auto_reload

import uvicorn

app = FastAPI(title="API'S")

app.include_router(furniture_router, prefix="/furniture")
app.include_router(comment_router, prefix="/comment")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=auto_reload)
