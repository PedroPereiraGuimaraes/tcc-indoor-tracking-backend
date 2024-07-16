from typing import Annotated, Optional
from pydantic import BaseModel, BeforeValidator, Field, ConfigDict
from datetime import datetime

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

# Generic message
class Message(BaseModel):
    message: str

# User shared properties
class UserBase(BaseModel):
     name: str = Field(...)
     email: str = Field(...)
     password: str = Field(...)
    #  model_config = ConfigDict(
    #     # populate_by_name=True, # precisa disso?
    #     arbitrary_types_allowed=True, # precisa disso
    #     json_schema_extra={
    #         "example": {"name": "Frida Gilbert",
    #                      "email": "frida_gilbert@gmail.com",
    #                      "password": "12345678",
    #                      "register": "1212",
    #                      "maintenance": False}
    #     },
    # )

class UserData(UserBase):
    # id: Optional[PyObjectId] = Field(alias="_id", default=None)
    isAdmin: bool = Field(default=False)

class UsersDataList(BaseModel):
    users: list[UserData]

class Login(BaseModel):
    email: str = Field(...)
    password: str = Field(...)

class UserAdmin(BaseModel):
    email: str = Field(...)
    isAdmin: bool = Field(default=False)

class EquipmentBase(BaseModel):
    name: str = Field(...)
    register_: str = Field(alias="register")
    maintenance: bool = Field(default=False)
    c_room: str = Field(...)
    c_date: datetime = Field(...)

class EquipmentHistory(BaseModel):
    start_date: datetime = Field(...)
    room: str = Field(...)

class Equipment(EquipmentBase):
    history: EquipmentHistory = Field(...)
    esp_id: Optional[str] = Field(...)


class Equipment_maintenance(BaseModel):
    patrimonio: str
    name: str
    last_maintenance: datetime
    next_maintenance: datetime

class Equipment_update(BaseModel):
    patrimonio: str
    name: str
    last_maintenance: datetime
    next_maintenance: datetime
