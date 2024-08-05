from __future__ import annotations
import os
import aiohttp
from .team import Team
from .member import Member
from .image import Image

BASE = "https://app.masterblaster.gg/api"

__all__ = [
    "Organisation",
]


class Organisation:
    def __init__(
        self,
        session: aiohttp.ClientSession = None,
        id: str = None,
        name: str = None,
        members: list[dict] = None,
        images: list[dict] = None,
    ) -> None:
        self.session: aiohttp.ClientSession = session
        self.id: str = id
        self.name: str = name
        self.members: list[Member] = [Member(**member) for member in members]
        self.images: list[Image] = [Image(**image) for image in images]

    def __str__(self) -> str:
        return self.name

    async def get_members(self):
        """
        Returns members of the organization

        Parameters
        ----------
        None

        Returns
        -------
        members: list[Member]
            A list of all members in the organization
        """
        r = await self.session.get(f"{os.getenv('MB_BASE_URL')}/organization/{self.id}")
        match r.status:
            case 200:
                members = await r.json()
                return [Member(**member) for member in members["members"]]
            case _:
                raise ValueError(
                    f"Unable to fetch members: {self} code: {r.status} err: {await r.text()}"
                )

    async def get_teams(self) -> list[Team]:
        """
        Returns teams of the organization

        Parameters
        ----------
        None

        Returns
        -------
        teams: list[Team]
            A list of all teams in the organization
        """
        r = await self.session.get(
            f"{os.getenv('MB_BASE_URL')}/organization/{self.id}/teams"
        )
        match r.status:
            case 200:
                teams = await r.json()
                return [Team(self.session, **team) for team in teams]
            case _:
                raise ValueError(
                    f"Unable to fetch teams: {self} code: {r.status} err: {await r.text()}"
                )

    async def get_images(self) -> list[Image]:
        """
        Returns images of the organization

        Parameters
        ----------
        None

        Returns
        -------
        images: list[Image]
            A list of all images in the organization
        """
        r = await self.session.get(f"{os.getenv('MB_BASE_URL')}/organization/{self.id}")
        match r.status:
            case 200:
                images = await r.json()
                return [Image(**image) for image in images["images"]]
            case _:
                raise ValueError(
                    f"Unable to fetch images: {self} code: {r.status} err: {await r.text()}"
                )
