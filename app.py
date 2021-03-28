from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Store', 'items':[
            {
                'name':'chair','price':1500
            }
        ]
    }
]



#POST /store -> name
@app.route('/store',methods=['POST'])
def create_store():
    data = request.get_json()
    store = {
        'name':data['name'], 'items': []
        }
    stores.append(store)
    return store



#GET /store/<name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'Not found'})



#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})



#POST /store/<name>/item -> name, price
@app.route('/store/<string:name>/item',methods=['POST'])
def post_item(name):
    data = request.get_json()
    for store in stores:
        if store['name'] == name:
            item = {
                'name': data['name'], 'price': data['price']
            }
    store['items'].append(item)
    return jsonify(item)

    return jsonify({'message':'Not found'})



#GET /store/<name>/item
@app.route('/store/<string:name>/item')
def get_item(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message':'Not found'})

@app.route('/')
def index():
    return 'Баю бай засыпай шелли попадает в рай'

if __name__ == '__main__':
    print("from main")
app.run(debug=True)
###
