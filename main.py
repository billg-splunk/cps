import logging
from flask import Flask, request
from waitress import serve

app = Flask(__name__)

@app.route('/test')
def test_it():
    return 'OK'
    
@app.route('/getScore')
def get_credit_score():
    customernum = request.args.get('customernum')
    # Last number =
    # 0-5 = Normal
    # 6, 7, 8 = Feature Flags
    # 9 = HipsterCard txns
    # Issues/Processes:
    # - Errors on feature flag 7 or credit scores not between 300-850
    # - Delays on transactions where credit score is 300-670
    # - HipsterCard txns will have a callout to another 3rd party inferred service

    score = random.randrage(250, 850, 1)
    if score < 300:
        score = -1

    #credit_score = get_credit_score_by_location(location)
    return str(score)

#def addDelays(customernum):


if __name__ == '__main__':
    serve(app, port=8899)
