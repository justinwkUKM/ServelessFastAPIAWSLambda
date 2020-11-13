from fastapi import APIRouter

from .endpoints import items

router = APIRouter()
router.include_router(items.router, prefix="/items", tags=["Items"])