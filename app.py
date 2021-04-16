from flask import Flask , request
from facedetctor import hello
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home',methods = ['GET','POST'])
def main():
    print("main k andar aaya!!!!!!!")
    d={}
    d['doc']= str(request.args['doc'])
    d['frame1']= str(request.args['frame1'])
    d['frame2']= str(request.args['frame2'])
    d['frame3']= str(request.args['frame3'])
    # d['frame5']= str(request.args['frame5'])
    value = hello(d['doc'], d['frame1'], d['frame2'], d['frame3'])
    print("Final validation is ", value)
    response = {'value': value}
    return response

if __name__ == "__main__":
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
