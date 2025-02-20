from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1> Welcome Flask APP!!!</h1>'

@app.route('/post/', methods=['GET'])
def post_method():
        return "<h1> POST MENTIONED IT IS GET METHOD CALL !!! </h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

