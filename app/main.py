from fastapi import APIRouter, Depends, FastAPI, HTTPException
import app.auth.router as auth_router
import app.fridge.router as fridge_router

app = FastAPI()

api_router = APIRouter()
api_router.include_router(auth_router.router)
api_router.include_router(fridge_router.router)

app.include_router(api_router)
