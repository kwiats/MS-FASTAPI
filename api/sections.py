from fastapi import APIRouter

router = APIRouter()


@router.get("/sections")
async def read_section():
    return {"courses": []}


@router.get("/sections/{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


@router.get("/content_blocks/{id}")
async def read_content_blocks(id: int):
    return {"courses": []}
