import asyncio
from time import perf_counter

import httpx


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if ExchangeRates._initialized:
            return
        ExchangeRates._initialized = True

    @staticmethod
    async def get_rate(cur1, cur2):
        async with httpx.AsyncClient() as client:
            url = (
                f"https://www.alphavantage.co/query?function"
                f"=CURRENCY_EXCHANGE_RATE&from_currency={cur1}"
                f"&to_currency={cur2}&apikey=PASTE_YOUR_API_KEY"
            )
            response = await client.get(url)
            content = list(response.json().values())
            print(content[0]["5. Exchange Rate"])


async def main():
    er = ExchangeRates()
    tasks = [
        er.get_rate("USD", "UAH"),
        er.get_rate("UAH", "USD"),
        er.get_rate("EUR", "UAH"),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()
    print(f"Total time: {end-start}")
