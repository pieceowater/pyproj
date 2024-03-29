# cfg/__init__.py
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class ConfigVars:
    service_name: str = getenv('APP_NAME', 'The Project')
    debug: bool = getenv('APP_DEBUG', 'FALSE').upper() == 'TRUE'

    host: str = '0.0.0.0'
    port: int = 4000
