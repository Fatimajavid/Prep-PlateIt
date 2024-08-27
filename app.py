from flask import Flask, request, render_template, jsonify
import os
import requests

app= Flask(__name__)
# API_KEY = '6e3dc6ef9b4745839004c4d3273f84f0'
BASE_URL = 'https://api.spoonacular.com'

@app.route('/')
def home():
    return render_template('index.html')
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug=True
)