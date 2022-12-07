import argparse
import aiohttp
import asyncio
import booru
import os


class Wrapper(object):
    def __init__(self):

        self.gelbooru = booru.Gelbooru()
        self.rule34 = booru.Rule34()
        self.tbib = booru.Tbib()
        self.safebooru = booru.Safebooru()
        self.xbooru = booru.Xbooru()
        self.realbooru = booru.Realbooru()
        self.hypnohub = booru.Hypnohub()
        self.danbooru = booru.Danbooru()
        self.atfbooru = booru.Atfbooru()
        self.yandere = booru.Yandere()
        self.konachan = booru.Konachan()
        self.konachan_net = booru.Konachan_Net()
        self.lolibooru = booru.Lolibooru()
        self.e621 = booru.E621()
        self.e926 = booru.E926()
        self.derpibooru = booru.Derpibooru()
        self.furbooru = booru.Furbooru()
        self.behoimi = booru.Behoimi()
        self.paheal = booru.Paheal()

    @staticmethod
    async def fetch(imgboard: str, search: str):
        """Fetches the data from safebooru.

        Parameters
        ----------
        imgboard : str
            The imageboard to be searched.

        search : str
            The search term to be used.

        Returns
        -------
        dict
            The data that represents the search from separate booru
        """

        data = await imgboard.search(query=search, limit=1)
        print("Data", data)
        print(len(booru.resolve(data)))


        image = await imgboard.search_image(query=search)
        print("Image", image)

        gacha = await imgboard.search(query=search, limit=30, gacha=True)
        print("Gacha", gacha)


Base = Wrapper()
Internal = booru.utils.constant.Api()

parse = argparse.ArgumentParser(description="Booru tests")

parse.add_argument("-api", action="store_true")
parse.add_argument("-build", action="store_true")
parse.add_argument("-gelbooru", action="store", type=str)
parse.add_argument("-rule34", action="store", type=str)
parse.add_argument("-tbib", action="store", type=str)
parse.add_argument("-safebooru", action="store", type=str)
parse.add_argument("-xbooru", action="store", type=str)
parse.add_argument("-realbooru", action="store", type=str)
parse.add_argument("-hypnohub", action="store", type=str)
parse.add_argument("-danbooru", action="store", type=str)
parse.add_argument("-atfbooru", action="store", type=str)
parse.add_argument("-yandere", action="store", type=str)
parse.add_argument("-konachan", action="store", type=str)
parse.add_argument("-konachan_net", action="store", type=str)
parse.add_argument("-lolibooru", action="store", type=str)
parse.add_argument("-e6", action="store", type=str)
parse.add_argument("-e9", action="store", type=str)
parse.add_argument("-derpibooru", action="store", type=str)
parse.add_argument("-furbooru", action="store", type=str)
parse.add_argument("-behoimi", action="store", type=str)
parse.add_argument("-paheal", action="store", type=str)
parse.add_argument("-changelog", action="store_true")

args = parse.parse_args()


async def main():
    if args.gelbooru:
        await Wrapper.fetch(Base.gelbooru, args.gelbooru)
    elif args.rule34:
        await Wrapper.fetch(Base.rule34, args.rule34)
    elif args.tbib:
        await Wrapper.fetch(Base.tbib, args.tbib)
    elif args.safebooru:
        await Wrapper.fetch(Base.safebooru, args.safebooru)
    elif args.xbooru:
        await Wrapper.fetch(Base.xbooru, args.xbooru)
    elif args.realbooru:
        await Wrapper.fetch(Base.realbooru, args.realbooru)
    elif args.hypnohub:
        await Wrapper.fetch(Base.hypnohub, args.hypnohub)
    elif args.danbooru:
        await Wrapper.fetch(Base.danbooru, args.danbooru)
    elif args.atfbooru:
        await Wrapper.fetch(Base.atfbooru, args.atfbooru)
    elif args.yandere:
        await Wrapper.fetch(Base.yandere, args.yandere)
    elif args.konachan:
        await Wrapper.fetch(Base.konachan, args.konachan)
    elif args.konachan_net:
        await Wrapper.fetch(Base.konachan_net, args.konachan_net)
    elif args.lolibooru:
        await Wrapper.fetch(Base.lolibooru, args.lolibooru)
    elif args.e6:
        await Wrapper.fetch(Base.e621, args.e6)
    elif args.e9:
        await Wrapper.fetch(Base.e926, args.e9)
    elif args.derpibooru:
        await Wrapper.fetch(Base.derpibooru, args.derpibooru)
    elif args.furbooru:
        await Wrapper.fetch(Base.furbooru, args.furbooru)
    elif args.behoimi:
        await Wrapper.fetch(Base.behoimi, args.behoimi)
    elif args.paheal:
        await Wrapper.fetch(Base.paheal, args.paheal)
    elif args.build:
        print(booru.__version__)

    elif args.changelog:
        os.system('git-changelog -o CHANGELOG.md -s angular -t angular .')

    elif args.api:
        for api in booru.utils.parser.list_api():
            res = booru.utils.parser.get_hostname(api)

            if res == "http://behoimi.org":
                Internal.headers = Internal.behoimi_bypass

            async with aiohttp.ClientSession(headers=Internal.headers) as resp:
                async with resp.get(res) as data:
                    print(f"{api} : {data.status}")

    else:
        print("No arguments given")


if __name__ == "__main__":
    asyncio.run(main())
