from __future__ import annotations
import os
import aiohttp
from typing import Optional
from datetime import datetime
from .player import Player
from .schedule import Schedule

BASE = "https://app.masterblaster.gg/api"


class Team:
    def __init__(
        self,
        session: aiohttp.ClientSession = None,
        id: Optional[str] = None,
        ownerPlayerId: str = None,
        organizationOwnerId: str = None,
        name: Optional[str] = None,
        tag: Optional[str] = None,
        flag: Optional[str] = None,
        shortHandle: Optional[str] = None,
        avatarImageId: str = None,
        bannerImageId: Optional[str] = None,
        socialLinks: list = None,
        gameId: str = None,
        players: list[dict] = None,  # Some weird metadata together with Player objects
        createdAt: Optional[datetime] = None,
    ) -> None:
        self.session: aiohttp.ClientSession = session
        self.id: Optional[str] = id
        self.owner_player_id: str = ownerPlayerId
        self.organization_owner_id: str = organizationOwnerId
        self.name: Optional[str] = name
        self.tag: Optional[str] = tag
        self.flag: Optional[str] = flag
        self.short_handle: Optional[str] = shortHandle
        self.avatar_image_id: str = avatarImageId
        self.banner_image_id: Optional[str] = bannerImageId
        self.social_links: list = socialLinks
        self.game_id: str = gameId
        self.players: list[Player] = [Player(**player["player"]) for player in players]
        self.created_at: Optional[datetime] = createdAt

    def __str__(self) -> str:
        return self.name

    async def get_schedule(self) -> Schedule:
        """
        Returns the schedule for the team

        Parameters
        ----------
        None

        Returns
        -------
        Schedule
        """
        r = await self.session.get(
            f"{os.getenv('MB_BASE_URL')}/match_schedule/player?includeFinished=false"
        )
        match r.status:
            case 200:
                schedule = await r.json()
                matches = []
                for match in schedule:
                    for team in match["teams"]:
                        if team["team"]["id"] == self.id:
                            matches.append(match)
                return Schedule(matches)
            case _:
                raise ValueError(
                    f"Unable to fetch schedule for: {self} code: {r.status} err: {await r.text()}"
                )
