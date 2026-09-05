from pydantic import BaseModel, Field, ConfigDict
from typing import Any
from datetime import datetime

class CharacterCreate(BaseModel): 
	name: str = Field(min_length=1, max_length=100)
	race: dict[str, Any] = Field(default_factory=dict)
	character_class: dict[str, Any] = Field(default_factory=dict)
	inventory: dict[str, Any] = Field(default_factory=dict)
	equipment: dict[str, Any] = Field(default_factory=dict)

	is_player: bool
	is_temporary: bool

	level: int = Field(default=1)
	armor_class: int = Field(default=10)
	max_hp: int = Field(default=10)
	current_hp: int = Field(default=10)
	temporary_hp: int = Field(default=0)

	strength: int = Field(default=10)
	dexterity: int = Field(default=10)
	constitution: int = Field(default=10)
	intelligence: int = Field(default=10)
	wisdom: int = Field(default=10)
	charisma: int = Field(default=10)

	general_condition: str = Field(default="Healthy", max_length=50)
	buffs: dict[str, Any] = Field(default_factory=dict)
	debuffs: dict[str, Any] = Field(default_factory=dict)
	active_skills: dict[str, Any] = Field(default_factory=dict)
	skills: dict[str, Any] = Field(default_factory=dict)
	spells: dict[str, Any] = Field(default_factory=dict)
	spell_slots: dict[str, Any] = Field(default_factory=dict)

class CharacterRead(CharacterCreate):
	model_config = ConfigDict(from_attributes=True)

	id: int
	owner_id: str
	created_at: datetime
	updated_at: datetime