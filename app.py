from flask import Flask, request

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def entry_point():
    #return "hello"
    if request.method == 'POST':
        #response = getSamsResponse()
        return 'this should be sams response'
    elif request.method == 'GET':
        return 'Hello and Welcome, User'

if __name__ == '__main__':
    app.run()