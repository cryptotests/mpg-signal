python

from coinmarketcap import Market

 

class CoinMarketCapClient:

    def __init__(self, api_key):

        self.client = Market(api_key=api_key)

    

    def get_trending_coins(self):

        return self.client.trending_latest()

    

    def get_coin_data(self, coin_id):

        return self.client.ticker(coin_id)

