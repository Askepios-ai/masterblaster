import pytest
import aiohttp
import os
from dotenv import load_dotenv, find_dotenv
from masterblaster.organisation import Organisation
from masterblaster.member import Member
from masterblaster.headers import Header

masterblaster_organisation = {
    "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "name": "name",
    "members": [
        {
            "player": {
                "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                "nickName": "name",
                "avatarUrl": "",
                "registered": "2000-01-01T00:00:00.00+00:00",
                "isProfileComplete": True,
                "gameAccounts": [
                    {
                        "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "nick": "name",
                        "avatarUrl": "",
                        "gameId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                        "isConnected": True,
                        "connectedAt": "2000-01-01T00:00:00.00+00:00",
                    }
                ],
            },
            "email": "email@email.com",
            "name": "name",
            "playerId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "role": 10,
            "addedAt": "2000-01-01T00:00:00.00+00:00",
            "invitedAt": None,
        },
    ],
    "images": [],
}


@pytest.fixture(autouse=True)
def load_env():
    load_dotenv(find_dotenv(".env.test"))


def test_init():
    org = Organisation(**masterblaster_organisation)
    assert org.id == masterblaster_organisation["id"]
    assert org.name == masterblaster_organisation["name"]
    expected = [Member(**member) for member in masterblaster_organisation["members"]]
    for member in org.members:
        assert member.name == expected.pop(0).name


def test_str():
    org = Organisation(**masterblaster_organisation)
    assert str(org) == masterblaster_organisation["name"]


@pytest.mark.asyncio
async def test_get_members():
    header = (
        Header()
        .add("Authorization", f"Bearer {os.getenv('ACCESS_TOKEN')}")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    masterblaster_organisation["id"] = os.getenv("ORG_ID")
    org = Organisation(**masterblaster_organisation)
    org.session = aiohttp.ClientSession(headers=header)
    expected = [Member(**member) for member in masterblaster_organisation["members"]]
    assert len([member.name for member in await org.get_members()]) == len(expected)
    await org.session.close()


@pytest.mark.asyncio
async def test_get_members_fail():
    header = (
        Header()
        .add("Authorization", "Bearer NOT-A-TOKEN")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    org = Organisation(**masterblaster_organisation)
    org.session = aiohttp.ClientSession(headers=header)
    org.id = "fail"
    with pytest.raises(ValueError):
        await org.get_members()
    await org.session.close()


@pytest.mark.asyncio
async def test_get_teams():
    header = (
        Header()
        .add("Authorization", f"Bearer {os.getenv('ACCESS_TOKEN')}")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    org = Organisation(**masterblaster_organisation)
    org.session = aiohttp.ClientSession(headers=header)
    teams = await org.get_teams()
    assert len(teams) == 1
    assert teams[0].name == os.getenv("TEAM_NAME")
    await org.session.close()


@pytest.mark.asyncio
async def test_get_images():
    expected = masterblaster_organisation["images"]
    header = (
        Header()
        .add("Authorization", f"Bearer {os.getenv('ACCESS_TOKEN')}")
        .add("User-Agent", "MasterBlaster-python")
        .add("Accept", "application/json")
        .add("Content-Type", "application/json")
        .add("Connection", "keep-alive")
    )
    org = Organisation(**masterblaster_organisation)
    org.session = aiohttp.ClientSession(headers=header)
    assert len([image.id for image in await org.get_images()]) == len(
        [image["imageId"] for image in expected]
    )
    assert [image.original_id for image in await org.get_images()] == [
        image["originalImageId"] for image in expected
    ]
    await org.session.close()
