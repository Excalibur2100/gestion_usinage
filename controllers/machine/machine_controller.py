from fastapi import APIRouter

router = APIRouter(prefix="/machine", tags=["machine"])

@router.get("/")
async def get_machine():
    return {"message": "Machine opérationnelle"}