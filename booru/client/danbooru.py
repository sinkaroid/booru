import re
import aiohttp
from typing import Union
from ..utils.parser import Api, better_object, parse_image_danbooru, get_hostname
from random import shuffle, randint

Booru = Api()


class Danbooru(object):
    """Danbooru Client

    Methods
    -------
    search : function
        Search and gets images from danbooru.

    search_image : function
        Gets images, image urls only from danbooru.

    """

    @staticmethod
    def append_object(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by danbooru.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            if "id" in raw_object[i]:
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.danbooru)}/posts/{raw_object[i]['id']}"

        return raw_object

    def __init__(self, api_key: str = "", login: str = ""):
        """Initializes danbooru.

        Parameters
        ----------
        api_key : str
            Your API Key which is accessible within your account options page

        login : str
            Your user ID, which is accessible on the account options/profile page.
        """

        if api_key =="" and login == "":
            self.api_key = None
            self.login = None
            self.specs = {}
        else:
            self.api_key = api_key
            self.login = login
            self.specs = {"api_key": self.api_key, "login": self.login}

        

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
            async with session.get(Booru.danbooru, params=self.specs) as resp:
                self.data = await resp.json(content_type=None)
                self.final = self.data

                for i in range(len(self.final)):
                    self.final[i]["tag_string"] = self.final[i]["tag_string"].split(" ")

                self.final = [i for i in self.final if not any(j in block for j in i["tag_string"])]

                if not self.final:
                    raise ValueError(Booru.error_handling_null)

                self.not_random = Danbooru.append_object(self.final)
                shuffle(self.not_random)

                try:
                    if gacha:
                        return better_object(self.not_random[randint(0, len(self.not_random))])

                    elif random:
                        return better_object(self.not_random)

                    else:
                        return better_object(Danbooru.append_object(self.final))

                except Exception as e:
                    raise ValueError(f"Failed to get data: {e}")

    async def search_image(
        self, query: str, block: str = "", limit: int = 100, page: int = 1
    ) -> Union[list, dict]:

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

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        self.query = query
        self.specs["tags"] = str(self.query)
        self.specs["limit"] = str(limit)
        self.specs["page"] = str(page)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(Booru.danbooru, params=self.specs) as resp:
                    self.data = await resp.json(content_type=None)
            
                    self.final = self.data
                    
                    for i in range(len(self.final)):
                        self.final[i]["tag_string"] = self.final[i]["tag_string"].split(" ")

                    self.final = [i for i in self.final if not any(j in block for j in i["tag_string"])]

                    self.not_random = parse_image_danbooru(self.final)
                    shuffle(self.not_random)
                    return better_object(self.not_random)

        except Exception as e:
            raise ValueError(f"Failed to get data: {e}")
