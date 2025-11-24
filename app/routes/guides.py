from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import SessionLocal
from app.models.guide import Guide
import json

router = APIRouter(prefix="/api/guides", tags=["Guides"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# List with pagination
@router.get("/", summary="List guides (paginated)")
def list_guides(page: int = 1, page_size: int = 12, db: Session = Depends(get_db)):
    if page < 1:
        page = 1
    offset = (page - 1) * page_size
    items = db.query(Guide).order_by(Guide.id).offset(offset).limit(page_size).all()
    total = db.query(Guide).count()
    results = []
    for g in items:
        results.append({
            "id": g.id,
            "title": g.title,
            "category": g.category,
            "urgency": g.urgency,
            "summary": g.summary,
            "estimated_time": g.estimated_time,
        })
    return {"page": page, "page_size": page_size, "total": total, "items": results}

# Search by q (title or summary), category, urgency
@router.get("/search", summary="Search guides")
def search_guides(
    q: Optional[str] = Query(None, description="Search query"),
    category: Optional[str] = Query(None),
    urgency: Optional[str] = Query(None),
    page: int = 1,
    page_size: int = 20,
    db: Session = Depends(get_db)
):
    query = db.query(Guide)
    if q:
        likeq = f"%{q}%"
        query = query.filter((Guide.title.ilike(likeq)) | (Guide.summary.ilike(likeq)))
    if category:
        query = query.filter(Guide.category.ilike(f"%{category}%"))
    if urgency:
        query = query.filter(Guide.urgency.ilike(f"%{urgency}%"))

    total = query.count()
    offset = (page - 1) * page_size
    items = query.order_by(Guide.id).offset(offset).limit(page_size).all()

    results = []
    for g in items:
        results.append({
            "id": g.id,
            "title": g.title,
            "category": g.category,
            "urgency": g.urgency,
            "summary": g.summary,
            "estimated_time": g.estimated_time
        })

    return {"page": page, "page_size": page_size, "total": total, "items": results}

# Get guide by id (with full fields)
@router.get("/{guide_id}", summary="Get a single guide by id")
def get_guide(guide_id: int, db: Session = Depends(get_db)):
    g = db.query(Guide).filter(Guide.id == guide_id).first()
    if not g:
        raise HTTPException(status_code=404, detail="Guide not found")
    return {
        "id": g.id,
        "title": g.title,
        "category": g.category,
        "urgency": g.urgency,
        "summary": g.summary,
        "symptoms": json.loads(g.symptoms) if g.symptoms else [],
        "steps": json.loads(g.steps) if g.steps else [],
        "donts": json.loads(g.donts) if g.donts else [],
        "estimated_time": g.estimated_time
    }

# Latest (most recent N)
@router.get("/latest", summary="Latest guides")
def latest_guides(limit: int = 6, db: Session = Depends(get_db)):
    items = db.query(Guide).order_by(Guide.id.desc()).limit(limit).all()
    results = []
    for g in items:
        results.append({
            "id": g.id,
            "title": g.title,
            "category": g.category,
            "urgency": g.urgency,
            "summary": g.summary,
            "estimated_time": g.estimated_time
        })
    return results