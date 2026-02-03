import requests
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

SERVER_URL = f"http://{os.getenv('SERVER_IP', 'localhost')}:{os.getenv('SERVER_PORT', '8900')}/"

if __name__ == '__main__':
    try:
        response = requests.post(SERVER_URL, data='heartbeat')
        print('Server response:', response.text)
    except Exception as e:
        print('Failed to send heartbeat:', e)
