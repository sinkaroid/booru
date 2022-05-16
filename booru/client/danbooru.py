import requests
import json
import re
from ..utils.parser import Api, better_object, parse_image, get_hostname, deserialize
from random import shuffle, randint

Booru = Api()


class Danbooru(object):
    """Danbooru wrapper

    Methods
    -------
    search : function
        Search and gets images from danbooru.

    get_image : function
        Gets images, image urls only from danbooru.

    """

    @staticmethod
    def append_obj(raw_object: dict):
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

        if api_key and login == "":
            self.api_key = None
            self.login = None
        else:
            self.api_key = api_key
            self.login = login

        self.specs = {"api_key": self.api_key, "login": self.login}

        if self.api_key and self.login:
            self.data = requests.get(f"https://danbooru.donmai.us/profile.json?api_key={self.api_key}&login={self.login}")
            
            if self.data.status_code != 200:
                raise ValueError(Booru.error_handling_invalid_auth)


    async def search(
        self,
        query: str,
        block: str = "",
        limit: int = 100,
        page: int = 1,
        random: bool = True,
        gacha: bool = False,
    ):

        """Search and gets images from danbooru.

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
            The json object returned by danbooru.
        """
        if gacha:
            limit = 100

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        if block != "":
            self.query = f"{query} -{block}*"

        else:
            self.query = query

        self.specs["tags"] = str(self.query)
        self.specs["limit"] = str(limit)
        self.specs["pid"] = str(page)
        self.specs["json"] = "1"

        self.data = requests.get(Booru.danbooru, params=self.specs)
        self.final = self.final = deserialize(self.data.json())

        if not self.final:
            raise ValueError(Booru.error_handling_null)

        self.not_random = Danbooru.append_obj(self.final)
        shuffle(self.not_random)

        try:
            if gacha:
                return better_object(self.not_random[randint(0, len(self.not_random))])

            elif random:
                return better_object(self.not_random)

            else:
                return better_object(Danbooru.append_obj(self.final))

        except Exception as e:
            raise ValueError(f"Failed to get data: {e}")

    async def get_image(
        self, query: str, block: str = "", limit: int = 100, page: int = 1
    ):

        """Gets images, meant just image urls from danbooru.

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
        dict
            The json object returned by danbooru.

        """

        if limit > 1000:
            raise ValueError(Booru.error_handling_limit)

        if block and re.findall(block, query):
            raise ValueError(Booru.error_handling_sameval)

        if block != "":
            self.query = f"{query} -{block}*"

        else:
            self.query = query

        self.specs["tags"] = str(self.query)
        self.specs["limit"] = str(limit)
        self.specs["pid"] = str(page)
        self.specs["json"] = "1"

        try:
            self.data = requests.get(Booru.danbooru, params=self.specs)
            self.final = self.final = deserialize(self.data.json())

            self.not_random = parse_image(self.final)
            shuffle(self.not_random)
            return better_object(self.not_random)

        except:
            raise ValueError(f"Failed to get data")
