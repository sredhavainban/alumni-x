# AlumniX - Alumni Networking Platform

A modern, professional alumni networking platform built with Flask.

## Features

- **20 Registration Numbers**: Simple login with registration numbers 23129001-23129020
- **Beautiful UI**: Modern glass morphism design with gradient backgrounds
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **No Database Required**: Lightweight application with pre-defined user data
- **Professional Dashboard**: Statistics, skills display, and connection suggestions

## Quick Start

### Local Development

1. **Install Python 3.11+**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **Open browser:** http://localhost:5000

### Available Registration Numbers

Use any of these numbers to login:
- 23129001 to 23129020

## Deployment Options

### Option 1: Heroku (Recommended)

1. **Install Heroku CLI**
2. **Login to Heroku:**
   ```bash
   heroku login
   ```
3. **Create Heroku app:**
   ```bash
   heroku create your-alumnix-app
   ```
4. **Deploy:**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push heroku main
   ```

### Option 2: Railway

1. **Connect your GitHub repository to Railway**
2. **Railway will automatically detect Flask and deploy**
3. **Set environment variables if needed**

### Option 3: Render

1. **Connect your GitHub repository to Render**
2. **Create a new Web Service**
3. **Set build command:** `pip install -r requirements.txt`
4. **Set start command:** `python app.py`

### Option 4: Python Anywhere

1. **Upload files to PythonAnywhere**
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure WSGI file**
4. **Reload web app**

## Project Structure

```
alumniX_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Heroku deployment config
├── runtime.txt           # Python version
├── README.md             # This file
└── templates/
    ├── login.html        # Login page
    ├── main.html         # Dashboard
    ├── logout.html       # Logout page
    └── registration_numbers.html  # Registration numbers list
```

## Features

- **Modern Design**: Glass morphism effects, gradients, animations
- **Responsive**: Works on all devices
- **Fast**: No database queries, instant loading
- **Secure**: Session-based authentication
- **Professional**: Clean, modern UI/UX

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design patterns
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## License

This project is open source and available under the MIT License. 