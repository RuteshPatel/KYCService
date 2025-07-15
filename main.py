import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from surpass_apis.routers import router as kyc_routers
load_dotenv()

app = FastAPI(
    title="True Pay",
    root_path="/api/kyc",
    docs_url="/docs",
    redoc_url="/redoc",
)
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(kyc_routers)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST_URL"),
        port=int(os.getenv("HOST_PORT")),
        log_level="info",
        reload=True
    )

