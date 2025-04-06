python

import pandas as pd

import numpy as np

 

class SignalAnalyzer:

    def __init__(self, coingecko, cmc, dexscreener):

        self.coingecko = coingecko

        self.cmc = cmc

        self.dexscreener = dexscreener

    

    def analyze_coin(self, coin):

        cg_data = self.coingecko.get_coin_data(coin.id)

        cmc_data = self.cmc.get_coin_data(coin.id)

        dex_data = self.dexscreener.get_pair_data(coin.contract)

        

        score = self._calculate_score(cg_data, cmc_data, dex_data)

        return {

            'coin': coin.id,

            'score': score,

            'metrics': self._generate_metrics(cg_data, cmc_data, dex_data)

        }

    

    def _calculate_score(self, cg_data, cmc_data, dex_data):

        score = 0

        

        # Market cap score (0-20 points)

        market_cap = float(cg_data['market_data']['market_cap']['usd'])

        if market_cap > 1000000000:  # > 1B

            score += 20

        elif market_cap > 100000000:  # > 100M

            score += 15

        elif market_cap > 10000000:  # > 10M

            score += 10

        else:

            score += 5

 

        # Volume score (0-20 points)

        volume = float(cg_data['market_data']['total_volume']['usd'])

        volume_to_market_cap = volume / market_cap

        if volume_to_market_cap > 0.3:

            score += 20

        elif volume_to_market_cap > 0.2:

            score += 15

        elif volume_to_market_cap > 0.1:

            score += 10

        else:

            score += 5

 

        # Price change score (0-20 points)

        price_change_24h = abs(float(cg_data['market_data']['price_change_percentage_24h']))

        if price_change_24h > 20:

            score += 20

        elif price_change_24h > 10:

            score += 15

        elif price_change_24h > 5:

            score += 10

        else:

            score += 5

 

        # Social score (0-20 points)

        social_score = float(cg_data['community_score'])

        if social_score > 80:

            score += 20

        elif social_score > 60:

            score += 15

        elif social_score > 40:

            score += 10

        else:

            score += 5

 

        # Liquidity score (0-20 points)

        liquidity = float(dex_data['liquidity']['usd'])

        if liquidity > 1000000:  # > 1M

            score += 20

        elif liquidity > 500000:  # > 500K

            score += 15

        elif liquidity > 100000:  # > 100K

            score += 10

        else:

            score += 5

 

        return score

 

    def _generate_metrics(self, cg_data, cmc_data, dex_data):

        return {

            'market_cap': cg_data['market_data']['market_cap']['usd'],

            'volume_24h': cg_data['market_data']['total_volume']['usd'],

            'price_change_24h': cg_data['market_data']['price_change_percentage_24h'],

            'social_score': cg_data['community_score'],

            'liquidity': dex_data['liquidity']['usd'],

            'holders': cmc_data['holders_count'],

            'trading_pairs': len(cg_data['tickers']),

            'community_growth': cg_data['community_data']['twitter_followers'],

        }

