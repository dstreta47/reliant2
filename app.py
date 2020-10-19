"""
This script runs the Reliant application using a development server.
"""
import os
from os import environ
from Reliant import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    app.run(host='0.0.0.0', port=port)
