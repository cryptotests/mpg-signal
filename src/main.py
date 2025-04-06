python

import schedule

import time

from src.config import CONFIG

from src.api.coingecko import CoinGeckoClient

from src.api.coinmarketcap import CoinMarketCapClient

from src.api.dexscreener import DexScreenerClient

from src.analysis.signals import SignalAnalyzer

from src.utils.email_sender import EmailSender

 

def get_trending_coins(cg_client, cmc_client):

    cg_trending = cg_client.get_trending_coins()

    cmc_trending = cmc_client.get_trending_coins()

    

    all_trending = []

    seen_coins = set()

    

    for coin in cg_trending + cmc_trending:

        if coin.id not in seen_coins:

            all_trending.append(coin)

            seen_coins.add(coin.id)

    

    return all_trending

 

def run_analysis():

    # Initialize clients

    cg_client = CoinGeckoClient(CONFIG['COINGECKO_API_KEY'])

    cmc_client = CoinMarketCapClient(CONFIG['CMC_API_KEY'])

    dex_client = DexScreenerClient()

    

    # Initialize analyzer

    analyzer = SignalAnalyzer(cg_client, cmc_client, dex_client)

    

    # Get trending coins

    trending_coins = get_trending_coins(cg_client, cmc_client)

    

    # Analyze coins

    results = []

    for coin in trending_coins:

        analysis = analyzer.analyze_coin(coin)

        results.append(analysis)

    

    # Sort and get top 3

    top_results = sorted(results, key=lambda x: x['score'], reverse=True)[:CONFIG['TOP_COINS']]

    

    # Send email

    email_sender = EmailSender(CONFIG['EMAIL_SENDER'], CONFIG['EMAIL_PASSWORD'])

    email_sender.send_analysis(CONFIG['EMAIL_RECIPIENT'], top_results)

 

def main():

    schedule.every().day.at(CONFIG['ANALYSIS_TIME']).do(run_analysis)

    

    while True:

        schedule.run_pending()

        time.sleep(60)

 

if __name__ == "__main__":

    main()

