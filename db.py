from flask import Flask, request, jsonify
import mysql.connector as con
#import logging
#from log import log_file
import pymongo

app = Flask(__name__)

@app.route('/insert_m', methods=['GET','POST'])
def insert_m():
    try:
        if(request.method == 'POST'):
            client = pymongo.MongoClient("mongodb+srv://sunitha:root@cluster0.hilt2da.mongodb.net/?retryWrites=true&w=majority")
            #db = client.test
            database = client['student']
            collection = database["marksheet"]
            id = request.json['id']
            phy = request.json['phy']
            chem = request.json['chem']
            math = request.json['math']
            collection.insert_one({'id' : id,'phy' : phy,'chem' : chem,'math' : math})
        return jsonify(str(True))
    except Exception as e:
        print(e)
        return jsonify(str(False))



@app.route('/test1', methods=['GET','POST'])
def test():
    if(request.method=='POST'):
        result = "Hello"
        return jsonify(result)


@app.route('/insert', methods=['GET','POST'])
def insert():
    try:
        mydb = con.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           port=3306,
                           database='student',
                           auth_plugin='mysql_native_password',
                           use_pure=True)

        #mydb = db_connect()
        cursor = mydb.cursor()
        #logging.info("Inserting data to marksheet table")
        cursor.execute("use student;")
        if(request.method == 'POST'):
            id = request.json['id']
            phy = request.json['phy']
            chem = request.json['chem']
            math = request.json['math']
            query = "insert into marksheet values("+str(id)+","+str(phy)+","+str(chem)+","+str(math)+");"
            cursor.execute(query)
            mydb.commit()
        mydb.close()
        return jsonify(str(True))
        #return jsonify("Successfully inserted")
    except Exception as e:
        print(e)
        return jsonify(str(False))
        #logging.exception(e)


@app.route('/update_m', methods=['GET','POST'])
def update_m():
    try:
        if(request.method == 'POST'):
            client = pymongo.MongoClient("mongodb+srv://sunitha:root@cluster0.hilt2da.mongodb.net/?retryWrites=true&w=majority")
            #db = client.test
            database = client['student']
            collection = database["marksheet"]
            id = request.json['id']
            attr = request.json['attr']
            val = request.json['val']
            collection.update_one({'id' : id},{'$set': {attr : val}})
        return jsonify(str(True))
    except Exception as e:
        print(e)
        return jsonify(str(False))




@app.route('/update', methods=['GET','POST'])
def update():
    try:
        mydb = con.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           port=3306,
                           database='student',
                           auth_plugin='mysql_native_password',
                           use_pure=True)
        cursor = mydb.cursor()
        cursor.execute("use student;")

        if (request.method == 'POST'):
            id = request.json['id']
            attr = request.json['attr']
            val = request.json['val']
            query = "update marksheet set "+str(attr)+"="+str(val)+" where id = "+str(id)+";"
            cursor.execute(query)
            mydb.commit()
        mydb.close()
        return jsonify(str(True))

    except Exception as e:
        print(e)
        return jsonify(str(False))


@app.route('/delete_m', methods=['GET','POST'])
def delete_m():
    try:
        if(request.method == 'POST'):
            client = pymongo.MongoClient("mongodb+srv://sunitha:root@cluster0.hilt2da.mongodb.net/?retryWrites=true&w=majority")
            #db = client.test
            database = client['student']
            collection = database["marksheet"]
            id = request.json['id']
            collection.delete_one({'id': id})
        return jsonify(str(True))
    except Exception as e:
        print(e)
        return jsonify(str(False))


@app.route('/delete', methods=['GET','POST'])
def delete():
    try:
        mydb = con.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           port=3306,
                           database='student',
                           auth_plugin='mysql_native_password',
                           use_pure=True)
        cursor = mydb.cursor()
        cursor.execute("use student;")

        if (request.method == 'POST'):
            id = request.json['id']
            query = "delete from marksheet where id = "+str(id)+";"
            cursor.execute(query)
            mydb.commit()
        mydb.close()
        return jsonify(str(True))

    except Exception as e:
        print(e)
        return jsonify(str(False))


@app.route('/fetch_m', methods=['GET','POST'])
def fetch_m():
    try:
        if(request.method == 'POST'):
            client = pymongo.MongoClient("mongodb+srv://sunitha:root@cluster0.hilt2da.mongodb.net/?retryWrites=true&w=majority")
            #db = client.test
            database = client['student']
            collection = database["marksheet"]
            id = request.json['id']
            d = collection.find({'id': id})
            res=""
            for i in d:
                print(i)
                res = res+str(i)

        return jsonify(str(res))
    except Exception as e:
        print(e)
        return jsonify(str(False))



@app.route('/fetch', methods=['GET','POST'])
def fetch():
    try:
        mydb = con.connect(host="127.0.0.1",
                           user="root",
                           password="root",
                           port=3306,
                           database='student',
                           auth_plugin='mysql_native_password',
                           use_pure=True)
        cursor = mydb.cursor()
        cursor.execute("use student;")

        if (request.method == 'POST'):
            id = request.json['id']
            query = "select * from marksheet where id = "+str(id)+";"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
        mydb.close()
        return jsonify(str(result))

    except Exception as e:
        print(e)
        return jsonify(str(False))




if __name__ =='__main__':
    app.run()
