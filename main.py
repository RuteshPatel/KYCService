import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from surpass_apis.routers import router as kyc_routers

app = FastAPI(
    title="True Pay",
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
        host="localhost",
        port=8000,
        log_level="info",
        reload=True
    )
