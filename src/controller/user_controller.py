from fastapi import APIRouter
from schema.user_schema import UserSchema
from service.user_service import UserService
from fastapi import Request

router = APIRouter()
user_service = UserService()


@router.post("/")
async def create_user(request: Request, status_code=201):
    user_data = await request.json()
    user = user_service.create(user_data)
    return user


@router.get("/")
def get_all_users():
    users = user_service.get_all_users()
    return users
