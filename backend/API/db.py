import databases
import ormar
import sqlalchemy
from enum import Enum

from .config import settings

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database

class Client(ormar.Model):
    class Meta(BaseMeta):
        tablename="clients"

    id: int = ormar.Integer(primary_key=True)
    creditsNumber: int = ormar.Integer()

class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)
    isAdmin: bool = ormar.Boolean(default=False, nullable=False)
    clientId: Client = ormar.ForeignKey(Client, name="clientId")


class Variant(ormar.Model):
    class Meta(BaseMeta):
        tablename = "db_variants"
    
    id: int = ormar.Integer(primary_key=True)
    chromosome: str = ormar.String(max_length=16, unique=False, nullable=False)
    position: int = ormar.Integer(unique=False, nullable=False)
    consequence: str = ormar.String(max_length=128, unique=False, nullable=True)
    gene: str = ormar.String(max_length=64, unique=False, nullable=True)
    exonic: bool = ormar.Boolean(default=False)
    depth: int = ormar.Integer(unique=False, nullable=False)

class TaskStages(Enum):
    s = 'started'
    a = 'allocating containers'
    p = 'pending'
    f = 'finished'
    q = 'quitted'


class Task(ormar.Model):
    class Meta(BaseMeta):
        tablename = "tasks"

    id: int = ormar.Integer(primary_key=True)
    status: str = ormar.String(max_length=256, choices = list(TaskStages))
    changedAt: str = ormar.DateTime


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)