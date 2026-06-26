from fastapi import Depends

from src.iw_delivery.core.dependencies.auth.authentication_manager import get_authentication_manager
from src.iw_delivery.core.dependencies.repositories.user_repository import get_user_repository
from src.iw_delivery.core.security import AuthenticationManager
from src.iw_delivery.repositories.db.users import UserRepository
from src.iw_delivery.services.user_service import UserService


def get_user_service(
        repository: UserRepository = Depends(get_user_repository),
        authentication_manager: AuthenticationManager = Depends(get_authentication_manager),
) -> UserService:
    """
    Constructs a UserService instance with injected UserRepository and AuthenticationManager.
    """
    return UserService(repository, authentication_manager)
