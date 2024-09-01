from django.conf import settings
from django.http import JsonResponse
from .fetchData import fetch_rows_from_sheet
from .sendToTelegram import send_message_to_telegram
from .generateMessage import generate_message
import asyncio


async def process_request(request):
    # Fetching Data from Google Sheets
    data = fetch_rows_from_sheet(settings.SHEET_ID, settings.JSON_KEYFILE_PATH,settings.SHEET_GID)
    
    if not data:
        return JsonResponse({'status': 'failed', 'message': 'No data found'})

    # Generate Message
    message = generate_message(data)
    if message is not None:
        await send_message_to_telegram(message)
    else:
        return JsonResponse({'status': 'failed', 'message': 'Failed to generate message'})

    return JsonResponse({'status': 'success', 'message': 'Generated the Post'})