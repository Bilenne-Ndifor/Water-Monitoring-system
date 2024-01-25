import sqlite3
from random import random
from datetime import datetime

class adaptor():
    def retrive_all():
        try:
            db = sqlite3.connect('watersys.db')
            sql = "SELECT * from water;"
            cur = db.cursor()
            cur.execute(sql)
            source = []
            while True:
                record = cur.fetchone()
                source.append(record)
                if record == None:
                    break
            print(source)
            print("retrive succesful")
            return source
        except sqlite3.Error as error:
            print( error)
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
                
                
    def retrive_Gchat():
        try:
            db = sqlite3.connect('watersys.db')
            sql = "SELECT * from genmessage;"
            cur = db.cursor()
            cur.execute(sql)
            source = []
            while True:
                record = cur.fetchone()
                source.append(record)
                if record == None:
                    break
            print(source)
            print("retrive succesful")
            return source
        except sqlite3.Error as error:
            print( error)
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
                
    def retrive_Achat():
        try:
            db = sqlite3.connect('watersys.db')
            sql = "SELECT * from admessage;"
            cur = db.cursor()
            cur.execute(sql)
            source = []
            while True:
                record = cur.fetchone()
                source.append(record)
                if record == None:
                    break
            print(source)
            print("retrive succesful")
            return source
        except sqlite3.Error as error:
            print( error)
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
    
                
    def retrive_submi():
        try:
            db = sqlite3.connect('watersys.db')
            sql = "SELECT * from submission;"
            cur = db.cursor()
            cur.execute(sql)
            source = []
            while True:
                record = cur.fetchone()
                source.append(record)
                if record == None:
                    break
            print(source)
            print("retrive succesful")
            return source
        except sqlite3.Error as error:
            print( error)
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
                
    def retrive_com():
        try:
            db = sqlite3.connect('watersys.db')
            sql = "SELECT * from complaint;"
            cur = db.cursor()
            cur.execute(sql)
            source = []
            while True:
                record = cur.fetchone()
                source.append(record)
                if record == None:
                    break
            print(source)
            print("retrive succesful")
            return source
        except sqlite3.Error as error:
            print( error)
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
        
    def updatewater(watername,waterlocation,watertype,condition,approxdanger,zone):
        try:
            db= sqlite3.connect('watersys.db')
            cursor = db.cursor()
            print("Connected to SQLite")
            
            data=(watername,waterlocation,watertype,condition,approxdanger,zone)
            sql = """Update water set name= ? ,location = ? ,type = ? ,condition= ? ,approxdanger= ? , zone = ?  where name = ?"""
            cursor.execute(sql, (watername,waterlocation,watertype,condition,approxdanger,zone,watername))
            db.commit()
            print("Record Updated successfully ")
            cursor.close()
        except sqlite3.Error as error:
            print( error)
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
        
    def storecomplaint(userid,waterid,watername,watertype,complaint,approxdanger):
        try:
            print("Start")
            db = sqlite3.connect('watersys.db')
            print("Connected")
            cur = db.cursor()
            print("Starting insert")
            complaintid=datetime.now()
            data = (complaintid,userid,waterid,watername,watertype,complaint,approxdanger)
            print("gotten data")
            sql = """INSERT INTO complaint (complaintid,userid,waterid,Watername,watertype,complaint,approxdanger) VALUES (?,?,?,?,?,?,?);"""
            cur.execute(sql, data)
            db.commit()
            print("Store succesful")
        except sqlite3.Error as error:
            print( error)
            
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")

            
    def storeSubmission(userid,watername,waterlocation,watertype,complaint,approxdanger,zone):
        try:
            print("Start")
            db = sqlite3.connect('watersys.db')
            print("Connected")
            cur = db.cursor()
            print("Starting insert")
            submissionid=datetime.now()
            wid=submissionid
            print(submissionid)
            data = (submissionid,wid,userid,complaint,approxdanger,zone,watername,watertype,waterlocation)
            print("gotten data")
            sql = """INSERT INTO submission (submissionid,waterid,userid,condition,approxdanger,zone,watername,watertype,waterlocation) VALUES (?,?,?,?,?,?,?,?,?);"""
            cur.execute(sql, data)
            db.commit()
            print("Store succesful")
        except sqlite3.Error as error:
            print( error)
            
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
            
    def storewater(watername,location,type,complaint,approxdanger,zone):
        try:
            print("Start")
            db = sqlite3.connect('watersys.db')
            print("Connected")
            cur = db.cursor()
            print("Starting insert")
            waterid=datetime.now()
            data = (waterid,watername,location,type,complaint,approxdanger,zone)
            print("gotten data")
            sql = """INSERT INTO water (waterid,name,location,type,condition,approxdanger,zone) VALUES (?,?,?,?,?,?,?);"""
            cur.execute(sql, data)
            db.commit()
            print("Store succesful")
        except sqlite3.Error as error:
            print( error)
            
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
                
                
    def storeuser(name,location,typen,password):
        try:
            print("Start")
            db = sqlite3.connect('watersys.db')
            print("Connected")
            cur = db.cursor()
            print("Starting insert")
            userid=datetime.now()
            data = (userid,name,typen,location,password)
            print("gotten data")
            sql = """INSERT INTO User (userid,name,type,location,password) VALUES (?,?,?,?,?);"""
            cur.execute(sql, data)
            db.commit()
            print("Store succesful")
        except sqlite3.Error as error:
            print( error)
            
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
                
    def storemessageA(sendid,sendname,message):
        try:
            print("Start")
            db = sqlite3.connect('watersys.db')
            print("Connected")
            cur = db.cursor()
            print("Starting insert")
            timedate=datetime.now()
            data = (timedate,sendid,sendname,message)
            print("gotten data")
            sql = """INSERT INTO admessage (timedate,senderid,sendername,message) VALUES (?,?,?,?);"""
            cur.execute(sql, data)
            db.commit()
            print("Store succesful")
        except sqlite3.Error as error:
            print( error)
            
    def storemessageG(sendid,sendname,message):
        try:
            print("Start")
            db = sqlite3.connect('watersys.db')
            print("Connected")
            cur = db.cursor()
            print("Starting insert")
            timedate=datetime.now()
            data = (timedate,sendid,sendname,message)
            print("gotten data")
            sql = """INSERT INTO genmessage (timedate,senderid,sendername,message) VALUES (?,?,?,?);"""
            cur.execute(sql, data)
            db.commit()
            print("Store succesful")
        except sqlite3.Error as error:
            print( error)
            
        finally:
            if db:
                db.close()
                print("The SQLite connection is closed")
            
            
    def search(sname,password):
        db = sqlite3.connect('watersys.db')
        sql = "SELECT * from User WHERE name= (?) AND Password= (?)"
        cur = db.cursor()
        cur.execute(sql, (sname,password,))
        names = []
        while True:
            record = cur.fetchone()
            names.append(record)
            if record == None:
                break
        print(names)
        return names
    
    
    def select(name):
        db = sqlite3.connect('watersys.db')
        sql = """SELECT * from water WHERE name= (?)"""
        cur = db.cursor()
        cur.execute(sql,(name,))
        names1 = []
        while True:
            record = cur.fetchone()
            names1.append(record)
            if record == None:
                break
        print(names1)
        return names1
    
    def deletesub(name):
        try:
            sqliteConnection = sqlite3.connect('watersys.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from submission where watername = ?"""
            cursor.execute(sql_update_query, (name,))
            sqliteConnection.commit()
            print("Record deleted successfully")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
                
    def deletecom(name):
        try:
            sqliteConnection = sqlite3.connect('watersys.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sql_update_query = """DELETE from complaint where Watername = ?"""
            cursor.execute(sql_update_query, (name,))
            sqliteConnection.commit()
            print("Record deleted successfully")

            cursor.close()

        except sqlite3.Error as error:
            print("Failed to delete reocord from a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")
    
    
#adaptor.storecomplaint(3,6,"sucke","river","shit",8)
#adaptor.updatewater("ntam","Buea","Lake","poisonned","10","Rural")
#adaptor.deletecom("niger")
#adaptor.select("Mezam")
#adaptor.storemessage(1,"john","this is unacceptable")
#adaptor.storeSubmission(1,1,1,1,1,1,1 )