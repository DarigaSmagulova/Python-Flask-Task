#!flask/bin/python
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

@app.route('/task1/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_task(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

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

@app.route('/task1/api/v1.0/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
