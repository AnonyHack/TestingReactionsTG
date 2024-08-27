from pyrogram import Client, filters
import requests
import random

api_id = 25753873 #--Add your Api Id here
api_hash = '3a5cdc2079cd76af80586102bd9761e2' #--Enter Api Hash Here

token = '7540444974:AAGKv6FfmW1CaLXQYqko-vIqLu9svLGW5i8' #--Enter Bot Token Here.

emojis = ["👍", "❤️", "🔥", "🥰", "👏", "😁", "🤯", "😱", "🎉", "🤩", "🙏", "👌", "🕊", "🤡", "😍", "❤‍🔥", "💯", "⚡️", "🏆", "🍓", "🍾", "💋", "😈", "🤓", "👻", "🙈", "😇", "🤝", "✍️", "🤗", "🫡", "🆒", "💘", "🙉", "🦄", "😘", "🙊", "😎"]

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)

@app.on_message()
async def react_to_message(client, message):
    chat_id = message.chat.id
    message_id = message.id
    
    # Choose a random emoji from the list
    random_emoji = random.choice(emojis)
    
    url = f'https://api.telegram.org/bot{token}/setMessageReaction'

    # Parameters for the request
    params = {
        'chat_id': chat_id,
        'message_id': message_id,
        'reaction': [{
            "type": "emoji",
            "emoji": random_emoji
        }]
    }

    response = requests.post(url, json=params)

    if response.status_code == 200:
        print("Reaction set successfully!")
        print("Response content:", response.content)
    else:
        print(f"Failed to set reaction. Status code: {response.status_code}")
        print("Response content:", response.content)
    
app.run()