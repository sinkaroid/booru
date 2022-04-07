import argparse
import asyncio
import booru
import requests


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
    def fetch(imgboard: str, search: str):
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

        async def main():
            data = await imgboard.search(query=search, limit=5)
            print(data)

        return asyncio.run(main())


Base = Wrapper()
Internal = booru.utils.parser.Api()

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

args = parse.parse_args()


def main():
    if args.gelbooru:
        Wrapper.fetch(Base.gelbooru, args.gelbooru)
    elif args.rule34:
        Wrapper.fetch(Base.rule34, args.rule34)
    elif args.tbib:
        Wrapper.fetch(Base.tbib, args.tbib)
    elif args.safebooru:
        Wrapper.fetch(Base.safebooru, args.safebooru)
    elif args.xbooru:
        Wrapper.fetch(Base.xbooru, args.xbooru)
    elif args.realbooru:
        Wrapper.fetch(Base.realbooru, args.realbooru)
    elif args.hypnohub:
        Wrapper.fetch(Base.hypnohub, args.hypnohub)
    elif args.danbooru:
        Wrapper.fetch(Base.danbooru, args.danbooru)
    elif args.atfbooru:
        Wrapper.fetch(Base.atfbooru, args.atfbooru)
    elif args.yandere:
        Wrapper.fetch(Base.yandere, args.yandere)
    elif args.konachan:
        Wrapper.fetch(Base.konachan, args.konachan)
    elif args.konachan_net:
        Wrapper.fetch(Base.konachan_net, args.konachan_net)
    elif args.lolibooru:
        Wrapper.fetch(Base.lolibooru, args.lolibooru)
    elif args.e6:
        Wrapper.fetch(Base.e621, args.e6)
    elif args.e9:
        Wrapper.fetch(Base.e926, args.e9)
    elif args.derpibooru:
        Wrapper.fetch(Base.derpibooru, args.derpibooru)
    elif args.furbooru:
        Wrapper.fetch(Base.furbooru, args.furbooru)
    elif args.behoimi:
        Wrapper.fetch(Base.behoimi, args.behoimi)
    elif args.paheal:
        Wrapper.fetch(Base.paheal, args.paheal)
    elif args.build:
        print(booru.__version__)

    elif args.api:
        for api in booru.utils.parser.list_api():
            res = booru.utils.parser.get_hostname(api)

            if res == "http://behoimi.org":
                Internal.headers = Internal.behoimi_bypass

            r = requests.get(res, headers=Internal.headers)
            print(res, r.status_code)

    else:
        print("No arguments given")


if __name__ == "__main__":
    main()
