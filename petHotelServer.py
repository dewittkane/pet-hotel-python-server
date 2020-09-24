from flask import Flask, request, jsonify

from connectionFunction import conn

import psycopg2 
import psycopg2.extras 


conn = psycopg2.connect("dbname=pet_hotel user=emersonaagaard", cursor_factory=psycopg2.extras.RealDictCursor)

app = Flask(__name__)

@app.route('/pets', methods=['GET','POST'])
def getPost():
    if (request.method == 'POST'):
        request.form
    elif (request.method == 'GET'):
        cur = conn.cursor()
        cur.execute("SELECT * FROM pet;")
        records = cur.fetchall()
        print(records)
        cur.close()
        return jsonify(records), 201


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




