import re
import aiohttp
from typing import Union
from ..utils.parser import Api, better_object, parse_image, get_hostname
from random import shuffle, randint

Booru = Api()


class Yandere(object):
    """Yandere Client

    Methods
    -------
    search : function
        Search and gets images from yandere.

    search_image : function
        Gets images, image urls only from yandere.

    """

    @staticmethod
    def append_object(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by yandere.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            if "id" in raw_object[i]:
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.yandere)}/post/show/{raw_object[i]['id']}"

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

        """Search method

        Parameters
        ----------
        query : str
            The query to search for.
        block : str
            The tags you want to block, separated by space.
        limit : int
            Expected number which is from pages
        page : int
            Expected number of page.
        random : bool
            Shuffle the whole dict, default is True.
        gacha : bool
            Get random single object, limit property will be ignored.

        Returns
        -------
        dict
            The json object (as string, you may need booru.resolve())
        """
        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        elif block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        self.query = query
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["page"] = page

        async with aiohttp.ClientSession() as session:
            async with session.get(Booru.yandere, params=self.specs) as resp:
                self.data = await resp.json()
                if not self.data:
                    raise ValueError(Booru.error_handling_null)

                self.final = self.data
                for i in range(len(self.final)):
                    self.final[i]["tags"] = self.final[i]["tags"].split(" ")

                self.final = [
                    i for i in self.final if not any(j in block for j in i["tags"])
                ]

                self.not_random = Yandere.append_object(self.final)
                shuffle(self.not_random)

                try:
                    if gacha:
                        return better_object(
                            self.not_random[randint(0, len(self.not_random))]
                        )
                    elif random:
                        return better_object(self.not_random)
                    else:
                        return better_object(Yandere.append_object(self.final))

                except Exception as e:
                    raise Exception(f"Failed to get data: {e}")
                    
    async def search_image(self, query: str, block: str = "", limit: int = 100, page: int = 1):

        """Parses image only

        Parameters
        ----------
        query : str
            The query to search for.
        block : str
            The tags you want to block, separated by space.
        limit : int
            Expected number which is from pages
        page : int
            Expected number of page.

        Returns
        -------
        dict
            The json object (as string, you may need booru.resolve())

        """
        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        elif block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        self.query = query
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["page"] = page

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(Booru.yandere, params=self.specs) as resp:
                    self.data = await resp.json()
                    self.final = self.data
                    for i in range(len(self.final)):
                        self.final[i]["tags"] = self.final[i]["tags"].split(" ")

                    self.final = [i for i in self.final if not any(j in block for j in i["tags"])]

                    self.not_random = parse_image(self.final)
                    shuffle(self.not_random)
                    return better_object(self.not_random)

        except Exception as e:
            raise Exception(f"Failed to get data: {e}")
