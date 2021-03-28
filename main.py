from flask import Flask

main = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    print("from main")
main.run()