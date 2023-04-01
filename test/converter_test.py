import requests
from currency_converter import CurrencyConverter
c = CurrencyConverter()

class TestCurrencyAPI:
    def test_currency_convertion_USD_EUR(self):
        test_amount = 100
        converted_value = c.convert(test_amount, 'EUR', 'USD')
        url = "https://www.theonlineconverter.co.uk/currency-converter/calculate"
        data = {'amount' : test_amount, 
                'from' : 'EUR',
                'to' : 'USD'
                }
        response = requests.post(url, params=data)
        assert response.status_code == 200
        assert response.text == f'<p> {test_amount} = {converted_value}</p>'
