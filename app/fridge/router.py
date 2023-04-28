from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.fridge.schemas import Item, ItemCreate
from app.fridge.models import get_items, create_user_item


router = APIRouter()


@router.post("/users/{user_id}/items/", response_model=Item)
def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items(db, skip=skip, limit=limit)
    return items
