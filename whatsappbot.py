
!pip install requests

import requests

NEWS_API_KEY = "185260d82d804402a8b96a9173be0c1d"  # From https://newsapi.org
ULTRAMSG_INSTANCE_ID = "instance126292"  # From https://ultramsg.com
ULTRAMSG_TOKEN = "k733rjhwbm9c8txc"  # From https://ultramsg.com
TO_PHONE_NUMBER = "918309359937"  # Your WhatsApp number (without +), e.g., 91XXXXXXXXXX
NUM_ARTICLES = 10  # Number of news articles to fetch

def get_latest_news():
    url = f"https://newsapi.org/v2/everything?q=India&language=en&sortBy=publishedAt&pageSize={NUM_ARTICLES}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    print("📦 Raw NewsAPI Response:", data)

    articles = data.get("articles", [])
    if not articles:
        return "No news articles found. Please check your API key or try a different query."

    message = "🗞️ *Top News Today:*\n\n"
    for i, article in enumerate(articles[:NUM_ARTICLES]):
        message += f"{i+1}. {article['title']}\n{article['url']}\n\n"
    return message.strip()



# Send WhatsApp Message via UltraMsg
def send_whatsapp_message(message):
    url = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"
    payload = {
        "token": ULTRAMSG_TOKEN,
        "to": TO_PHONE_NUMBER,
        "body": message
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    print("✅ Message sent! Response:", response.json())

#  Run the bot
news_message = get_latest_news()
send_whatsapp_message(news_message)
