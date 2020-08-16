import sys
import mysql.connector as sql

from config import CONFIG as cfg
from config import DB



class Setup:
    def __init__(self):
        pass

    def createDB(self, cursor):
        try:
            csr.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'\
                COLLATE 'utf8mb4_unicode_ci'"
            )

        except sql.Error as e:
            print("Failed to create database: {}".format(e))
            exit(1)

    def connect(self):
        try:
            c = sql.connect(**CONFIG)

        except sql.Error as e:
            if e.errno == sql.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with you username or password")
            elif e.errno == sql.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
                createDB(cursor)

            else:
                print(e)

    def tables(self):
        for name in TABLES:
            description = TABLES[name]
        try:
            print("Creating table {}:".format(name), end="")
            csr.execute(description)
        except sql.Error as e:
            if e.errno == sql.errorcode.ER_TABLE_EXISTS_ERROR:
                print("The table already exists.")
            else:
                print(e.msg)
        c.close()
    


c.close()

