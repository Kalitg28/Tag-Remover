import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', True))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', None))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
else:
    # Fill the Values
    API_ID = ""
    API_HASH = ""
    BOT_TOKEN = ""
