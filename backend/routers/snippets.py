from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from typing import List
from database import get_db
from models import User, Snippet, Tag
from auth import get_current_user
import schemas

router = APIRouter()


@router.post("", response_model=schemas.Snippet)
async def create_snippet(
    snippet: schemas.SnippetCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Create a new code snippet"""
    db_snippet = Snippet(
        title=snippet.title,
        description=snippet.description,
        code=snippet.code,
        language=snippet.language,
        user_id=current_user.id,
        is_public=int(snippet.is_public),
    )

    # Add tags
    if snippet.tags:
        for tag_name in snippet.tags:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
            db_snippet.tags.append(tag)

    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)
    return db_snippet


@router.get("", response_model=List[schemas.Snippet])
async def list_snippets(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all snippets for current user"""
    snippets = db.query(Snippet).options(joinedload(Snippet.tags)).filter(Snippet.user_id == current_user.id).all()
    return snippets


@router.get("/public", response_model=List[schemas.Snippet])
async def list_public_snippets(db: Session = Depends(get_db)):
    """Get all public snippets"""
    snippets = db.query(Snippet).options(joinedload(Snippet.tags)).filter(Snippet.is_public == 1).all()
    return snippets


@router.get("/{snippet_id}", response_model=schemas.Snippet)
async def get_snippet(
    snippet_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get a specific snippet"""
    snippet = db.query(Snippet).filter(Snippet.id == snippet_id).first()
    if not snippet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Snippet not found",
        )

    # Check permissions
    if snippet.user_id != current_user.id and not snippet.is_public:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    # Increment view count if public
    if snippet.is_public:
        snippet.view_count += 1
        db.commit()

    return snippet


@router.put("/{snippet_id}", response_model=schemas.Snippet)
async def update_snippet(
    snippet_id: int,
    snippet_update: schemas.SnippetUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update a snippet"""
    db_snippet = db.query(Snippet).filter(Snippet.id == snippet_id).first()
    if not db_snippet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Snippet not found",
        )

    if db_snippet.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    # Update fields
    if snippet_update.title:
        db_snippet.title = snippet_update.title
    if snippet_update.description is not None:
        db_snippet.description = snippet_update.description
    if snippet_update.code:
        db_snippet.code = snippet_update.code
    if snippet_update.language:
        db_snippet.language = snippet_update.language
    if snippet_update.is_public is not None:
        db_snippet.is_public = int(snippet_update.is_public)

    if snippet_update.tags is not None:
        db_snippet.tags.clear()
        for tag_name in snippet_update.tags:
            tag = db.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.add(tag)
            db_snippet.tags.append(tag)

    db.commit()
    db.refresh(db_snippet)
    return db_snippet


@router.delete("/{snippet_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_snippet(
    snippet_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a snippet"""
    db_snippet = db.query(Snippet).filter(Snippet.id == snippet_id).first()
    if not db_snippet:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Snippet not found",
        )

    if db_snippet.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied",
        )

    db.delete(db_snippet)
    db.commit()
