# Albums Store

This project is about creating online shop of songs.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
-Python
-Flask
-If in your system there is no virtualenv, you can download it from here https://pypi.python.org/pypi/virtualenv
-curl
```

### Installing
Installing of flask:
```
$ virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.
$ flask/bin/pip install flask
```
Installing of curl
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
brew install curl
```

## Running the tests

### First part of project is Creating Users:

To create localhost let's write our first part of project: GET USERS

```
from flask import Flask, jsonify, abort, make_response, request
app = Flask(__name__)

users = [
         {
         'id': 1,
         'name': u'Kuanysh'
         },
         {
         'id': 2,
         'name': u'Yersultan'
         }
         ]

@app.route('/task1/api/v1.0/users', methods=['GET'])
def get_tasks():
    return jsonify({'users': users})

if __name__ == '__main__':
    app.run(debug=True)
```

### To run it:

```
$ chmod a+x app.py
$ ./app.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```

### To get users:

```$ curl -i http://localhost:5000//task1/api/v1.0/users
```

### To get users by id:
```
@app.route('/task1/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_task(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

```
### Call:
```
$ curl -i http://localhost:5000//task1/api/v1.0/users/1
```

If the received id is not found in the database, we will return a 404 error, which according to the HTTP means “Resource Not Found”.

### To add a new task to our database:
```
@app.route('/task1/api/v1.0/users', methods=['POST'])
def create_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'name': request.json['name']
    }
    users.append(user)
    return jsonify({'user': user}), 201
```
### Call:
```
url -i -H "Content-Type: application/json" -X POST -d '{"name":"Dariga"}' http://localhost:5000//task1/api/v1.0/users
```
users = 
        {
         'id': 3,
         'name': 'Dariga'
        }
      

### After completing this request we can get an updated task list:
users = [
         {
         'id': 1,
         'name': 'Kuanysh'
         },
         {
         'id': 2,
         'name': 'Yersultan'
         },
         {
         'id': 3,
         'name': 'Dariga'
         }
         ]

If there is no data, or the data is in place but the value of the name field is missing, then the code 400 is returned, which is used to denote “Bad Request”.

### To update or change excisting data

```
@app.route('/task1/api/v1.0/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'name' in request.json and type(request.json['name']) != str:
        abort(400)
    user[0]['name'] = request.json.get('name', user[0]['name'])

    return jsonify({'task': user[0]})
```
### Call:

```
curl -i -H "Content-Type: application/json" -X PUT -d '{"name":'Talgat'}' http://localhost:5000//task1/api/v1.0/users/2
```
users = 
        {
         'id': 2,
         'name': 'Talgat'
        }

### To delete:

```
@app.route('/task1/api/v1.0/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})
```
### Call:

```
curl -i -H "Content-Type: application/json" -X Delete -d '{"name":'Talgat'}' http://localhost:5000//task1/api/v1.0/users/3

```

users = {
         'id': 1,
         'name': 'Kuanysh'
         },
         {
         'id': 2,
         'name': 'Yersultan'
         }
         
### This is the end of first part. Now we are moving to createing categories of products and details of products.

First we need to change port number
```
app = Flask(__name__) # app.run(port=9000)
```
### To get category or prodact detail:

```
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
```
###  Now we have: http://127.0.0.1:5000/task2/api/products and http://127.0.0.1:5000/task2/api/categories

### Call for getting:

```
$ curl -i http://localhost:9000///task2/api/categories
or
$ curl -i http://localhost:9000///task2/api/products
```
### To get by id:
```
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
```


### To add a new category or product:

```
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
```
### To update:

```
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
```
### To delete:

```
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
```
### This is end of second part.
