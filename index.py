
from flask import Flask, request, make_response

app = Flask(__name__)

koders = [
    { 'name': 'mike'},
    { 'name': 'charles' },
    { 'name': 'lucho' }
]

@app.route('/')
def hola_mundo():
    return {
        'message': 'hola mundo'
    }

@app.route('/koders')
def get_koders():
    return {
        'koders': koders
    }

@app.route('/koders', methods=['POST'])
def create_koder():
    data = request.json
    koders.append({ 'name': data['name'] })
    return {
        'message': 'koder created',
        'koders': koders
    }

## /koders/loquesea
# /koders/charles
# /koders/lucho
# /koders/noexisto
@app.route('/koders/<name>', methods=['DELETE'])
def delete_koder(name):
    if { 'name': name } in koders:
        koders.remove({ 'name': name })
    else:
        return make_response(
            { 'message': f'{name} does not exists' },
            404
        )

    return {
        'message': 'koder deleted',
        'koders': koders
    }
