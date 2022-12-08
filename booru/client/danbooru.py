import re
from typing import Union
from ..utils.fetch import request, request_wildcard, roll
from ..utils.constant import Api, better_object, parse_image_danbooru, get_hostname
from random import shuffle

Booru = Api()


class Danbooru(object):
    """Danbooru Client

    Methods
    -------
    search : function
        Search and gets images from danbooru.

    search_image : function
        Search and gets images from danbooru, but only returns image.

    find_tags : function
        Get the proper tags from danbooru.

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

        if api_key == "" and login == "":
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
    ) -> Union[list, str, None]:

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

        raw_data = await request(site=Booru.danbooru, params_x=self.specs, block=block)
        self.appended = Danbooru.append_object(raw_data)

        try:
            if gacha:
                return better_object(roll(self.appended))
            elif random:
                shuffle(self.appended)
                return better_object(self.appended)
            else:
                return better_object(Danbooru.append_object(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")

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
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["page"] = page

        raw_data = await request(site=Booru.danbooru, params_x=self.specs, block=block)
        self.appended = Danbooru.append_object(raw_data)

        try:
            return better_object(parse_image_danbooru(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")

    async def find_tags(site: str, query: str) -> Union[list, str, None]:
        """Find tags

        Parameters
        ----------
        site : str
            The site to search for.
        query : str
            The tag to search for.

        Returns
        -------
        list
            The list of tags.
        """
        try:
            data = await request_wildcard(site=Booru.danbooru_wildcard, query=query)
            return better_object(data)

        except Exception as e:
            raise Exception(f"Failed to get data: {e}")

