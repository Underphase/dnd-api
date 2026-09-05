from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from src.core.db.models.character import Character
from src.schemas.characterSchema import CharacterCreate

class CharacterRepository:
	def __init__(self, db: AsyncSession):
		self.db = db

	async def create_character(
			self,
			owner_id: str,
			data: CharacterCreate,
	) -> Character:
		character = Character(
			owner_id=owner_id,
			**data.model_dump()
			)

		self.db.add(character)
		await self.db.flush()
		await self.db.refresh(character)

		return character

	async def count_characters(
			self,
	):
		stmt = select(func.count()).select_from(Character)
		result = await self.db.execute(stmt)
		total = result.scalar_one_or_none()
		return total
	