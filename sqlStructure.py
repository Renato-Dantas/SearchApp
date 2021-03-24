import sqlite3

class sqliteFunctions:
    def __init__(self):
        self.connector = sqlite3.connect('supplier.db')
        self.cursor = self.connector.cursor()
        
    def insertValues(self,info):
        insert = 'INSERT INTO supplier VALUES (?,?,?,?,?,?,?,?)'
        self.cursor.execute(insert, info)
        self.connector.commit()

    def selectAllData(self):
        self.cursor.execute('SELECT * FROM supplier')
        data = self.cursor.fetchall()
        print(data)
    
    def searchSqlArea(self, area):
        select = 'SELECT * FROM supplier WHERE area = ?'
        self.cursor.execute(select, [area])
        data = cursor.fetchall()
        return data
    
    def searchSqlName(self, name):
        select = 'SELECT id,name,area,city,email,phone1,phone2,link FROM supplier WHERE name = ?'
        self.cursor.execute(select, [name])
        data = self.cursor.fetchall()
        return data

    def updateData(self, data):
        update = 'UPDATE supplier SET id = ?, name = ?, area = ?, city = ?, email = ?, phone1 = ?, phone2 = ?, link = ? WHERE name = ?'
        self.cursor.execute(update, data)
        data = self.cursor.fetchall()

    def closeConnection(self):
        self.cursor.close()
        self.connector.close()