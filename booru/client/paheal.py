import json
import re
import aiohttp
from typing import Union
from ..utils.constant import Api, better_object
from random import shuffle, randint
from xmltodict import parse

Booru = Api()


class Paheal(object):
    """Paheal Client

    Methods
    -------
    search : function
        Search and gets images from paheal.

    search_image : function
        Search and gets images from paheal, but only returns image.

    """

    def __init__(self, api_key: str = "", user_id: str = ""):
        """Initializes paheal.

        Parameters
        ----------
        api_key : str
            Your API Key which is accessible within your account options page

        user_id : str
            Your user ID, which is accessible on the account options/profile page.
        """

        if api_key and user_id == "":
            self.api_key = None
            self.user_id = None
        else:
            self.api_key = api_key
            self.user_id = user_id

        self.specs = {"api_key": self.api_key, "user_id": self.user_id}

    async def search(
        self,
        query: str,
        limit: int = 100,
        page: int = 1,
        random: bool = True,
        gacha: bool = False,
    ) -> Union[aiohttp.ClientResponse, str]:

        """Search and gets images from paheal.

        Parameters
        ----------
        query : str
            The tags to search for.

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
            The json object returned by paheal.
        """
        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        self.tags = query
        self.specs["tags"] = self.tags
        self.specs["limit"] = limit
        self.specs["page"] = page

        async with aiohttp.ClientSession() as session:
            async with session.get(Booru.paheal, params=self.specs) as resp:
                self.data = await resp.text()
                data_dict = parse(self.data)
                unsolved = json.dumps(data_dict)
                self.final = json.loads(unsolved)

                if "tag" not in self.final["posts"]:
                    raise ValueError(Booru.error_handling_null)

                self.not_random = self.final["posts"]["tag"]
                shuffle(self.not_random)

                try:
                    if gacha:
                        return better_object(
                            self.final["posts"]["tag"][
                                randint(0, len(self.final["posts"]["tag"]))
                            ]
                        )
                    elif random:
                        return better_object(self.final["posts"]["tag"])
                    else:
                        return better_object(self.not_random)

                except Exception as e:
                    raise Exception(f"Failed to get data: {e}")

    async def search_image(
        self, query: str, limit: int = 100, page: int = 1
    ) -> Union[aiohttp.ClientResponse, str]:

        """Gets images, meant just image urls from paheal.

        Parameters
        ----------
        query : str
            The tags to search for.

        limit : int
            The limit of images to return.

        page : int
            The number of desired page

        Returns
        -------
        list
            The list of image urls.

        """

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        self.tags = query
        self.specs["tags"] = self.tags
        self.specs["limit"] = limit
        self.specs["page"] = page

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(Booru.paheal, params=self.specs) as resp:
                    self.data = await resp.text()
                    data_dict = parse(self.data)
                    unsolved = json.dumps(data_dict)
                    self.final = json.loads(unsolved)

                    abc_kontol = self.final["posts"]["tag"]
                    ## extract all image urls
                    self.image_urls = []
                    for i in abc_kontol:  # paheal emang ngentot
                        self.image_urls.append(i["@file_url"])

                    shuffle(self.image_urls)
                    return better_object(self.image_urls)

        except Exception as e:
            raise Exception(f"Failed to get data: {e}")
