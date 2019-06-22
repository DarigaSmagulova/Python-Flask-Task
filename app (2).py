from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)
# app.run(port=8000)

categories = [
            {
            'id': 1,
            'title': u'Russion'
            },
            {
            'id': 2,
            'title': u'Hip-Hop/RnB'
            },
            {
            'id': 3,
            'title': u'RAP'
            },
            {
            'id': 4,
            'title': u'Soul'
            }
    ]

products = [
              {
              'id': 1,
              'title': u'8 mesyacev v Vegase',
            'artist': u'zoloto',
            'category': u'Russion'
              },
              {
              'id': 2,
              'title': u'Testing',
            'artist': u'ASAP Rocky',
            'category': u'RAP'
              },
              {
              'id': 3,
              'title': u'IGOR',
            'artist': u'Tyler, the Creator',
            'category': u'RAP'
              },
              {
              'id': 4,
              'title': u'Blonde',
            'artist': u'Frank Ocean',
            'category': u'Soul'
              }
              ]
#GET C
@app.route('/task2/api/categories', methods=['GET'])
def get_categories():
    return jsonify({'categories': categories})

#GET P
@app.route('/task2/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})
#GET C id
@app.route('/task2/api/categories/<int:categories_id>', methods=['GET'])
def get_category(categories_id):
    category = list(filter(lambda x: x['id'] == categories_id, categories))
    if len(category) == 0:
        abort(404)
    return jsonify({'category': category[0]})
#GET P id
@app.route('/task2/api/products/<int:products_id>', methods=['GET'])
def get_product(products_id):
    product = list(filter(lambda x: x['id'] == products_id, products))
    if len(product) == 0:
        abort(404)
    return jsonify({'product': product[0]})
#POST C
@app.route('/task2/api/categories', methods=['POST'])
def create_category():
    if not request.json or not 'title' in request.json:
        abort(400)
    category = {
        'id': categories[-1]['id'] + 1,
        'title': request.json['title']
    }
    categories.append(category)
    return jsonify({'category': category}), 201
#POST P
@app.route('/task2/api/products', methods=['POST'])
def create_product():
    if not request.json or not 'title' in request.json:
        abort(400)
    product = {
        'id': products[-1]['id'] + 1,
        'title': request.json['title'],
        'artist': request.json.get('artist', ""),
        'category': request.json.get('category', "")
    }
    products.append(product)
    return jsonify({'product': product}), 201
#PUT C
@app.route('/task2/api/categories/<int:categories_id>', methods=['PUT'])
def update_category(categories_id):
    category = list(filter(lambda x: x['id'] == categories_id, categories))
    if len(category) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(404)
    categories[0]['title'] = request.json.get('title', category[0]['title'])
    return jsonify({'category': category[0]})
#PUT P
@app.route('/task2/api/products/<int:products_id>', methods=['PUT'])
def update_product(products_id):
    product = list(filter(lambda x: x['id'] == products_id, products))
    if len(product) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(404)
    if 'artist' in request.json and type(request.json['artist']) != str:
        abort(404)
    if 'category' in request.json and type(request.json['category']) != str:
        abort(404)
    products[0]['title'] = request.json.get('title', product[0]['title'])
    products[0]['artist'] = request.json.get('artist', product[0]['artist'])
    products[0]['category'] = request.json.get('category', product[0]['category'])
    return jsonify({'product': product[0]})

#DELETE C
@app.route('/task2/api/categories/<int:categories_id>', methods=['DELETE'])
def delete_category(categories_id):
    category = list(filter(lambda x: x['id'] == categories_id, categories))
    if len(category) == 0:
        abort(404)
    categories.remove(category[0])
    return jsonify({'result': True})
#DELETE P
@app.route('/task2/api/products/<int:products_id>', methods=['DELETE'])
def delete_product(products_id):
    product = list(filter(lambda x: x['id'] == products_id, products))
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
