import asyncio
import booru

async def main():
    gel = booru.Tbib()
    # search for 1000 random cat_girls, in parallel batches of 100 at once to the Gelbooru API
    results = await asyncio.gather(*[
        gel.search("mei_terumi")
        for _ in range(10)
    ])
    results = [booru.resolve(res) for res in results]
    print(results)

asyncio.run(main())