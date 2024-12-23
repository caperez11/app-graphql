from sqlalchemy import QueuePool
from sqlmodel import SQLModel, create_engine, Session

from app.core.settings import settings

# Crear el motor de SQLModel usando la URL de la base de datos de settings
engine = create_engine(
    settings.database_url,  # URL de la base de datos
    echo=settings.is_show_sql,  # Modo verboso para mostrar detalles de consultas SQL
    poolclass=QueuePool,  # Usamos QueuePool (pool de conexiones por defecto de SQLAlchemy)
    pool_size=10,  # Número máximo de conexiones abiertas
    max_overflow=20,  # Conexiones extra permitidas si el pool está lleno
    pool_timeout=30  # Tiempo máximo (en segundos) para esperar antes de lanzar un error
)


# Crear las tablas en la base de datos (si no existen)
def init_db():
    # Esta función se llamará al iniciar la aplicación
    SQLModel.metadata.create_all(engine)


# Obtener un contexto de sesión de la base de datos
def get_session():
    with Session(engine) as session:
        yield session
