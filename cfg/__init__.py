# cfg/__init__.py
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class ConfigVars:
    secret_key: str = getenv('APP_SECRET_KEY')
    service_name: str = getenv('APP_NAME', 'The Project')
    debug: bool = getenv('APP_DEBUG', 'FALSE').upper() == 'TRUE'

    host: str = '0.0.0.0'
    port: int = 4000

    __db_host: str = getenv('APP_DB_HOST', 'localhost')
    __db_port: int = getenv('APP_DB_PORT')
    __db_name: int = getenv('APP_DB_NAME', 'postgres')
    __db_user: str = getenv('APP_DB_USER', 'postgres')
    __db_pass: str = getenv('APP_DB_PASS', 'root')

    db_conn_str: str = (
        f"postgresql://{__db_user}:{__db_pass}@{__db_host}"
        f"{f':{__db_port}' if __db_port else ''}"
        f"/{__db_name}"
    )

