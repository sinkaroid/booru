import aiohttp
from typing import Union
from random import randint, shuffle
from .constant import Api

Booru = Api()


async def request(
    site: str, params_x: dict, ua: dict = Booru.headers, block: str = ""
) -> Union[aiohttp.ClientResponse, list, None]:
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

                pattern = [
                    i for i in pattern if not any(j in block for j in i["tags"])
                ]

                return pattern

            except Exception as e: ## danbooru
                if e.args[0] == "tags":
                    for i in range(len(pattern)):
                        pattern[i]["tag_string"] = pattern[i]["tag_string"].split(" ")

                    pattern = [
                        i for i in pattern if not any(j in block for j in i["tag_string"])
                    ]

                    return pattern

                else: ## furry stuff sigh
                    return pattern
                        

def roll(objek: list) -> dict:
    return objek[randint(0, len(objek) - 1)]
