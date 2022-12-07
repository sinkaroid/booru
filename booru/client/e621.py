import aiohttp
from typing import Union
from ..utils.fetch import request, roll
from ..utils.constant import Api, better_object, parse_image, get_hostname
from random import shuffle

Booru = Api()


class E621(object):
    """E621 Client

    Methods
    -------
    search : function
        Search and gets images from e621.

    search_image : function
        Gets images, meant just image urls from e621.

    """

    @staticmethod
    def append_object(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by e621.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            if "id" in raw_object[i]:
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.e621)}/posts/{raw_object[i]['id']}"

        return raw_object

    def __init__(self, api_key: str = "", user_id: str = ""):
        """Initializes e621.

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

        """Search and gets images from e621.

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
            The json object returned by e621.
        """
        if gacha:
            limit = 100
        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)
        else:
            self.query = query

        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["page"] = page

        raw_data = await request(site=Booru.e621, params_x=self.specs, block="")
        self.appended = E621.append_object(raw_data["posts"])
        
        try:
            if gacha:
                return better_object(roll(self.appended))
            elif random:
                shuffle(self.appended)
                return better_object(self.appended)
            else:
                return better_object(E621.append_object(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")

    async def search_image(
        self, query: str, limit: int = 100, page: int = 1
    ) -> Union[aiohttp.ClientResponse, str]:

        """Gets images, meant just image urls from e621.

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
        list
            The list of image urls.

        """

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)


        self.query = query
        self.specs["tags"] = self.query
        self.specs["limit"] = limit
        self.specs["pid"] = page
        self.specs["json"] = "1"

        raw_data = await request(site=Booru.e621, params_x=self.specs, block="")
        self.appended = E621.append_object(raw_data["posts"])

        try:
            return better_object(parse_image(self.appended))
        except Exception as e:
            raise Exception(f"Failed to get data: {e}")
