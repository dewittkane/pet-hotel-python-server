from flask import Flask, request

app = Flask(__name__)

@app.route('/pets', methods=['GET','POST'])
def getPost():
    if (request.method == 'POST'):
       request.form
    elif (request.method == 'GET'):
        return 'GET pie', 201
    
@app.route('/pets/<id>', methods=['PUT', 'DELETE'])
def putDelete(id):
    if (request.method == 'PUT'):
        return request.form["pie"] + id
    elif (request.method == 'DELETE'):
        # return request.args.get('pets')
        return id

@app.route('/owner', methods=['GET','POST'])
def getPostOwner():
    if (request.method == 'POST'):
       request.form
    elif (request.method == 'GET'):
        return 'GET pie', 201
    
@app.route('/owner/<id>', methods=['PUT', 'DELETE'])
def putDeleteOwner(id):
    if (request.method == 'PUT'):
        return request.form["pie"] + id 
    elif (request.method == 'DELETE'):
        # return request.args.get('pets')
        return id


