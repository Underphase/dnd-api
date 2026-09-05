from src.repositories.characterRepository import CharacterRepository
from src.schemas.characterSchema import CharacterCreate

class CharacterService:
	def __init__(self, repo: CharacterRepository):
		self.repo = repo

	async def create_character(self, data: CharacterCreate):
		if not data.race:
			data.race = {"name": "human"}
		if data.level < 1:
			data.level = 1
		if data.max_hp and not data.current_hp:
			data.current_hp = data.max_hp
		if data.max_hp < 1:
			data.max_hp = 10
		if data.armor_class < 1:
			data.armor_class = 10

		count = await self.repo.count_characters()
		owner_id = f'c{count}'

		character = await self.repo.create_character(owner_id=owner_id, data=data)
		return character
		