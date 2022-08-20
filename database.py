import mysql.connector as con
import logging
from flask import Flask, request, jsonify
import pymongo
from log import log_file

'''

1 . Write a program to insert a record in sql table via api database
2.  Write a program to update a record via api 
3 . Write a program to delete a record via api 
4 . Write a program to fetch a record via api
5 . All the above questions you have to answer for mongo db as well . 
'''

app = Flask(__name__)



@app.route('/insert', methods=['GET','POST'])
def insert():
    try:
        mydb = db_connect()
        cursor = mydb.cursor()
        logging.info("Inserting data to marksheet table")
        cursor.execute("use student;")
        if(request.method == 'POST'):
            id = request.json['id']
            phy = request.json['phy']
            chem = request.json['chem']
            math = request.json['math']
        query = "insert into marksheet values("+str(id)+","+str(phy)+","+str(chem)+","+str(math)+");"
        cursor.execute(query)
        mydb.commit()
        return jsonify("Successfully inserted")
    except Exception as e:
        logging.exception(e)

@app.route('/connect', methods=['GET','POST'])
def db_connect():
    """
    Create a database connector
    :return: returns the connector
    """
    try:
        logging.info("Connect to database")
        mydb = con.connect(host = "localhost",
                           user="root",
                           password="root",
                           use_pure=True)
        return mydb
    except Exception as e:
        mydb.close()
        print(e)
        logging.exception(e)




if __name__ =='__main__':
    app.run()
