import requests
import json
import re
from ..utils.parser import Api, better_object, get_hostname, read_json
from random import shuffle, randint
from xmltodict import parse

Booru = Api()


class Paheal(object):
    """paheal wrapper

    Methods
    -------
    search : function
        Search and gets images from paheal.

    get_image : function
        Gets images, meant just image urls from paheal.

    """

    def __init__(self, api_key: str = "", user_id: str = ""):
        """Initializes paheal.

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
    ):

        """Search and gets images from paheal.

        Parameters
        ----------
        query : str
            The tags to search for.

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
            The json object returned by paheal.
        """
        if gacha:
            limit = 100

        if limit > 100:
            raise ValueError(Booru.error_handling_limit)

        else:
            self.tags = query

        self.specs["tags"] = str(self.tags)
        self.specs["limit"] = str(limit)
        self.specs["page"] = str(page)

        self.data = requests.get(Booru.paheal, params=self.specs)
        data_dict = parse(self.data.text)
        unsolved = json.dumps(data_dict)
        self.final = json.loads(unsolved, encoding="utf-8")

        if "tag" not in self.final["posts"]:
            raise ValueError(Booru.error_handling_null)

        self.not_random = self.final["posts"]["tag"]
        shuffle(self.not_random)

        try:
            if gacha:
                return better_object(
                    self.final["posts"]["tag"][
                        randint(0, len(self.final["posts"]["tag"]))
                    ]
                )

            elif random:
                return better_object(self.final["posts"]["tag"])

            else:
                return better_object(self.not_random)

        except:
            raise ValueError(f"Failed to get data")

    async def get_image(self, query: str, limit: int = 100, page: int = 1):

        """Gets images, meant just image urls from paheal.

        Parameters
        ----------
        query : str
            The tags to search for.

        limit : int
            The limit of images to return.

        page : int
            The number of desired page

        Returns
        -------
        list
            The list of image urls.

        """

        if limit > 100:
            raise ValueError(Booru.error_handling_limit)

        else:
            self.tags = query

        self.specs["tags"] = str(self.query)
        self.specs["limit"] = str(limit)
        self.specs["page"] = str(page)

        try:
            self.data = requests.get(Booru.paheal, params=self.specs)
            data_dict = parse(self.data.text)
            unsolved = json.dumps(data_dict)
            self.final = json.loads(unsolved, encoding="utf-8")

            abc_kontol = self.final["posts"]["tag"]
            ## extract all image urls
            self.image_urls = []
            for i in abc_kontol:  # paheal emang ngentot
                self.image_urls.append(i["@file_url"])

            shuffle(self.image_urls)
            return better_object(self.image_urls)

        except Exception as e:
            raise ValueError(f"Failed to get data: {e}")
