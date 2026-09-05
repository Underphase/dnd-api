from fastapi import APIRouter, Depends, HTTPException

from src.api.dependencies import get_character_service
from src.schemas.characterSchema import CharacterRead, CharacterCreate
from src.services.characterService import CharacterService

router = APIRouter(prefix='/characters', tags=["characters"])

@router.post("/", response_model=CharacterRead, status_code=201)
async def create_character(
	data: CharacterCreate,
	service: CharacterService = Depends(get_character_service)
):
	character = await service.create_character(data)
	return character