from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    id: int
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserCreateResponse(UserBase):
    is_active: bool
    is_superuser: bool
    created_at: str
    class Config:
        orm_mode = True

