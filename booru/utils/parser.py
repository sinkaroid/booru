import json
import re
from random import sample
from booru import __version__
from xmltodict import parse
from requests import get


class Api:
    """Api class

    This class is used to parse the data from the api.

    Attributes:
        gelbooru (str): The base url for gelbooru.
        rule34 (str): The base url for rule34.
        tbib (str): The base url for tbib.
        safebooru (str): The base url for safebooru.
        xbooru (str): The base url for xbooru.
        realbooru (str): The base url for realbooru.
        hypnohub (str): The base url for hypnohub.
        danbooru (str): The base url for danbooru.
        atfbooru (str): The base url for atfbooru.
        yandere (str): The base url for yandere.
        konachan (str): The base url for konachan.
        konachan_net (str): The base url for konachan.net.
        lolibooru (str): The base url for lolibooru.
        e621 (str): The base url for e621.
        e926 (str): The base url for e926.
        derpibooru (str): The base url for derpibooru.
        furbooru (str): The base url for furbooru.
        behoimi (str): The base url for behoimi.
        paheal (str): The base url for paheal.
        e_handling_limit (str): The error message for the limit.
        e_handling_sameval (str): The error message for the same values.
        e_handling_cantparse (str): The error message for the parsing.
        e_handling_null (str): The error message for the null.
    """

    def __init__(
        self,
        BASE_headers={
            "User-Agent": f"booru/v{__version__} (https://pypi.org/project/booru);",
            "From": "anakmancasan@gmail.com",
        },
        BYPASS_headers={
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1)",
            "Referer": "http://behoimi.org/data/ff/f3/",
            "From": "anakmancasan@gmail.com",
        },
    ):

        self.gelbooru = "https://gelbooru.com/index.php?page=dapi&s=post&q=index"
        self.rule34 = "https://rule34.xxx/index.php?page=dapi&s=post&q=index"
        self.tbib = "https://tbib.org/index.php?page=dapi&s=post&q=index"
        self.safebooru = "https://safebooru.org/index.php?page=dapi&s=post&q=index"
        self.xbooru = "https://xbooru.com/index.php?page=dapi&s=post&q=index"
        self.realbooru = "https://realbooru.com/index.php?page=dapi&s=post&q=index"
        self.hypnohub = "https://hypnohub.net/index.php?page=dapi&s=post&q=index"
        self.danbooru = "https://danbooru.donmai.us/posts.json"
        self.atfbooru = "https://booru.allthefallen.moe/posts.json"
        self.yandere = "https://yande.re/post.json"
        self.konachan = "https://konachan.com/post.json"
        self.konachan_net = "https://konachan.net/post.json"
        self.lolibooru = "https://lolibooru.moe/post.json"
        self.e621 = "https://e621.net/posts.json"
        self.e926 = "https://e926.net/posts.json"
        self.derpibooru = "https://derpibooru.org/api/v1/json/search/images"
        self.furbooru = "https://furbooru.com/api/v1/json/search/images"
        self.behoimi = "http://behoimi.org/post/index.json"
        self.paheal = "https://rule34.paheal.net/api/danbooru/find_posts/index.xml"
        self.error_handling_limit = "there is a hard limit of 100 posts per request."
        self.error_handling_sameval = "block values should not be hit to the query"
        self.error_handling_cantparse = "failed to get data, the api is misleading"
        self.error_handling_null = "no results, make sure you spelled everything right"
        self.headers = BASE_headers
        self.behoimi_bypass = BYPASS_headers


BASE_URL = Api()


def list_api():
    """Returns the api url.

    Returns
    -------
    list
    """
    # create this list for mocking
    api_list = [
        BASE_URL.gelbooru,
        BASE_URL.rule34,
        BASE_URL.tbib,
        BASE_URL.safebooru,
        BASE_URL.xbooru,
        BASE_URL.realbooru,
        BASE_URL.hypnohub,
        BASE_URL.danbooru,
        BASE_URL.atfbooru,
        BASE_URL.yandere,
        BASE_URL.konachan,
        BASE_URL.konachan_net,
        BASE_URL.lolibooru,
        BASE_URL.e621,
        BASE_URL.e926,
        BASE_URL.derpibooru,
        BASE_URL.furbooru,
        BASE_URL.behoimi,
        BASE_URL.paheal,
    ]
    return api_list


def better_object(parser: dict):
    """Converts the json object to a more readable object.

    Parameters
    ----------
    parser : dict

    Returns
    -------
    dict
        The new dictionaries with neat keys.

    """
    return json.dumps(parser, sort_keys=True, indent=4, ensure_ascii=False)

def deserialize(data: list):
    """Deserialize instance containing a JSON document

    Parameters
    ----------
    data : list
        The raw data after fetch request

    Returns
    -------
    dict
        The deserialized with better object
    """
    return json.loads(better_object(data), encoding="utf-8")


def parse_image(raw_object: dict):
    """Extracts the image url from the json object.

    Parameters
    ----------
    obj : dict
        The object to be parsed.

    Returns
    -------
    list
        The list of image urls.
    """
    if "post" not in raw_object:
        data = raw_object

    elif "post" in raw_object:
        data = raw_object["post"]

    try:
        images = [i["file_url"] for i in data]

    except:
        images = [i["file"]["url"] for i in data]  # furry stuff sigh

    return images


def get_hostname(url: str):
    """Extract single hostname from the nested url

    Parameters
    ----------
    url : str

    Returns
    -------
    str
        The site contains protocol and hostname
    """
    return re.sub(r"(.*://)?([^/?]+).*", "\g<1>\g<2>", url)
