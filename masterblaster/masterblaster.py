import os
import aiohttp
import logging
from .headers import Header
from .organisation import Organisation
from .member import Member
from .team import Team
from typing import Any, Optional


__all__ = [
    "MasterBlaster",
]


class MasterBlaster:
    """
    MasterBlaster is the main class for interacting with the MasterBlaster API

    :param access_token: The access token for the organization

    :ivar access_token: The access token for the organization
    :ivar headers: The headers used for the session

    """

    def __init__(self, access_token: Optional[str]) -> None:
        self.access_token: Optional[str] = access_token
        self.headers: Header = Header()
        self._session: aiohttp.ClientSession | None = None
        self.logger = logging.getLogger(__name__)

    async def __aenter__(self) -> "MasterBlaster":
        """
        :meta private:
        """
        await self._setup()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        """
        :meta private:
        """
        await self._session.close()

    async def teardown(self) -> None:
        """
        Close the session

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        await self._session.close()
        self._session = None

    @classmethod
    async def create(cls, access_token: str) -> "MasterBlaster":
        """
        Create a new fully setup MasterBlaster instance

        Parameters
        ----------
        access_token : str
            The access token for the organization
        org_name : str
            The name of the organization

        Returns
        -------
        MasterBlaster
        """
        self = cls(access_token)
        await self._setup()
        return self

    async def _setup(self) -> "MasterBlaster":
        """
        :meta private:
        """
        if self._session and not self._session.closed:
            await self._session.close()
        assert self.access_token is not None, "Missing Masterblaster access token"
        self.headers = (
            Header()
            .add("Authorization", f"Bearer {self.access_token}")
            .add("User-Agent", "MasterBlaster-python")
            .add("Accept", "application/json")
            .add("Content-Type", "application/json")
            .add("Connection", "keep-alive")
        )
        self._session = aiohttp.ClientSession(headers=self.headers)
        return self

    async def set_access_token(self, access_token: str) -> None:
        """
        Set the access token for the organization
        Will update the session

        Parameters
        ----------
        access_token : str
            The access token for the organization

        Returns
        -------
        None
        """
        self.access_token = access_token
        await self._setup()

    async def get_org(self, org_id: str) -> Organisation:
        """
        Returns the organization for the given organization id

        Parameters
        ----------
        org_id (str): The organization id

        Returns
        -------
        Organisation
        """
        r = await self._session.get(f"{os.getenv('MB_BASE_URL')}/organization/{org_id}")
        match r.status:
            case 200:
                return Organisation(self._session, **await r.json())
            case _:
                raise ValueError(
                    f"Unable to fetch organization: {org_id} code: {r.status} err: {await r.text()}"
                )

    async def get_org_by_name(self, org_name: str) -> Organisation:
        """
        Returns the organization for the given organization name
        Users can be associated with multiple organizations with the same name, so this function will return the first one
        Parameters
        ----------
        org_name (str): The organization name

        Returns
        -------
        Organisation
        """
        orgs = await self.get_all_orgs()
        for org in orgs:
            if org.name == org_name:
                return org
        raise ValueError(f"Unable to find organization: {org_name}")

    async def get_all_orgs(self) -> list[Organisation]:
        """
        Get all organizations for the current access token

        Parameters
        ----------
        None

        Returns
        -------
        organisations: List[Organisation]
        """
        r = await self._session.get(f"{os.getenv('MB_BASE_URL')}/organization/player")
        match r.status:
            case 200:
                orgs = await r.json()
                orgs = [await self.get_org(org["id"]) for org in orgs]
                return orgs
            case _:
                raise Exception(
                    f"Unable to fetch organizations. code: {r.status} err: {await r.text()}"
                )

    async def search_org(self, org_name: str) -> Organisation:
        """
        Search for an organization by name

        Parameters
        ----------
        org_name (str): The name of the organization

        Returns
        -------
        Organisation: Organisation
        """
        r = await self._session.get(
            f"{os.getenv('MB_BASE_URL')}/search2/search?objectType=organization&query={org_name}"
        )
        match r.status:
            case 200:
                # MB enforces unique names, no chance of multiple pages here
                r = await r.json()
                try:
                    await self.get_org(r["data"][0]["id"])
                except Exception:
                    raise LookupError(f"Unable to find organization: {org_name}")
            case _:
                raise Exception(
                    f"Unable to fetch organizations. code: {r.status} err: {await r.text()}"
                )

    async def search_team(self, team_name: str) -> Team:
        """
        Search for a team by name

        Parameters
        ----------
        team_name (str): The name of the team

        Returns
        -------
        Organisation: Organisation
        """

        async def get_team(self, team_id: int) -> Team | None:
            r = await self._session.get(f"{os.getenv('MB_BASE_URL')}/Team/{team_id}")
            match r.status:
                case 200:
                    return Team(self._session, **await r.json())
                case _:
                    raise Exception(
                        f"Unable to fetch team: {team_id} code: {r.status} err: {await r.text()}"
                    )

        r = await self._session.get(
            f"{os.getenv('MB_BASE_URL')}/search2/search?objectType=team&query={team_name}"
        )
        match r.status:
            case 200:
                # MB enforces unique names, no chance of multiple pages here
                r = await r.json()
                try:
                    return await get_team(self, r["data"][0]["id"])
                except Exception:
                    raise

            case _:
                raise Exception(
                    f"Unable to fetch teams. code: {r.status} err: {await r.text()}"
                )

    async def search_player(self, player_name: str) -> list[InternalMember]:
        """
        Search for a player by name

        Parameters
        ----------
        player_name (str):
            The name of the player

        Returns
        -------
        Member: list[Member]
            List of members with given name
        """
        r = await self._session.get(
            f"{os.getenv('MB_BASE_URL')}/search2/search?objectType=player&query={player_name}"
        )
        match r.status:
            case 200:
                # MB enforces unique names, no chance of multiple pages here
                r = await r.json()
                try:
                    return await get_player(self, r["data"][0]["id"])
                except Exception:
                    raise

            case _:
                raise Exception(
                    f"Unable to fetch players. code: {r.status} err: {await r.text()}"
                )
