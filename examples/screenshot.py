import asyncio
from ResentAPI import API 

api = API("YOUR-API-KEY-HERE")

async def main():
    data = await api.screenshot("https://api.resent.dev")
    print(f"Screenshot url: {data.image_url}")

if __name__ == "__main__":
    asyncio.run(main())