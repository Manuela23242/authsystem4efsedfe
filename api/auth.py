from flask import Flask, request, redirect, render_template
import requests
import os

app = Flask(__name__)

CLIENT_ID = os.getenv('CLIENT_ID', '1332407176970502194')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', 'rFQmcF-Wl6Q1o96HKf646S8wElg0dYI3')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'https://authsystem4efsedfe.vercel.app/api/auth')

@app.route('/api/auth')
def auth_callback():
    code = request.args.get('code')
    if not code:
        return render_template('callback.html', success=False, error="No authorization code received")
    
    # Token exchange
    data = {
        'client_id': 1332407176970502194_ID,
        'client_secret': rFQmcF-Wl6Q1o96HKf646S8wElg0dYI3,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify guilds.join'
    }
    
    try:
        response = requests.post('https://discord.com/api/oauth2/token', data=data)
        response.raise_for_status()
        tokens = response.json()
        
        # Get user info
        user_response = requests.get(
            'https://discord.com/api/users/@me',
            headers={'Authorization': f'Bearer {tokens["access_token"]}'}
        )
        user_data = user_response.json()
        
        return render_template('callback.html', 
                             success=True,
                             username=user_data.get('username'),
                             user_id=user_data.get('id'))
    
    except Exception as e:
        return render_template('callback.html', 
                             success=False,
                             error=str(e))

@app.route('/')
def index():
    return redirect('https://your-discord-invite.gg')  # Redirect to your Discord
