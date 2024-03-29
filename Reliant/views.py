"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, url_for, request, Flask
from Reliant import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Social Media Contact Information'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/artworks')
def artworks():
    """Renders the about page."""
    return render_template(
        'artworks.html',
        title='artworks',
        year=datetime.now().year,
        message='Your application description page.'
    )

