from typing import List

import strawberry
from fastapi import Depends
from strawberry import Info

from app.schemes.user import UserType
from app.services.user import UserService


@strawberry.type
class Query:
    # def __init__(self, service: UserService = Depends(UserService)):  # Inyección aquí
    #     self.service = service

    @strawberry.field
    def hello(self) -> str:
        return "Hello World!"

    @strawberry.field
    async def users(self) -> List[UserType]:
        """Obtiene una lista de todos los usuarios desde el contexto."""
        users: list[UserType] = await UserService.get_users()

        return users


    # @strawberry.field
    # async def users(self, service: UserService = Depends(UserService)) -> List[UserType]:
    #     """Obtiene una lista de todos los usuarios."""
    #
    #     users = await service.get_users()
    #     return users
