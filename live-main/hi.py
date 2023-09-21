import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '5835400119:AAG05VIHGiaNvefr3DKF4yd8bTAcZLSyxx4'

# Telegram API endpoint for deleting the webhook
url = f'https://api.telegram.org/bot{bot_token}/deleteWebhook'

try:
    response = requests.get(url)
    data = response.json()
    
    if data['ok']:
        print("Webhook deleted successfully.")
    else:
        print(f"Failed to delete webhook: {data['description']}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
