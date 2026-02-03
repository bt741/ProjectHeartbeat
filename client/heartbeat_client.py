import requests

SERVER_URL = 'http://localhost:8080/'

if __name__ == '__main__':
    try:
        response = requests.post(SERVER_URL, data='heartbeat')
        print('Server response:', response.text)
    except Exception as e:
        print('Failed to send heartbeat:', e)
