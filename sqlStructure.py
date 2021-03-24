import sqlite3

class sqliteFunctions:

    def insertValues(self,info):
        connector = sqlite3.connect('supplier.db')
        cursor = connector.cursor()
        insert = 'INSERT INTO supplier VALUES (?,?,?,?,?,?,?,?)'
        cursor.execute(insert, info)
        connector.commit()
        connector.close()

    def selectAllData(self):
        connector = sqlite3.connect('supplier.db')
        cursor = connector.cursor()
        cursor.execute('SELECT * FROM supplier')

        data = cursor.fetchall()
        connector.close()
        print(data)
    
    def searchSqlArea(self, area):
        connector = sqlite3.connect('supplier.db')
        cursor = connector.cursor()
        select = 'SELECT * FROM supplier WHERE area = ?'
        cursor.execute(select, [area])
        data = cursor.fetchall()
        connector.close()
        return data
    
    def searchSqlName(self, name):
        connector = sqlite3.connect('supplier.db')
        cursor = connector.cursor()
        select = 'SELECT id,name,area,city,email,phone1,phone2,link FROM supplier WHERE name = ?'
        cursor.execute(select, [name])
        data = cursor.fetchall()
        connector.close()
        return data

    def updateData(self, data):
        connector = sqlite3.connect('supplier.db')
        cursor = connector.cursor()
        update = 'UPDATE supplier SET id = ?, name = ?, area = ?, city = ?, email = ?, phone1 = ?, phone2 = ?, link = ? WHERE name = ?'
        cursor.execute(update, data)
        data = cursor.fetchall()
        connector.commit()
        connector.close()