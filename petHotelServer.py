from flask import Flask, request, jsonify
from connectionFunction import conn
# import psycopg2 
# import psycopg2.extras 

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/pets', methods=['GET','POST'])
def getPost():
    if (request.method == 'POST'):
        cur = conn.cursor()
        data = request.form
        queryText = 'INSERT INTO "pet" ("owner_id", "pet_name", "breed", "color") VALUES (%s, %s, %s, %s);'
        cur.execute(queryText, (data['ownerId'], data['petName'], data['petBreed'], data['petColor'] ,))
        conn.commit()
        cur.close()
        return f"posted {(data['petName'])}", 201
    elif (request.method == 'GET'):
        cur = conn.cursor()
        cur.execute("SELECT * FROM pet;")
        records = cur.fetchall()
        print(records)
        cur.close()
        return jsonify(records), 201

        # if (request.method == 'POST'):
        # data = request.form
        # # print(owner_name)
        # cur = con.cursor()
        # queryInsertText = "insert into owners (name) values (%s);"
        # cur.execute(queryInsertText, (data["name"], ))
        # con.commit()
        # cur.close()
        # return jsonify(data["name"]), 201


@app.route('/pets/<id>', methods=['PUT', 'DELETE'])
def putDelete(id):
    if (request.method == 'PUT'):
        cur = conn.cursor()
        # check-in/-out put request
        inOrOut = request.form["check"]
        if (inOrOut == 'in'):
            # inOrOut = "we're checking in"
            queryText = 'UPDATE "pet" SET "checked_in" = TRUE WHERE id = %s;'
            cur.execute(queryText, (id))
            conn.commit()
            cur.close()
            return "checked in!", 200
        elif (inOrOut == 'out'):
            # inOrOut = "we're checking out"
            queryText = 'UPDATE "pet" SET "checked_in" = FALSE WHERE id = %s;'
            cur.execute(queryText, (id))
            conn.commit()
            cur.close()
            return "checked out!", 200
        # return f"checked {}!" + id

    elif (request.method == 'DELETE'):
        cur = conn.cursor()
        petId = id
        queryText = (f'DELETE FROM "pet" WHERE id = {petId} RETURNING "pet".pet_name;')
        cur.execute(queryText)
        petName = cur.fetchall()
        petName = petName[0]
        print("printing our thing")
        print(petName['pet_name'])
        # conn.commit()
        cur.close()
        return jsonify(petName), 200
    # elif ()

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




