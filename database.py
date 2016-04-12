#!/usr/bin/python
# -*- coding: utf-8 -*-

print( "Content-type:text/html\r\n\r\n")
print('<html>')

import _mysql

class Database():
    def __init__(self):
        self.connection = _mysql.connect(host="iesc-s2.mit.edu",user="aladetan_matiash",passwd="TYZfuR5p",db="aladetan_matiash")
        self.connection.close()
        '''try:
            self.connection = _mysql.connect(host="iesc-s2.mit.edu",user="aladetan_matiash",passwd="TYZfuR5p",db="aladetan_matiash")
            print(self.connection)
#            self.connection.close()
        except _mysql.Error as  e:
            print("ERROR! %d: %s" % (e.args[0],e.args[1]))'''
    

    def findSongs(self,username):
        song_dict = {}
#        self.cursor = connection.cursor()
        query = '''SELECT song_title FROM songs WHERE username=%s''' % username
        self.connection.query(query)
        result = self.connection.store_result()
        rows = self.connection.fetch_row(maxrows=0,how=0)
        for row in rows:
            print(row)
            
    def insert(self,id,username,song_title):
        '''
        inserts data into table, where data is a list of values specific to that table
        '''
        query = '''INSERT INTO songs (id,username,song_title,chords) VALUES (%d,%s,%s,NONE)''' % (id,username,song_title)
        self.connection.query(query)
        

    
database = Database()
database.insert(1,"Matias","Random Song")
database.findSongs("Matias")
database.connection.close()

print("</html>")
