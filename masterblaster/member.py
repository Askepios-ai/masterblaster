from datetime import datetime
from dateutil import parser

from .player import Player

from typing import Optional

__all__ = [
    "Member",
]


class Member:
    """
    Class for organization members

    :param player: The player object
    :param email: The member email
    :param name: The member name
    :param playerId: The player id
    :param role: The member role
    :param addedAt: When the member was added
    :param invitedAt: When the member was invited

    :ivar player: The member's related player object
    :ivar email: The member's email-address
    :ivar name: The member's name
    :ivar player_id: The member's player id
    :ivar role: The member's role
    :ivar added_at: When the member was added
    :ivar invited_at: When the member was invited
    """

    def __init__(
        self,
        player: dict,
        email: str,
        name: str,
        playerId: str,
        role: int,
        addedAt: str,
        invitedAt: Optional[datetime],
    ) -> None:
        self.player: Player = Player(**player)
        self.email: str = email
        self.name: str = name
        self.player_id: str = playerId
        self.role: int = role
        self.added_at: datetime = None if not addedAt else parser.isoparse(addedAt)
        self.invited_at: Optional[datetime] = (
            None if not invitedAt else parser.isoparse(invitedAt)
        )

    def __str__(self) -> str:
        return f"{self.name}"


class InternalMember:
    """
    Class for internal searchable members
    Contains different information than player objects for organization/teams
    """

    def __init__(
        self,
        id: str,
        objectId: str,
        objectType: str,
        objectName: str,
        avatarUrl: str,
        displayText: str,
        searchableProperties: dict,
    ) -> None:
        self.id: str = id
        self.object_id: str = objectId
        self.object_type: str = objectType
        self.object_name: str = objectName
        self.avatar_url: str = avatarUrl
        self.display_text: str = displayText
        self.searchable_properties: dict = searchableProperties
