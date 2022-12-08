import re
import aiohttp
from bs4 import BeautifulSoup
from typing import Union
from random import randint
from .constant import Api, ascii_to_str

Booru = Api()


async def request(
    site: str, params_x: dict, ua: dict = Booru.headers, block: str = ""
) -> Union[aiohttp.ClientResponse, list, None]:
    """Fetch the site

    Parameters
    ----------
    site : str
        The site to request
    params_x : dict
        The parameters to be passed
    ua : dict
        The user agent to be passed
    block : str
        The tags to be blocked

    Returns
    -------
    Union[aiohttp.ClientResponse, list, None]
        The response
    """

    if site == Booru.behoimi:
        ua = Booru.behoimi_bypass
    async with aiohttp.ClientSession(headers=ua) as session:
        async with session.get(site, params=params_x) as resp:
            data = await resp.json(content_type=None)
            if not data:
                raise Exception(Booru.error_handling_null)

            if "post" not in data:
                pattern = data

            elif "post" in data:
                pattern = data["post"]

            elif "images" in data:
                pattern = data["images"]

            try:
                for i in range(len(pattern)):
                    pattern[i]["tags"] = pattern[i]["tags"].split(" ")

                pattern = [i for i in pattern if not any(j in block for j in i["tags"])]

                return pattern

            except Exception as e:  ## danbooru
                if e.args[0] == "tags":
                    for i in range(len(pattern)):
                        pattern[i]["tag_string"] = pattern[i]["tag_string"].split(" ")

                    pattern = [
                        i
                        for i in pattern
                        if not any(j in block for j in i["tag_string"])
                    ]

                    return pattern

                else:  ## furry stuff sigh
                    return pattern


def roll(objek: list) -> dict:
    """Roll the object

    Parameters
    ----------
    objek : list
        The object to be rolled

    Returns
    -------
    dict
        The rolled object
    """

    return objek[randint(0, len(objek) - 1)]


async def request_wildcard(site: str, query: str) -> Union[list, None]:
    """Fetch wildcard

    Parameters
    ----------
    site : str
        The site to request
    query : str
        The query to request

    Returns
    -------
    Union[list, None]
        The response
    """

    if (
        site == Booru.gelbooru_wildcard
        or site == Booru.hypnohub_wildcard
        or site == Booru.rule34_wildcard
        or site == Booru.realbooru_wildcard
        or site == Booru.safebooru_wildcard
        or site == Booru.tbib_wildcard
        or site == Booru.xbooru_wildcard
    ):
        sorting = Booru.base_gelbooru_sorting_tags
        stop_disini_anjing = "index.php?page=post&s=list&tags="

    elif site == Booru.danbooru_wildcard or site == Booru.atfbooru_wildcard:
        sorting = Booru.base_danbooru_sorting_tags
        stop_disini_anjing = "/posts?tags="

    elif (
        site == Booru.yandere_wildcard
        or site == Booru.konachan_wildcard
        or site == Booru.konachan_net_wildcard
        or site == Booru.lolibooru_wildcard
    ):
        sorting = Booru.base_yandere_sorting_tags
        stop_disini_anjing = "/post?tags="

    async with aiohttp.ClientSession() as session:
        async with session.get(f"{site}{query}*{sorting}") as resp:
            print(resp.url)
            soup = BeautifulSoup(await resp.text(), "html.parser")
            get_all = soup.find_all("a")
            all_tags = [tag["href"] for tag in get_all]

            all_tags = [tag for tag in all_tags if tag.startswith(stop_disini_anjing)]
            ## findall /posts?tags=(.*)
            validate_tags = [
                re.findall(r"tags=(.*)", tag)[0]
                for tag in all_tags
                if re.findall(r"tags=(.*)", tag)
            ]

            tags = [
                tag
                for tag in validate_tags
                if tag != "all"
                and tag != "order%3Arandom"
                and tag != "translation_request"
            ]

            return ascii_to_str(tags)
