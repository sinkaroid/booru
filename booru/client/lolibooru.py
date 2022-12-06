import requests
import json
import re
from ..utils.parser import Api, better_object, parse_image, get_hostname, deserialize
from random import shuffle, randint


Booru = Api()


class Lolibooru(object):
    """lolibooru wrapper

    Methods
    -------
    search : function
        Search and gets images from lolibooru.

    get_image : function
        Gets images, image urls only from lolibooru.

    """

    @staticmethod
    def append_obj(raw_object: dict):
        """Extends new object to the raw dict

        Parameters
        ----------
        raw_object : dict
            The raw object returned by lolibooru.

        Returns
        -------
        str
            The new value of the raw object
        """
        for i in range(len(raw_object)):
            if "id" in raw_object[i]:
                raw_object[i][
                    "post_url"
                ] = f"{get_hostname(Booru.lolibooru)}/post/show/{raw_object[i]['id']}"

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
    ):

        """Search and gets images from lolibooru.

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
            The json object returned by lolibooru.
        """
        if gacha:
            limit = 100

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        else:
            self.query = query

        self.specs["tags"] = str(self.query)
        self.specs["limit"] = str(limit)
        self.specs["page"] = str(page)

        self.data = requests.get(Booru.lolibooru, params=self.specs)
        self.final = self.final = deserialize(self.data.json())

        for i in range(len(self.final)):
            self.final[i]["tags"] = self.final[i]["tags"].split(" ")

        self.final = [i for i in self.final if not any(j in block for j in i["tags"])]

        if not self.final:
            raise ValueError(Booru.error_handling_null)

        self.not_random = Lolibooru.append_obj(self.final)
        shuffle(self.not_random)

        try:
            if gacha:
                return better_object(self.not_random[randint(0, len(self.not_random))])

            elif random:
                return better_object(self.not_random)

            else:
                return better_object(Lolibooru.append_obj(self.final))

        except Exception as e:
            raise ValueError(f"Failed to get data: {e}")

    async def get_image(self, query: str, block="", limit: int = 100, page: int = 1):

        """Gets images, meant just image urls from lolibooru.

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
            The json object returned by lolibooru.

        """

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        else:
            self.query = query

        self.specs["tags"] = str(self.query)
        self.specs["limit"] = str(limit)
        self.specs["page"] = str(page)

        try:
            self.data = requests.get(Booru.lolibooru, params=self.specs)
            self.final = self.final = deserialize(self.data.json())
            for i in range(len(self.final)):
                self.final[i]["tags"] = self.final[i]["tags"].split(" ")

            self.final = [i for i in self.final if not any(j in block for j in i["tags"])]

            self.not_random = parse_image(self.final)
            shuffle(self.not_random)
            return better_object(self.not_random)

        except:
            raise ValueError(f"Failed to get data")
