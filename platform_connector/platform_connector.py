import MetaTrader5 as mt5
import os
from dotenv import load_dotenv, find_dotenv

class PlatformConnector():
    def __init__(self):
        # find and load .env file
        load_dotenv(find_dotenv())

        # platform initialization
        self._initialize_platform()

        # checking the account type
        self._live_account_warning()
    
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

    def _live_account_warning(self) -> None:
        # Method that access the account info
        account_info = mt5.account_info()

        # Check the type of the account
        if account_info.trade_mode == mt5.ACCOUNT_TRADE_MODE_DEMO:
            print('Demo Account Detected')
        elif account_info.trade_mode == mt5.ACCOUNT_TRADE_MODE_REAL:
            if not input('Real Account Detected --- Continue? (y/n)').lower() == 'y':
                mt5.shutdown()
                raise Exception('The user has stopped the program by typing not to continue the Real Account conection')
        else:
            print('Challenge Account Detected')

            
