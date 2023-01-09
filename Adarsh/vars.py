# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID',"3369707"))
    API_HASH = str(getenv('API_HASH',"aec1fd7abdfec322c426961a570ef336"))
    BOT_TOKEN = str(getenv('BOT_TOKEN',"5726328717:AAFziqmaN24ns07g2KEUUdvV0j5-Fhu4OU0"))
    name = str(getenv('name', "filetolinkbot"))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', "60"))
    WORKERS = int(getenv('WORKERS', "4"))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL',"-1001666406019"))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', "18.117.98.198"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1115053159").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME',"Crazy_Phoenix"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN','18.117.98.198:8080')) if not ON_HEROKU or getenv('FQDN','18.117.98.198:8080') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL',"mongodb+srv://beast06king:beastking@cluster0.hgxilfg.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL',"AMD_LinkZz"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
