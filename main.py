import logging
from flask import Flask, request
from waitress import serve
from splunk_otel.tracing import start_tracing

start_tracing(
    service_name='creditprocessorservice',
    resource_attributes={
        'service.version': '3.1'
    })

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

@app.route('/test')
def test_it():
    return 'OK'
    
@app.route('/credit_check_ok')
def credit_check_ok():
    location = request.args.get('location')
    if credit_check_passes(location):
        return 'YES'
    else:
        return 'NO'

@app.route('/get_credit_score')
def get_credit_score():
    location = request.args.get('location')
    credit_score = get_credit_score_by_location(location)
    return str(credit_score)

def get_credit_score_by_location(location):
    if location == 'USA':
        return 750
    elif location == 'Canada':
        return 800
    elif location == 'England':
        return 850
    elif location == 'France':
        return 550
    else:
        return 700

def credit_check_passes(location):
    if location == 'France':
        return False

if __name__ == '__main__':
    serve(app, port=8899)
