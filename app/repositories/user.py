from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select

from app.core.db import get_session, engine  # Importa el gestor de sesión desde tu proyecto
from app.models.user import User


class UserRepository:
    # def __init__(self, session: Session = Depends(get_session)):  # Inyección aquí
    #     self.session = session

    @staticmethod
    async def get_users():
         with Session(engine) as session:
            query = select(User)
            result =  session.exec(query).all()
            return result


    # def add_user(self, user: User):
    #     """Agrega un usuario a la base de datos"""
    #     self.session.add(user)
    #     self.session.commit()
    #     self.session.refresh(user)
    #     return user
    #
    # async def get_user_by_id(self, user_id: int):
    #     """Obtiene un usuario basado en su ID"""
    #     result = await self.session.execute(
    #         "SELECT * FROM user WHERE id = :id", {"id": user_id}
    #     )
    #     return result.fetchone()
