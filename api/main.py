from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.app.routes import equipment, user
import uvicorn

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

api.include_router(user.router, prefix="/user", tags=["user"])
api.include_router(equipment.router, prefix="/equipment", tags=["equipment"])

if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)
