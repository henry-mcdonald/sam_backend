from flask import Flask, request
from samlogic import get_response

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def entry_point():
    #return "hello"
    if request.method == 'POST':
        #response = getSamsResponse()

        return(request.form.get('userinput'))
        #return get_response(request.form.get('userinput'))
    elif request.method == 'GET':
        return 'Hello and Welcome, User'

if __name__ == '__main__':
    app.run()