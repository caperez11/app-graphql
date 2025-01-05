import uuid

import strawberry
from fastapi import FastAPI, Depends
from sqlmodel import Session
from strawberry.fastapi import GraphQLRouter

from app.api.graphql.custom_graphql_context import CustomGraphQLContext
from app.api.graphql.query import Query
from app.core.db import init_db, get_session, engine

from app.models.user import User
from app.services.user import UserService

app = FastAPI()

# Inicializar la base de datos al iniciar la aplicación
init_db()


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
async def root(session: Session = Depends(get_session)):
    new_user = User(uuid=str(uuid.uuid4()), username="johndoe", email="test@gmail.com", is_active=True)

    session.add(new_user)  # Añade el usuario
    session.commit()  # Guarda los cambios (transacción)
    session.refresh(new_user)  # Refleja la instancia con los datos generados

    return {"message": "User created", "user": new_user.dict()}


@app.get("/users")
async def get_all_users(service: UserService = Depends(UserService)):
    """RUTA: Obtiene todos los usuarios."""
    users = await service.get_users()  # Obtiene los usuarios desde el servicio
    return {"users": users}


