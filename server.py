from flask import Flask
from flask import session, redirect, url_for, render_template, Response, request
import json 
from urllib.parse import urlencode, quote_plus

app = Flask(__name__)

@app.route('/api/nf/balance', methods=['POST'])
def balance():
    content = request.json
    bln =  {
        "101010":'10',
        "202020":'20',
        "303030":'30',
        "404040":'40',
        "505050":'50'}.get(content["account"],'0')
    return Response(json.dumps({"amount":bln}), content_type='appication/json')

@app.route('/api/nf/get_account', methods=['POST'])
def get_account():
    content = request.json
    res =  {
        "authsaz1":{'status':'1', 'account':['101010','202020']},
        "authsaz2":{'status':'1', 'account':['303030']},
        "authsaz3":{'status':'1', 'account':['404040','505050']}}.get(content["username"],{'status':'0'})
    return Response(json.dumps(res), content_type='appication/json')

@app.route('/api/f/transfer', methods=['POST'])
def transfer():
    content = request.json
    res =  {
        "Result":'Successfull transfer ' + content['amount'] + ' Dollars, From: ' 
           + content['account'] + ' to ' + content['account2']
        }
    return Response(json.dumps(res), content_type='appication/json')
    
run = {
    "debug": True,
    "port": 7001,
    "host": '0.0.0.0',
    "threaded": True
}

if __name__== "__main__":
   app.run(debug=run["debug"], threaded=run["threaded"], host=run["host"], port=run["port"])
