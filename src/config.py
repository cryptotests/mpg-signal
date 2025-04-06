python

import os

from dotenv import load_dotenv

 

load_dotenv()

 

CONFIG = {

    'COINGECKO_API_KEY': os.getenv('COINGECKO_API_KEY'),

    'CMC_API_KEY': os.getenv('CMC_API_KEY'),

    'EMAIL_SENDER': os.getenv('EMAIL_SENDER'),

    'EMAIL_PASSWORD': os.getenv('EMAIL_PASSWORD'),

    'EMAIL_RECIPIENT': os.getenv('EMAIL_RECIPIENT'),

    'ANALYSIS_TIME': '20:00',

    'TOP_COINS': 3

}

