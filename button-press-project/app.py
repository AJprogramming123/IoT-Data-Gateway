from flask import Flask, render_template
import boto3
from collections import Counter

app = Flask(__name__)

# DynamoDB setup
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('arduino-button')

@app.route('/')
def home():
    return "Flask running — go to /chart"

@app.route('/chart')
def chart():
    response = table.scan()
    items = response.get('Items', [])
    print("Raw items:", items)
    
    # Extract nested button values
    buttons = [int(item['payload']['button']) for item in items if 'payload' in item and 'button' in item['payload']]
    print("Extracted buttons:", buttons)
    
    counts = Counter(buttons)
    labels = [f"Button {b}" for b in counts.keys()]
    values = list(counts.values())
    
    print("Labels:", labels)
    print("Values:", values)
    
    return render_template('chart.html', labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug=True)

