from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.iw_delivery.core.dependencies.db import get_session
from src.iw_delivery.repositories.db.users import UserRepository


def get_user_repository(
        session: AsyncSession = Depends(get_session),
) -> UserRepository:
    """
    Constructs a UserRepository instance with injected AsyncSession.
    """
    return UserRepository(session)
