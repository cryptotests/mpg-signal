python

from pycoingecko import CoinGeckoAPI

 

class CoinGeckoClient:

    def __init__(self, api_key):

        self.client = CoinGeckoAPI(api_key=api_key)

    

    def get_trending_coins(self):

        return self.client.get_search_trending()

    

    def get_coin_data(self, coin_id):

        return self.client.get_coin_by_id(coin_id)

