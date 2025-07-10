import random

from fastapi import APIRouter
from starlette import status

from common.response import ApiResponse

router = APIRouter(prefix="/surpass", tags=["Surpass API's"])


@router.get("/get-cibil-score", summary="Get Cibil Score")
async def get_cibil_score():
    response = {
        "success": True,
        "message": "Your CIBIL score has been retrieved successfully!",
        "status_code": status.HTTP_200_OK,
        "data": {
            "score": random.randint(200, 900)
        }
    }
    return ApiResponse.create_response(
        success=response.get("success"), message=response.get("message"),
        status_code=response.get("status_code") if response.get(
            "status_code"
        ) else status.HTTP_200_OK,
        data=response.get("data")
    )
