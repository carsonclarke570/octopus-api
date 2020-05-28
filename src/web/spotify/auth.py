import requests

def get_tokens(client_id, client_secret, code):
    url = 'https://accounts.spotify.com/api/token'
    body = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:5000/',
        'client_id': client_id,
        'client_secret': client_secret
    }
    req = requests.post(url, data=body)
    resp = req.json()
    
    return resp['access_token'], resp['refresh_token']