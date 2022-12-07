import re
import aiohttp
from typing import Union
from ..utils.fetch import request, roll
from ..utils.constant import Api, better_object, parse_image, get_hostname
from random import shuffle, randint

Booru = Api()

# these referer request just help you out to interacts with the API, not for displaying images


class Behoimi(object):
    """3d booru / Behoimi wrapper

    Methods
    -------
    search : function
        Search and gets images from behoimi.

    search_image : function
        Gets images, image urls only from behoimi.

    """

    @staticmethod
    async def mock(site: str, params: dict):
        async with aiohttp.ClientSession(headers=Booru.behoimi_bypass) as session:
            async with session.get(site, params=params) as resp:
                return await resp.json()

    @staticmethod
    def append_object(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by behoimi.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            if "id" in raw_object[i]:
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.behoimi)}/post/show/{raw_object[i]['id']}"

        return raw_object

    def __init__(self):
        self.specs = {}

    async def search(
        self,
        query: str,
        block: str = "",
        limit: int = 100,
        page: int = 1,
        random: bool = True,
        gacha: bool = False,
    ) -> Union[aiohttp.ClientResponse, str]:

        """Search and gets images from behoimi.

        Parameters
        ----------
        query : str
            The query to search for.

        block : str
            The tags to block.

        limit : int
            The limit of images to return.

        page : int
            The number of desired page

        random : bool
            Shuffle the whole dict, default is True.

        gacha : bool
            Get random single object, limit property will be ignored.

        Returns
        -------
        dict
            The json object returned by behoimi.
        """
        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        self.query = query
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["page"] = page

        raw_data = await request(site=Booru.behoimi, params_x=self.specs, block=block)
        self.appended = Behoimi.append_object(raw_data)
        
        try:
            if gacha:
                return better_object(roll(self.appended))
            elif random:
                shuffle(self.appended)
                return better_object(self.appended)
            else:
                return better_object(Behoimi.append_object(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")

    async def search_image(
        self, query: str, block="", limit: int = 100, page: int = 1
    ) -> Union[aiohttp.ClientResponse, str]:

        """Gets images, meant just image urls from behoimi.

        Parameters
        ----------
        query : str
            The query to search for.

        block : str
            The tags to block.

        limit : int
            The limit of images to return.

        page : int
            The number of desired page

        Returns
        -------
        dict
            The json object returned by behoimi.

        """

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        self.query = query
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["page"] = page

        raw_data = await request(site=Booru.behoimi, params_x=self.specs, block=block)
        self.appended = Behoimi.append_object(raw_data)

        try:
            return better_object(parse_image(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")
