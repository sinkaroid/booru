import requests
import json
import re
from ..utils.parser import Api, better_object, parse_image, get_hostname, deserialize
from random import shuffle, randint

Booru = Api()


class Derpibooru(object):
    """derpibooru wrapper

    Methods
    -------
    search : function
        Search and gets images from derpibooru.

    get_image : function
        Gets images, image urls only from derpibooru.

    """

    @staticmethod
    def append_obj(raw_object: dict):
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
    ):

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
        if gacha:
            limit = 100

        if limit > 100:
            raise ValueError(Booru.error_handling_limit)

        else:
            self.query = query

        self.specs["q"] = str(self.query)
        self.specs["per_page"] = str(limit)
        self.specs["page"] = str(page)

        self.data = requests.get(Booru.derpibooru, params=self.specs)
        self.final = self.final = deserialize(self.data.json())

        if not self.final["images"]:
            raise ValueError(Booru.error_handling_null)

        self.not_random = Derpibooru.append_obj(self.final["images"])
        shuffle(self.not_random)

        try:
            if gacha:
                return better_object(self.not_random[randint(0, len(self.not_random))])

            elif random:
                return better_object(self.not_random)

            else:
                return better_object(Derpibooru.append_obj(self.final["images"]))

        except Exception as e:
            raise ValueError(f"Failed to get data: {e}")

    async def get_image(self, query: str, limit: int = 100, page: int = 1):

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

        if limit > 100:
            raise ValueError(Booru.error_handling_limit)

        else:
            self.query = query

        self.specs["q"] = str(self.query)
        self.specs["per_page"] = str(limit)
        self.specs["page"] = str(page)

        try:
            self.data = requests.get(Booru.derpibooru, params=self.specs)
            self.final = self.final = deserialize(self.data.json())

            self.not_random = [
                i["representations"]["full"] for i in self.final["images"]
            ]
            shuffle(self.not_random)
            return better_object(self.not_random)

        except:
            raise ValueError(f"Failed to get data")
