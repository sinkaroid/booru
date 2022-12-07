import re
from typing import Union
from ..utils.fetch import request, roll
from ..utils.constant import Api, better_object, parse_image_danbooru, get_hostname
from random import shuffle

Booru = Api()


class Atfbooru(object):
    """AllTheFallen Client

    Methods
    -------
    search : function
        Search and gets images from atfbooru.

    search_image : function
        Search and gets images from atfbooru, but only returns image.

    """

    @staticmethod
    def append_object(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by atfbooru.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            if "id" in raw_object[i]:
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.atfbooru)}/posts/{raw_object[i]['id']}"

        return raw_object

    def __init__(self, api_key: str = "", user_id: str = ""):
        """Initializes atfbooru.

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

        raw_data = await request(site=Booru.atfbooru, params_x=self.specs, block=block)
        self.appended = Atfbooru.append_object(raw_data)

        try:
            if gacha:
                return better_object(roll(self.appended))
            elif random:
                shuffle(self.appended)
                return better_object(self.appended)
            else:
                return better_object(Atfbooru.append_object(self.appended))
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

        raw_data = await request(site=Booru.atfbooru, params_x=self.specs, block=block)
        self.appended = Atfbooru.append_object(raw_data)

        try:
            return better_object(parse_image_danbooru(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")
