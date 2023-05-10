class Price:
    def __init__(self, amount: int, currency: str):
        self.amount: int = amount
        self.currency: str = currency

    def __add__(self, other):
        rates_USD = ExchangeRates.exchange_rates[self.currency]
        rates_other = ExchangeRates.exchange_rates[other.currency]
        if self.currency == other.currency:
            return Price(round(self.amount + other.amount, 2), self.currency)
        elif other.currency == "USD":
            return Price(
                round(self.amount + other.amount * rates_USD, 2), self.currency
            )
        else:
            return Price(
                round(self.amount + other.amount / rates_other * rates_USD, 2),
                self.currency,
            )

    def __sub__(self, other):
        rates_USD = ExchangeRates.exchange_rates[self.currency]
        rates_other = ExchangeRates.exchange_rates[other.currency]
        if self.currency == other.currency:
            return Price(round(self.amount - other.amount, 2), self.currency)
        elif other.currency == "USD":
            return Price(
                round(self.amount - other.amount * rates_USD, 2), self.currency
            )
        else:
            return Price(
                round(self.amount - other.amount / rates_other * rates_USD, 2),
                self.currency,
            )

    def __str__(self):
        return f"{self.amount} {self.currency}"


class ExchangeRates:
    exchange_rates = {"UAH": 36.9259, "EUR": 0.9061, "GBP": 0.8002, "USD": 1}


def main():
    type_currency = ["UAH", "USD", "EUR", "GBP"]
    while True:
        currency_1 = input(f"Enter the first currency {type_currency}: ")
        amount_1 = float(input("Enter amount: "))
        price_1 = Price(amount=amount_1, currency=currency_1)
        currency_2 = input(f"Enter the second currency {type_currency}: ")
        if not currency_2:
            print("Second currency not entered")
            break
        else:
            amount_2 = float(input("Enter amount: "))
            price_2 = Price(amount=amount_2, currency=currency_2)
            price_add = price_1 + price_2
            price_sub = price_1 - price_2
            print(f"Sum of prices: {price_add}")
            print(f"Substraction of prices: {price_sub}")
            break


if __name__ == "__main__":
    main()
