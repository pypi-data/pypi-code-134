
from typing import AsyncGenerator
from sqlalchemy import Column, Integer, String
import uuid
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy import update
import fastapi_users_db_sqlalchemy
import os


# DATABASE_URL = os.getenv("DB_URL")
# name = os.getenv("POSTGRES_USER")
# password = os.getenv("POSTGRES_PASSWORD")
# DATABASE_URL = "postgresql+asyncpg://localhost:1234@localhost:5432/test"
# DATABASE_URL= 'postgresql+asyncpg://name:password@host:port/db'
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
Base: DeclarativeMeta = declarative_base()

class User(SQLAlchemyBaseUserTableUUID, Base):
    org_id = Column(fastapi_users_db_sqlalchemy.generics.GUID())
    org_name = Column(String)

engine = create_async_engine("postgresql+asyncpg://postgres:1234@localhost:5432/test")
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def update_orgid(user):
    # print(temp)
    async with async_session_maker() as session:
        # q = select(User).where(User.id == userid)
        # result = await session.execute(q)
        # curr = result.scalars().first()
        # curr.org_id = curr.id
        # await session.update(curr)
        # await session.commit()

        # user = select(User).where(User.id == userid)
        # r_user = await session.execute(user)
        # if r_user.scalars().first():

        org_id = select(User).where(User.org_name == user.org_name and User.id != user.id)
        r_orgid = await session.execute(org_id)
        oid = r_orgid.scalars().first()
        print(oid)

        if oid:
            orgid =  user.id if oid.org_id == None else oid.org_id

        else:
            orgid = user.id
        q = update(User).where(User.id == user.id).values(org_id = orgid)
            
        await session.execute(q)
        await session.commit()
        return orgid

        # q = update(User).where(User.id == userid).values(org_id = userid)
        # r = await session.execute(q)
        # await session.commit()
        # print(r.scalars().first())

