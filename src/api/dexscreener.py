python

from dexscreener_api import DexScreener

 

class DexScreenerClient:

    def __init__(self):

        self.client = DexScreener()

    

    def get_pair_data(self, token_address):

        return self.client.get_pair(token_address)

