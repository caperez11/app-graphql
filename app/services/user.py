from fastapi import Depends

from app.repositories.user import UserRepository
from app.schemes.user import UserType


class UserService:
    # def __init__(self, repository: UserRepository = Depends(UserRepository)):  # Inyección aquí
    #     self.repository = repository


    @staticmethod
    async def get_users():
        # lst_user = await self.repository.get_users()
        lst_user = await UserRepository.get_users()
        return [UserType(id=user.id, username=user.username, uuid=user.uuid) for user in lst_user]
