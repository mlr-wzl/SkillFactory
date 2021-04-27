import requests
import json
from config import keys

class APIException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f"You don't need to convert {quote} in {quote}, don't you?")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"It was not possible to process currency {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"It was not possible to process currency {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'{amount} could not be processed')

        r_base = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=27c1bfcad0c47501c40be7e870cdd857&symbols={base_ticker}&format=1')
        r_quote = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=27c1bfcad0c47501c40be7e870cdd857&symbols={quote_ticker}&format=1')

        total_base = json.loads(r_base.content)['rates'][keys[base]]
        total_quote = json.loads(r_quote.content)['rates'][keys[quote]]
        return round((total_base/total_quote)*amount,2)


