from flask import Flask, render_template, request, jsonify, url_for, send_from_directory
from datetime import datetime
import config
import json
import os
from dotenv import load_dotenv
from flask_talisman import Talisman
from flask_mail import Mail, Message

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load configuration from config.Config
app.config.from_object(config.Config)

mail = Mail(app)


# Configuring Talisman with HSTS enabled
# https://pypi.org/project/flask-talisman/
csp = {
    'default-src': ["'self'"],
    'script-src': ["'self'", "https://stackpath.bootstrapcdn.com", "https://www.youtube.com", 
                   "https://cdnjs.cloudflare.com", "https://cdn.jsdelivr.net", 
                   "https://www.googletagmanager.com", "https://googleads.g.doubleclick.net",
                   "https://www.googleadservices.com"],
    'style-src': ["'self'", "'unsafe-inline'", "https://stackpath.bootstrapcdn.com", 
                  "https://cdnjs.cloudflare.com", "https://netdna.bootstrapcdn.com", 
                  "https://fonts.googleapis.com", "https://cdn.jsdelivr.net"],
    'font-src': ["'self'", "https://stackpath.bootstrapcdn.com", "https://netdna.bootstrapcdn.com", 
                 "https://fonts.gstatic.com", "https://cdnjs.cloudflare.com"],
    'img-src': ["'self'", "https://www.youtube.com", "data:", "https://www.google.com", 
                "https://www.google.ca", "https://googleads.g.doubleclick.net"],
    'connect-src': ["'self'", "https://cb-server-production.up.railway.app"],
    'frame-src': ["'self'", "https://www.youtube.com", "https://td.doubleclick.net"], 
    'object-src': ["'none'"],
    'media-src': ["'self'"]
}
talisman = Talisman(
    app,
    frame_options=None,
    force_https=True,
    strict_transport_security_include_subdomains=True,
    strict_transport_security_max_age=31536000,
    content_security_policy=csp,
    content_security_policy_nonce_in=['script-src', 'style-src']
)

# Enable debug mode
app.debug = False

# Initializations
current_year = datetime.now().year

@app.route('/')
def index():
    current_route = request.path
    return render_template('index.html', current_route=current_route, 
                                            current_year=current_year)


@app.route('/static/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('static/js', filename, mimetype='application/javascript')



if __name__ == '__main__':
    app.run(debug=False)