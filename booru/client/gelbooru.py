import re
from typing import Union
from ..utils.fetch import request, request_wildcard, roll
from ..utils.constant import Api, better_object, parse_image, get_hostname
from random import shuffle

Booru = Api()


class Gelbooru(object):
    """Gelbooru Client

    Methods
    -------
    search : function
        Search and gets images from gelbooru.

    search_image : function
        Search and gets images from gelbooru, but only returns image.

    find_tags : function
        Get the proper tags from gelbooru.

    """

    @staticmethod
    def append_object(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by gelbooru.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            if "id" in raw_object[i]:
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.gelbooru)}/index.php?page=post&s=view&id={raw_object[i]['id']}"

        return raw_object

    def __init__(self, api_key: str = "", user_id: str = ""):
        """Initializes gelbooru.

        Parameters
        ----------
        api_key : str
            Your API Key (If possible)

        user_id : str
            Your user ID (If possible)
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

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        self.query = query
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["pid"] = page
        self.specs["json"] = "1"

        raw_data = await request(site=Booru.gelbooru, params_x=self.specs, block=block)
        self.appended = Gelbooru.append_object(raw_data)

        try:
            if gacha:
                return better_object(roll(self.appended))
            elif random:
                shuffle(self.appended)
                return better_object(self.appended)
            else:
                return better_object(Gelbooru.append_object(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")

    async def search_image(
        self, query: str, block: str = "", limit: int = 100, page: int = 1
    ) -> Union[list, str, None]:

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
        self.specs["pid"] = page
        self.specs["json"] = "1"

        raw_data = await request(site=Booru.gelbooru, params_x=self.specs, block=block)
        self.appended = Gelbooru.append_object(raw_data)

        try:
            return better_object(parse_image(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")

    async def find_tags(self, query: str) -> Union[list, str, None]:
        """Find tags

        Parameters
        ----------
        query : str
            The tag to search for.

        Returns
        -------
        list
            The list of tags (as string, you may need booru.resolve())
        """
        try:
            data = await request_wildcard(site=Booru.gelbooru_wildcard, query=query)
            return better_object(data)

        except Exception as e:
            raise Exception(f"Failed to get data: {e}")
