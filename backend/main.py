from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import logging
import uvicorn
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from chem_compute_routes import router as chem_compute_routes
import os

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(chem_compute_routes, prefix="/general")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
