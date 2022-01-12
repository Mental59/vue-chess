import asyncio
import aioredis


async def main():
    redis = aioredis.from_url(
        "redis://0.0.0.0", encoding="utf-8", decode_responses=True
    )

    # async with redis.client() as conn:
    #     await conn.set("my-key", "value")
    #     val = await conn.get("my-key")
    # print(val)

    async with redis.client() as conn:
        val = await conn.get("my-")
        print(val)

    # async with redis.client() as conn:
    #     user = {"Name": "Pradeep", "Company": "SCTL", "Address": "Mumbai", "Location": "RCP"}
    #     await conn.hset("pythonDict", user)

    # conn.hmset("pythonDict", user)

    # async for key in redis.scan_iter("*"):
    #     val = await redis.get(key)
    #     print(val)

if __name__ == "__main__":
    asyncio.run(main())
