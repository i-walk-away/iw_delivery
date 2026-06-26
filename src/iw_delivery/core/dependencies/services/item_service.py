from fastapi import Depends

from src.iw_delivery.core.dependencies.repositories.item_repository import get_item_repository
from src.iw_delivery.repositories.db.items import ItemRepository
from src.iw_delivery.services.item_service import ItemService


def get_item_service(
        repository: ItemRepository = Depends(get_item_repository),
) -> ItemService:
    """
    Constructs an ItemService instance with injected ItemRepository.
    """
    return ItemService(repository)
