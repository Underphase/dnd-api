from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.dependencies import get_db
from src.repositories.characterRepository import CharacterRepository
from src.services.characterService import CharacterService


def get_character_service(db: AsyncSession = Depends(get_db)) -> CharacterService:
    repo = CharacterRepository(db)
    return CharacterService(repo)