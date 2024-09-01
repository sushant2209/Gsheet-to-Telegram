from telethon import TelegramClient
from .xtelethon import CustomParseMode  # Import your custom class
from django.conf import settings
from datetime import timedelta
from telethon.sessions import StringSession
import os

# Define the path for the GIF if needed
gif_path = os.path.join(settings.MEDIA_ROOT, "SampleGIF.gif")

async def send_message_to_telegram(message):
    

    api_id = settings.TELEGRAM_API_ID
    api_hash = settings.TELEGRAM_API_HASH
    client = TelegramClient(StringSession(settings.SESSION_STRING), settings.API_ID, settings.API_HASH)
    await client.start()  # Start the client asynchronously
    client.parse_mode = CustomParseMode('markdown')  # Set parse_mode if needed

    try:
        entity = await client.get_entity(settings.TELEGRAM_CHANNEL_USERNAME)
        await client.send_file(entity,gif_path, caption=message, schedule=timedelta(minutes=1))
        print("Message sent successfully to Telegram.")
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")
    finally:
        await client.disconnect()
