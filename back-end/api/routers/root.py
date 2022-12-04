from fastapi import APIRouter


prefix = ""
router = APIRouter(
    prefix=f"{prefix}",
    tags=[prefix],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def welcome():
    """Display a welcome message."""
    return {"message": "Welcome to the API!"}
