from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login")
async def login():
    return {"login"}

@router.post("/signup")
async def signup():
    return {"signup"}