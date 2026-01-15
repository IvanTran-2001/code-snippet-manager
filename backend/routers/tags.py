from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Tag
import schemas

router = APIRouter()


@router.get("", response_model=List[schemas.Tag])
async def list_tags(db: Session = Depends(get_db)):
    """Get all available tags"""
    tags = db.query(Tag).all()
    return tags
