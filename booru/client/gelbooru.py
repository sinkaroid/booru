import requests
import json
import re
from ..utils.parser import Api, better_object, parse_image, get_hostname, deserialize
from random import shuffle, randint

Booru = Api()


class Gelbooru(object):
    """Gelbooru wrapper

    Methods
    -------
    search : function
        Search and gets images from gelbooru.

    get_image : function
        Gets images, meant just image urls from gelbooru.

    """

    @staticmethod
    def append_obj(raw_object: dict):
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
    ):

        """Search and gets images from gelbooru.

        Parameters
        ----------
        query : str
            The query to search for.

        block : str
            The disgusting query you want to block,
            e.g: you want to search 'erza_scarlet' but dont want to gets furry, fill in 'furry'

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
            The json object returned by gelbooru.
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
        self.specs["pid"] = str(page)
        self.specs["json"] = "1"

        self.data = requests.get(Booru.gelbooru, params=self.specs)
        self.final = self.final = deserialize(self.data.json())

        if "post" not in self.final or not self.final:
            raise ValueError(Booru.error_handling_null)

        self.final = self.final["post"]
        for i in range(len(self.final)):
            self.final[i]["tags"] = self.final[i]["tags"].split(" ")

        self.final = [i for i in self.final if not any(j in block for j in i["tags"])]

        self.not_random = Gelbooru.append_obj(self.final)
        shuffle(self.not_random)

        try:
            if gacha:
                return better_object(self.not_random[randint(0, len(self.not_random))])

            elif random:
                return better_object(self.not_random)

            else:
                return better_object(Gelbooru.append_obj(self.final))

        except Exception as e:
            raise ValueError(f"Failed to get data: {e}")

    async def get_image(
        self, query: str, block: str = "", limit: int = 100, page: int = 1
    ):

        """Gets images, meant just image urls from gelbooru.

        Parameters
        ----------
        query : str
            The query to search for.

        block : str
            The disgusting query you want to block,
            e.g: you want to search 'erza_scarlet' but dont want to gets furry, fill in 'furry'

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

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        else:
            self.query = query

        self.specs["tags"] = str(self.query)
        self.specs["limit"] = str(limit)
        self.specs["pid"] = str(page)
        self.specs["json"] = "1"

        try:
            self.data = requests.get(Booru.gelbooru, params=self.specs)
            self.final = self.final = deserialize(self.data.json())

            if "post" not in self.final:
                raise ValueError(Booru.error_handling_null)

            self.not_random = parse_image(self.final)
            shuffle(self.not_random)
            return better_object(self.not_random)

        except:
            raise ValueError(f"Failed to get data")
