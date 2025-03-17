import csv
import asyncio
import zipfile
from io import BytesIO, StringIO

import httpx


async def create_record(sem: asyncio.Semaphore, row: dict) -> None:
    """
    Post the data to API
    """
    async with sem:
        client = httpx.AsyncClient()
        await client.post("http://127.0.0.1:8000/imports/", json=dict(row))
        await client.aclose()


async def main():
    """
    Downloads data for U.S. Crude Oil Imports and posts data to API
    """
    url = "https://www.kaggle.com/api/v1/datasets/download/alistairking/u-s-crude-oil-imports"
    response = httpx.get(url, follow_redirects=True)
    bytes = BytesIO(response.read())
    zf = zipfile.ZipFile(bytes)
    text = StringIO(zf.open("data.csv").read().decode())
    csvreader = csv.DictReader(text)

    i = 0
    sem = asyncio.Semaphore(100)  # Limit tasks to 10 concurrent tasks
    async with asyncio.TaskGroup() as tg:
        for row in csvreader:
            i += 1
            tg.create_task(create_record(sem, row))
        print(f"{i} tasks created.")

    print("tasks complete.")


if __name__ == "__main__":
    asyncio.run(main())
