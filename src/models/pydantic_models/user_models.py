from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": "$2b$12$CDVEKy.pcnJ.YN7kTsSFlOQBimLD4eydKqpikLwx7tD9d6u5LM0ua",
    }
}
