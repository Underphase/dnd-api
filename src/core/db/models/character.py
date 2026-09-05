from datetime import datetime
from typing import TypeAlias

from sqlalchemy import Boolean, DateTime, Integer, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from src.core.db.base import Base

JSONValue: TypeAlias = (
	str
	| int
	| float
	| bool
	| None
	| list["JSONValue"]
	| dict[str, "JSONValue"]
)


class Character(Base):
	__tablename__ = "character"

	id: Mapped[int] = mapped_column(primary_key=True)
	owner_id: Mapped[str] = mapped_column(String(64), index=True)
	name: Mapped[str] = mapped_column(String(100))

	race: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)
	character_class: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)
	inventory: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)
	equipment: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)

	is_player: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
	is_temporary: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

	level: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
	armor_class: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
	max_hp: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
	current_hp: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
	temporary_hp: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

	strength: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
	dexterity: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
	constitution: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
	intelligence: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
	wisdom: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
	charisma: Mapped[int] = mapped_column(Integer, default=10, nullable=False)

	general_condition: Mapped[str] = mapped_column(String(50), default="Healthy", nullable=False)
	buffs: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)
	debuffs: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)

	active_skills: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)
	skills: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)
	spells: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)
	spell_slots: Mapped[dict[str, JSONValue]] = mapped_column(JSONB, default=dict, nullable=False)

	created_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), nullable=False
	)
	updated_at: Mapped[datetime] = mapped_column(
		DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
	)
