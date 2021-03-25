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
        data = self.cursor.fetchall()
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

    # Retorna uma lista com as áreas possíveis
    def readTxt(self):
        with open ('area.txt', encoding='UTF-8') as file:
            areaList = []
            for line in file:
                areaList.append(line.strip('\n'))
        return areaList

    def searchListNames(self):
        search = "SELECT name FROM supplier"
        self.cursor.execute(search)
        names = self.cursor.fetchall()
        return names

    def closeConnection(self):
        self.cursor.close()
        self.connector.close()