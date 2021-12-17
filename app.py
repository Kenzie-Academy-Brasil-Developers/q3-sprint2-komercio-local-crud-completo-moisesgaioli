from flask import Flask, json, jsonify, request

produtos = [
    {"id": 1, "name": "sabonete", "price": 5.99},
    {"id": 2, "name": "perfume", "price": 39.90},
    {"id": 3, "name": "tapete", "price": 10.30},
    {"id": 4, "name": "tunica", "price": 19.29},
    {"id": 5, "name": "chuveiro", "price": 119.19},
    {"id": 6, "name": "arroz", "price": 30.10},
    {"id": 7, "name": "oleo de cozinha", "price": 11.15},
    {"id": 8, "name": "carne moida", "price": 39.90},
    {"id": 9, "name": "bola", "price": 25.99},
    {"id": 10, "name": "cantil", "price": 55.99},
    {"id": 11, "name": "copo", "price": 5.99},
    {"id": 12, "name": "panela", "price": 25.99},
    {"id": 13, "name": "prato", "price": 10.99},
    {"id": 14, "name": "açucar", "price": 7.99},
    {"id": 15, "name": "sal", "price": 5.99},
    {"id": 16, "name": "pipoca", "price": 3.14},
    {"id": 17, "name": "sabonete", "price": 5.99},
    {"id": 18, "name": "miojo", "price": 2.39},
    {"id": 19, "name": "alface", "price": 3.99},
    {"id": 20, "name": "tomate", "price": 9.99},
    {"id": 21, "name": "macarrao", "price": 6.40},
    {"id": 22, "name": "mesa", "price": 115.99},
    {"id": 23, "name": "cadeira gamer", "price": 445.99},
    {"id": 24, "name": "mouse gamer", "price": 215.99},
    {"id": 25, "name": "tv", "price": 995.99},
    {"id": 26, "name": "liquidificador", "price": 65.99},
    {"id": 27, "name": "furadeira", "price": 99.15},
    {"id": 28, "name": "ferro de passar", "price": 55.80},
    {"id": 29, "name": "coberta", "price": 55.99},
    {"id": 30, "name": "sofa", "price": 600.15}
]

app = Flask(__name__)

@app.get('/products')
def list_products():
    return jsonify(produtos), '200 - OK'


@app.get('/products/<product_id>')
def get(product_id: int):
    product_filtred = [produto for produto in produtos if produto['id'] == int(product_id)]
    return jsonify(product_filtred), 200


@app.post('/products')
def create():
    new_product = {'id': 31, 'name': request.json['name'], 'price': request.json['price']}
    produtos.append(new_product)
    return jsonify(new_product), '201 - CREATED'


@app.patch('/products/<product_id>')
def update(product_id: int):
    name = ''
    price = ''    
    product_filtred = [produto for produto in produtos if produto['id'] == int(product_id)]

    if name and price:
        product_edited = {'id': product_filtred[0]['id'], 'name': name, 'price': price}
         
    elif price:
        product_edited = {'id': product_filtred[0]['id'], 'name': product_filtred[0]['name'], 'price': price}
        
    elif name:
        product_edited = {'id': product_filtred[0]['id'], 'name': name, 'price': product_filtred[0]['price']}
        
    return {}, '204 - NO CONTENT'


@app.delete('/products/<product_id>')
def delete(product_id: int):
    product_filtred = [produto for produto in produtos if produto['id'] == int(product_id)]
    produtos.remove(product_filtred[0])
    return {}, '204 - NO CONTENT'