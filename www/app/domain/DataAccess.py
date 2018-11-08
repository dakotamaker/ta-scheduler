import csv
import sqlite3
import os, sys
from .AbstractDataAccess import AbstractDataAccess


_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)

class DataAccess(AbstractDataAccess):

    # Loads <tableName>.csv into the in memory database with column names <cols>
    def LoadCSVTable(self, tableName: str, cols: [str]):
        if len(tableName) <= 0 or len(cols) <= 0:
            raise ValueError

        colNames = ', '.join(['%s' % i[0] for i in cols])
        self.cur.execute('create table %s (%s);' % (
            tableName, ', '.join(['%s %s' % (i[0], i[1]) for i in cols])))
        with open(_root + '/database/%s.csv' % tableName) as f:
            reader = csv.reader(f)
            next(reader)  # skip col names
            values = [tuple(row) for row in reader]
            params = ('?,' + '?,'.join(' ' * len(cols))).rstrip(', ')
        self.cur.executemany('insert into %s (%s) values (%s);' %
                             (tableName, colNames, params), values)
        self.conn.commit()
    
    # Writes the in memory table <tableName> to <tableName>.csv
    def SaveCSVTable(self, tableName: str):
        if len(tableName) <= 0:
            raise ValueError

        self.cur.execute('pragma table_info(%s)' % tableName)
        colNames = [row['name'] for row in self.cur.fetchall()]

        self.cur.execute('select * from %s' % tableName)
        rowValues = [dict(row).values() for row in self.cur.fetchall()]
        with open(_root + '/database/%s.csv' % tableName, 'w', newline='\n') as f:
            writer = csv.writer(f)
            writer.writerow(colNames)
            writer.writerows(rowValues)