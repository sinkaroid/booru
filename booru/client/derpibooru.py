import aiohttp
from typing import Union
from ..utils.fetch import request, roll
from ..utils.constant import Api, better_object, parse_image, get_hostname
from random import shuffle, randint

Booru = Api()


class Derpibooru(object):
    """derpibooru wrapper

    Methods
    -------
    search : function
        Search and gets images from derpibooru.

    search_image : function
        Gets images, image urls only from derpibooru.

    """

    @staticmethod
    def append_object(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by derpibooru.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            if "id" in raw_object[i]:
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.derpibooru)}/images/{raw_object[i]['id']}"

        return raw_object

    def __init__(self, key: str = ""):
        """Initializes derpibooru.

        Parameters
        ----------
        key : str
            An optional authentication token. If omitted, no user will be authenticated.
        """

        if key:
            self.key = None
        else:
            self.key = key

        self.specs = {"key": self.key}

    async def search(
        self,
        query: str,
        limit: int = 100,
        page: int = 1,
        random: bool = True,
        gacha: bool = False,
    ) -> Union[aiohttp.ClientResponse, str]:

        """Search and gets images from derpibooru.

        Parameters
        ----------
        query : str
            The query to search for.


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
            The json object returned by derpibooru.
        """
        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        self.query = query
        self.specs["q"] = self.query
        self.specs["per_page"] = limit
        self.specs["page"] = page

        raw_data = await request(site=Booru.derpibooru, params_x=self.specs, block="")
        self.appended = Derpibooru.append_object(raw_data["images"])
        
        try:
            if gacha:
                return better_object(roll(self.appended))
            elif random:
                shuffle(self.appended)
                return better_object(self.appended)
            else:
                return better_object(Derpibooru.append_object(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")

    async def search_image(self, query: str, limit: int = 100, page: int = 1) -> Union[aiohttp.ClientResponse, str]:

        """Gets images, meant just image urls from derpibooru.

        Parameters
        ----------
        query : str
            The query to search for.

        limit : int
            The limit of images to return.

        page : int
            The number of desired page

        Returns
        -------
        dict
            The json object returned by derpibooru.

        """

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        self.query = query
        self.specs["q"] = self.query
        self.specs["per_page"] = limit
        self.specs["page"] = page

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(Booru.derpibooru, params=self.specs) as resp:
                    self.data = await resp.json(content_type=None)
                    self.final = self.data

                    self.not_random = [
                        i["representations"]["full"] for i in self.final["images"]
                    ]
                    shuffle(self.not_random)
                    return better_object(self.not_random)

        except Exception as e:
            raise Exception(f"Failed to get data: {e}")
