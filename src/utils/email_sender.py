python

import smtplib

from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart

from jinja2 import Template

 

class EmailSender:

    def __init__(self, sender_email, password):

        self.sender_email = sender_email

        self.password = password

        

    def _get_email_template(self):

        template_str = """

        <html>

        <head>

            <style>

                body { font-family: Arial, sans-serif; }

                .coin { margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; }

                .metrics { margin-left: 20px; }

                .score { font-size: 18px; font-weight: bold; }

            </style>

        </head>

        <body>

            <h2>MPG Signal Daily Crypto Analysis</h2>

            {% for result in results %}

            <div class="coin">

                <div class="score">Score: {{ result.score }}/100</div>

                <h3>{{ result.coin }}</h3>

                <div class="metrics">

                    <p>Market Cap: ${{ '{:,.2f}'.format(result.metrics.market_cap) }}</p>

                    <p>24h Volume: ${{ '{:,.2f}'.format(result.metrics.volume_24h) }}</p>

                    <p>24h Price Change: {{ '{:.2f}'.format(result.metrics.price_change_24h) }}%</p>

                    <p>Liquidity: ${{ '{:,.2f}'.format(result.metrics.liquidity) }}</p>

                    <p>Social Score: {{ result.metrics.social_score }}/100</p>

                    <p>Holders: {{ result.metrics.holders }}</p>

                    <p>Trading Pairs: {{ result.metrics.trading_pairs }}</p>

                    <p>Twitter Followers: {{ '{:,}'.format(result.metrics.community_growth) }}</p>

                </div>

            </div>

            {% endfor %}

        </body>

        </html>

        """

        return Template(template_str)

    

    def send_analysis(self, recipient, analysis_results):

        msg = MIMEMultipart()

        msg['From'] = self.sender_email

        msg['To'] = recipient

        msg['Subject'] = 'MPG Signal Daily Crypto Analysis'

        

        template = self._get_email_template()

        body = template.render(results=analysis_results)

        msg.attach(MIMEText(body, 'html'))

        

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

            server.login(self.sender_email, self.password)

            server.send_message(msg)

