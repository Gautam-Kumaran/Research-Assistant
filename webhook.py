'''import requests
import json


data = { 'message': 'Hello World!'}

r = requests.post(webhookURL, data=json.dumps(data), headers={'Content-Type': 'application/json'})'''

import requests

webhookURL = 'https://discord.com/api/webhooks/1136179249255043122/WoM8myNnutg1Eoq7bDYToqK5Qs7GVeBVglDGyxmeBCcRbwVaDRgqzG15HrxO8kr7k_WC'


def send_webhook(url, content):
    headers = {'Content-Type': 'application/json'}
    data = {'content': content}

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print("Webhook sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send webhook: {e}")

def sendToTeams(message):
    webhook_url = webhookURL
    message_content = message

    send_webhook(webhook_url, message_content)

'''from discord_webhook import DiscordWebhook, DiscordEmbed

content = "Hello, World!"

webhook = DiscordWebhook(url=webhookURL, content=content, username = "Research Assistant")

embed = DiscordEmbed(title='Research Assistant', description='Hello, World', color=242424)

webhook.add_embed(embed)
response = webhook.execute()'''