from fastapi import Depends
from passlib.context import CryptContext

from src.iw_delivery.core.dependencies.auth.context import get_context
from src.iw_delivery.core.security import AuthenticationManager


def get_authentication_manager(
        context: CryptContext = Depends(get_context)
) -> AuthenticationManager:
    """
    Constructs an AuthenticationManager instance with injected
    passlib.CryptContext.
    """
    return AuthenticationManager(context)
