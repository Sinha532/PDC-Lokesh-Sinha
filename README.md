

# Flask Google OAuth Printing Design Tool

A Flask web application that combines Google OAuth authentication with a unique printing design pattern generator. Users can securely sign in with their Google account and create custom text patterns.

## Features

### 🔐 Google OAuth Authentication
- **Secure Login**: Users sign in using their Google account credentials
- **Session Management**: Protected routes with user session handling
- **Profile Information**: Display user name, email, and profile picture
- **Auto Logout**: Secure session termination functionality

### 🎨 Printing Design Tool
- **Pattern Generation**: Create text-based designs using "FORMULAQSOLUTIONS" as base
- **Dynamic Input**: Generate patterns with 1-100 lines of customizable output
- **Two Display Options**: View patterns on web page or print to browser console
- **Real-time Generation**: Backend processing with instant results

## How It Works

### Google Authentication Process
1. **Initial Login**: User clicks "Sign in with Google" button
2. **OAuth Flow**: Application redirects to Google's authorization server
3. **User Consent**: Google asks user to approve access permissions
4. **Token Exchange**: Google returns authorization code to callback URL
5. **User Information**: Application fetches user profile data using access token
6. **Session Creation**: User data stored in secure Flask session
7. **Dashboard Access**: User redirected to protected dashboard page

### Pattern Generation Algorithm
The printing design tool uses a sophisticated algorithm that:
1. **Takes Input**: User enters number of lines (1-100)
2. **Processes Request**: Backend `design.py` module handles pattern logic
3. **Creates Pattern**: Uses "FORMULAQSOLUTIONS" as base string
4. **Generates Design**: Creates diamond/pyramid shaped text patterns
5. **Returns Output**: Sends formatted pattern back to frontend
6. **Displays Result**: Shows pattern in terminal-style output box

## Technical Architecture

### Backend Components
- **Flask Application**: Main web server (`app.py`)
- **OAuth Integration**: Google authentication using Authlib library
- **Pattern Engine**: Separate `design.py` module for pattern generation
- **Session Management**: Secure user session handling
- **API Endpoints**: RESTful API for pattern generation requests

### Frontend Components
- **Login Page**: Google OAuth sign-in interface
- **Dashboard**: User profile and authentication success page
- **Design Tool**: Interactive pattern generation interface
- **Responsive Design**: Mobile-friendly CSS styling

### Security Features
- **Environment Variables**: Sensitive credentials stored securely
- **Session Protection**: All routes require authentication
- **HTTPS Ready**: Production-ready security configuration
- **Input Validation**: Backend validation for all user inputs

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Google Cloud Console account
- Modern web browser

### Local Development Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/Sinha532/PDC-Lokesh-Sinha.git
   cd PDC-Lokesh-Sinha
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Google OAuth**
   - Create project in Google Cloud Console
   - Enable Google+ API
   - Create OAuth 2.0 credentials
   - Add authorized redirect URI: `http://127.0.0.1:5000/callback`

4. **Set Environment Variables**
   Create `.env` file:
   ```
   GOOGLE_CLIENT_ID=your_client_id_here
   GOOGLE_CLIENT_SECRET=your_client_secret_here
   SECRET_KEY=your_secret_key_here
   ```

5. **Run Application**
   ```bash
   python app.py
   ```

6. **Access Application**
   Open `http://127.0.0.1:5000` in your browser

## File Structure

```
├── app.py                 # Main Flask application
├── design.py              # Pattern generation logic
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── .gitignore            # Git ignore rules
└── templates/
    ├── login.html        # Google sign-in page
    ├── dashboard.html    # User profile page
    └── design.html       # Pattern generation interface
```

## Dependencies

- **Flask**: Web framework for Python
- **Authlib**: OAuth authentication library
- **Requests**: HTTP client for API calls
- **Python-dotenv**: Environment variable management

## Deployment

### Vercel Deployment
The application is configured for easy deployment on Vercel:

1. **Connect GitHub**: Link your repository to Vercel
2. **Environment Variables**: Add production OAuth credentials in Vercel dashboard
3. **Automatic Deployment**: Vercel builds and deploys automatically

### Production Considerations
- Use separate Google OAuth credentials for production
- Set production redirect URI to your deployed domain
- Configure HTTPS for security
- Monitor application logs and performance


## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

**Built with Flask, Google OAuth, and creative pattern algorithms for educational and demonstration purposes.**
