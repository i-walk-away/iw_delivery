from pydantic import BaseModel

from src.iw_delivery.models.dto.items import ItemDTO


class OrderItemDTO(BaseModel):
    item: ItemDTO
    quantity: int


class OrderDTO(BaseModel):
    id: int
    items: list[OrderItemDTO]
    is_placed: bool


class AddItemToOrder(BaseModel):
    item_id: int


class RemoveItemFromOrder(BaseModel):
    item_id: int
