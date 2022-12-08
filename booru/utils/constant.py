import json
import re
from booru import __version__


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
        e_handling_invalid_auth (str): The error message for the invalid auth.
        headers (dict): The headers request.
        bypass_headers (dict): The bypass headers request.

        base_gelbooru_sorting_tags (str): Pattern for gelbooru sorting tags. 
        base_danbooru_sorting_tags (str): Pattern for danbooru sorting tags.
        base_yande_sorting_tags (str): Pattern for yande sorting tags.

        gelbooru_wildcard (str): The base wildcard url for gelbooru search.
        hypnohub_wildcard (str): The base wildcard url for hypnohub search.
        rule34_wildcard (str): The base wildcard url for rule34 search.
        realbooru_wildcard (str): The base wildcard url for realbooru search.
        safebooru_wildcard (str): The base wildcard url for safebooru search.
        tbib_wildcard (str): The base wildcard url for tbib search.
        xbooru_wildcard (str): The base wildcard url for xbooru search.

        danbooru_wildcard (str): The base wildcard url for danbooru search.
        atfbooru_wildcard (str): The base wildcard url for atfbooru search.

        yandere_wildcard (str): The base wildcard url for yandere search.
        lolibooru_wildcard (str): The base wildcard url for lolibooru search.
        kona_wildcard (str): The base wildcard url for konachan search.
        konachan_net_wildcard (str): The base wildcard url for konachan.net search.
    """

    def __init__(
        self,
        BASE_headers={
            "User-Agent": f"booru/v{__version__} (https://pypi.org/project/booru);",
            "From": "hey@sinkaroid.org",
        },
        BYPASS_headers={
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1)",
            "Referer": "http://behoimi.org/data/ff/f3/",
            "From": "hey@sinkaroid.org",
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
        self.error_handling_limit = "there is a hard limit of 1000 posts per request."
        self.error_handling_sameval = "block values should not be hit to the query"
        self.error_handling_cantparse = "failed to get data, the api is misleading"
        self.error_handling_null = "no results, make sure you spelled everything right"
        self.error_handling_invalid_auth = "invalid api key or login"
        self.headers = BASE_headers
        self.behoimi_bypass = BYPASS_headers

        self.base_gelbooru_sorting_tags = "&sort=desc&order_by=index_count"
        self.base_danbooru_sorting_tags = "&search%5Border%5D=count"
        self.base_yandere_sorting_tags = "&type=&order=count"

        self.gelbooru_wildcard = "https://gelbooru.com/index.php?page=tags&s=list&tags="
        self.hypnohub_wildcard = "https://hypnohub.net/index.php?page=tags&s=list&tags="
        self.rule34_wildcard = "https://rule34.xxx/index.php?page=tags&s=list&tags="
        self.realbooru_wildcard = "https://realbooru.com/index.php?page=tags&s=list&tags="
        self.safebooru_wildcard = "https://safebooru.org/index.php?page=tags&s=list&tags="
        self.tbib_wildcard = "https://tbib.org/index.php?page=tags&s=list&tags="
        self.xbooru_wildcard = "https://xbooru.com/index.php?page=tags&s=list&tags="

        self.danbooru_wildcard = "https://danbooru.donmai.us/tags?commit=Search&search%5Bhide_empty%5D=yes&search%5Bname_or_alias_matches%5D="
        self.atfbooru_wildcard = "https://booru.allthefallen.moe/tags?commit=Search&search%5Bhide_empty%5D=yes&search%5Bname_or_alias_matches%5D="

        self.yandere_wildcard = "https://yande.re/tag?name="
        self.konachan_wildcard = "https://konachan.com/tag?name="
        self.konachan_net_wildcard = "https://konachan.net/tag?name="
        self.lolibooru_wildcard = "https://lolibooru.moe/tag?name="
        
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
    str
        The new dictionaries with neat keys.

    """
    return json.dumps(parser, sort_keys=True, indent=4, ensure_ascii=False)


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

    images = list(dict.fromkeys(images))
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


def resolve(b_object: dict) -> dict:
    """Resolves the json object.

    Parameters
    ----------
    b_object : dict

    Returns
    -------
    dict
        raw json object
    """
    return json.loads(b_object)


def parse_image_danbooru(raw_object: dict) -> list:
    """Smh, it's danbooru though

    Parameters
    ----------
    raw_object : dict
        The object to be parsed.

    Returns
    -------
    list
        The list of image urls.
    """

    image = []

    try:
        for i in raw_object:
            image.append(i["file_url"])
        return image
    except KeyError:
        for i in raw_object:
            try:
                image.append(i["file_url"])
            except KeyError:
                pass
        return list(set(image))

def ascii_to_str(data: list):
    """ASCII to string 

    Parameters
    ----------
    data : list
        The data to be replaced

    Returns
    -------
    list
        The replaced data
    """

    bad_char = ["%28", "%29", "%2A", "%2F", "%3D", "%3A", "%27"]
    excpected_char = ["(", ")", "*", "/", "=", ":", "'"]
    for i in range(len(data)):
        for j in range(len(bad_char)):
            data[i] = data[i].replace(bad_char[j], excpected_char[j])

    return data

