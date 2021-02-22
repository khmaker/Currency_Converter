import requests


class CurrencyConverter:
    cache = {}

    def __init__(self, base_currency: str):
        self.base_currency = base_currency
        self.cache.update(self.get_currency_json('usd'))
        self.cache.update(self.get_currency_json('eur'))

    @staticmethod
    def get_currency_json(currency: str):
        r = requests.get(f'http://www.floatrates.com/daily/{currency}.json')
        rates = r.json()
        for rate in rates.keys():
            rates[rate] = rates[rate].get('inverseRate')
        return {currency: rates}

    def convert(self, currency: str, amount: float):
        self.check_cache(currency)
        rate = self.cache.get(currency).get(self.base_currency)
        return amount * rate

    def check_cache(self, currency: str):
        in_cache = 'Oh! It is in the cache!'
        not_in_cache = 'Sorry, but it is not in the cache!'
        print('Checking the cache…')
        currency_in_cache = currency in self.cache
        print(in_cache if currency_in_cache else not_in_cache)
        if not currency_in_cache:
            self.cache.update(self.get_currency_json(currency))


currencies_set = {'usd', }
currency_dict = CurrencyConverter.get_currency_json('usd')
currencies_set.update(currency_dict.get('usd').keys())

if __name__ == '__main__':

    my_currency = input().lower()

    if my_currency in currencies_set:
        converter = CurrencyConverter(my_currency)
        while True:
            target_currency = input().lower()
            if target_currency == '':
                break
            amount_of_money = input()
            try:
                amount_of_money = float(amount_of_money)
            except ValueError as e:
                print(e)
            value = converter.convert(target_currency, amount_of_money)
            print(f'You received {value:.2f} {target_currency.upper()}')

    else:
        print('No such currency')
