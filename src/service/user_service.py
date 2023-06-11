from db import SessionLocal
from model import User

db = SessionLocal()

class UserService:
    @staticmethod
    def create(user_data):
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_all_users():
        return db.query(User).all()
