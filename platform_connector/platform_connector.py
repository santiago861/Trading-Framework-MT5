import MetaTrader5 as mt5
import os
from dotenv import load_dotenv, find_dotenv

class PlatformConnector():
    def __init__(self):
        # find and load .env file
        load_dotenv(find_dotenv())

        # platform initialization
        self._initialize_platform()
    
    def _initialize_platform(self) -> None:
        if mt5.initialize(
            path = os.getenv('MT5_PATH'),
            login = int(os.getenv('MT5_LOGIN')),
            password = os.getenv('MT5_PASSWORD'),
            server = os.getenv('MT5_SERVER'),
            timeout = int(os.getenv('MT5_TIMEOUT')),
            portable = eval(os.getenv('MT5_PORTABLE'))
        ):
            print('Platform successfully launched')
        else:
            raise Exception(f'Something went wrong launching the platform: {mt5.last_error()}')