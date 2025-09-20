Based on the project files and information gathered, here's a comprehensive README.md file for your Flask Google OAuth Printing Design Tool:

# Flask Google OAuth Printing Design Tool

A secure web application that combines Google OAuth 2.0 authentication with a powerful text pattern generator. Users authenticate with their Google accounts and gain access to an interactive pattern design tool that creates ASCII art using the "FORMULAQSOLUTIONS" algorithm.

## 🚀 Features

### 🔐 Google OAuth Authentication
- **Secure Login**: OAuth 2.0 implementation using Google's authentication service
- **User Session Management**: Persistent login sessions with secure session handling
- **Profile Integration**: Displays user's Google profile picture, name, and email
- **Protected Routes**: All design tools require authentication

### 🎨 Pattern Design Tool
- **Dynamic Pattern Generation**: Creates ASCII art patterns based on user input
- **FORMULAQSOLUTIONS Algorithm**: Uses a sophisticated algorithm that generates expanding and contracting text patterns
- **Flexible Input**: Accepts any number between 1-100 lines for pattern generation
- **Dual Output Options**: 
  - **Web Display**: Shows patterns in a terminal-style interface
  - **Console Output**: Prints patterns to browser developer console

### 📱 Modern UI/UX
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Glass Morphism**: Modern UI with backdrop blur effects and transparent elements
- **Real-time Feedback**: Loading states and error handling for better user experience
- **Centered Layout**: Clean, professional interface matching authentication flow

## 🏗️ Technical Architecture

### Backend (Flask)
```
├── app.py              # Main Flask application with OAuth routes
├── design.py           # Pattern generation algorithm
├── requirements.txt    # Python dependencies
└── vercel.json        # Deployment configuration
```

### Frontend
```
├── templates/
│   ├── login.html     # Google OAuth login page
│   ├── dashboard.html # User welcome dashboard
│   └── design.html    # Pattern generation interface
```

### Core Technologies
- **Flask**: Python web framework for backend API
- **Authlib**: OAuth 2.0 client implementation
- **Google OAuth 2.0**: Secure authentication provider
- **JavaScript**: Frontend interactivity and API calls
- **CSS3**: Modern styling with glassmorphism effects

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google Cloud Console account
- Git for version control

### 1. Clone Repository
```bash
git clone https://github.com/Sinha532/PDC-Lokesh-Sinha.git
cd PDC-Lokesh-Sinha
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Google OAuth Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select existing one
3. Enable Google+ API
4. Create OAuth 2.0 credentials (Web Application)
5. Add authorized origins: `http://127.0.0.1:5000`
6. Add redirect URIs: `http://127.0.0.1:5000/callback`

### 4. Environment Configuration
Create `.env` file:
```bash
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
SECRET_KEY=your_secret_session_key
```

### 5. Run Application
```bash
python app.py
```
Visit: `http://127.0.0.1:5000`

## 🎯 How It Works

### Authentication Flow
1. **Login Page**: Users see Google Sign-in button
2. **OAuth Redirect**: Clicking redirects to Google's authentication server
3. **User Consent**: Google asks for permission to share profile information
4. **Token Exchange**: Application receives authorization code and exchanges for access token
5. **Profile Retrieval**: Fetches user's email, name, and profile picture
6. **Session Creation**: Stores user data in secure Flask session
7. **Dashboard Redirect**: Successful authentication leads to welcome dashboard

### Pattern Generation Algorithm
The `design.py` module implements a sophisticated pattern generation system:

```python
def print_design(n):
    base = "FORMULAQSOLUTIONS"
    # Creates patterns using mathematical algorithms for:
    # - Odd numbers: Symmetric diamond shapes
    # - Even numbers: Expanded patterns with n+1 total lines
    # - Dynamic spacing and character repetition
```

#### Pattern Examples:
- **21 lines**: Creates full "FORMULAQSOLUTIONS" diamond pattern
- **16 lines**: Generates abbreviated pattern ending with "S"
- **Custom sizes**: Adapts algorithm for any input 1-100

### API Endpoints
- `GET /`: Login page with Google OAuth button
- `GET /login`: Initiates Google OAuth flow
- `GET /callback`: Handles OAuth callback and token exchange
- `GET /dashboard`: Protected user welcome page
- `GET /design`: Pattern generation interface
- `POST /generate-pattern`: API endpoint for pattern creation
- `GET /logout`: Clears session and redirects to login

## 🚀 Deployment

### Vercel Deployment
The application is configured for serverless deployment on Vercel:

1. **Connect GitHub**: Link repository to Vercel dashboard
2. **Environment Variables**: Set production OAuth credentials in Vercel settings
3. **Automatic Deployment**: Pushes to main branch trigger automatic deployments

### Production OAuth Setup
- **Production Credentials**: Create separate Google Cloud project for production
- **Domain Configuration**: Update redirect URIs to production domain
- **HTTPS Enforcement**: Production uses HTTPS for secure OAuth flow

## 🔒 Security Features

- **OAuth 2.0 Compliance**: Follows Google's security best practices
- **Session Security**: Uses Flask's secure session management
- **Environment Variables**: Sensitive credentials stored securely
- **Route Protection**: Authentication required for all design features
- **HTTPS Ready**: Configured for secure production deployment

## 🎨 Pattern Algorithm Details

The FORMULAQSOLUTIONS algorithm creates text-based designs through:

1. **Base String Processing**: Uses "FORMULAQSOLUTIONS" as foundation
2. **Mathematical Progression**: Calculates character positions using formulas
3. **Dynamic Spacing**: Centers patterns with calculated whitespace
4. **Line Distribution**: Handles both odd/even input numbers differently
5. **Character Repetition**: Repeats substrings based on line position

This creates visually appealing ASCII art patterns that scale dynamically with user input, making each generated design unique while maintaining aesthetic consistency.

## 📝 License

This project is developed as part of a Python Development Challenge (PDC) and serves as a demonstration of modern web authentication integrated with algorithmic design generation.

***

**Assessment Submission Repository as Python Development Challenge BreadWinner** - A secure, modern web application showcasing OAuth integration and algorithmic pattern generation.

[5](https://docs.replit.com/additional-resources/google-auth-in-flask)
[6](https://dev.to/revisepdf/how-i-implemented-google-oauth-in-my-flask-application-with-supabase-6ke)
[7](https://stackoverflow.com/questions/9499286/using-google-oauth2-with-flask)
