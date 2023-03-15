import boto3
import random
from flask import Flask, render_template

app = Flask(__name__)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyTable2')

@app.route('/')
def index():
    response = table.scan()
    fortunes = response['Items']
    random_fortune = random.choice(fortunes)['fortune']
    return render_template('index.html', fortune=random_fortune)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
