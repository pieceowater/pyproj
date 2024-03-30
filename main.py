# main.py
from dotenv import load_dotenv
from api import app
from cfg import ConfigVars as conf

if __name__ == '__main__':
    load_dotenv()

    app.run(
        host=conf.host,
        port=conf.port,
        debug=conf.debug,
        load_dotenv=True
    )
