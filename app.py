import os
from datetime import datetime
from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from authlib.integrations.flask_client import OAuth
import requests
from dotenv import load_dotenv
from design import generate_pattern_response

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Production-ready secret key
app.secret_key = os.getenv('SECRET_KEY') or os.urandom(24)

# OAuth Setup
oauth = OAuth(app)

google = oauth.register(
    name='google',
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
    access_token_url='https://oauth2.googleapis.com/token',
    client_kwargs={'scope': 'email profile'}
)

@app.route('/')
def index():
    """Home page with Google sign-in option"""
    return render_template('login.html')

@app.route('/login')
def login():
    """Initiate Google OAuth login"""
    redirect_uri = url_for('callback', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/callback')
def callback():
    """Handle Google OAuth callback"""
    try:
        token = google.authorize_access_token()
        resp = requests.get(
            'https://www.googleapis.com/oauth2/v2/userinfo',
            headers={'Authorization': f'Bearer {token["access_token"]}'}
        )
        
        if resp.status_code == 200:
            user_info = resp.json()
            session['user'] = {
                'email': user_info.get('email'),
                'name': user_info.get('name'),
                'picture': user_info.get('picture', ''),
                'login_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')
            }
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('index'))
    except Exception as e:
        app.logger.error(f"OAuth callback error: {e}")
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    """Protected dashboard page"""
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/design')
def design():
    """Design page after successful authentication"""
    if 'user' not in session:
        return redirect(url_for('index'))
    return render_template('design.html', user=session['user'])

@app.route('/generate-pattern', methods=['POST'])
def generate_pattern():
    """API endpoint to generate pattern from backend"""
    if 'user' not in session:
        return jsonify({'success': False, 'error': 'Authentication required'}), 401
    
    try:
        data = request.get_json()
        n = data.get('lines', 0)
        result = generate_pattern_response(n)
        return jsonify(result)
    except Exception as e:
        return jsonify({'success': False, 'error': f'Server error: {str(e)}'}), 500

@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.pop('user', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)
