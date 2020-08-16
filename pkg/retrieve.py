# 1. Standard libraries
import os, sys
from pprint import pprint as prt
# 2. Third party
import mysql.connector as sql
import requests as rq
# 3. Local applications
# 3.1 Settings
from settings.cfg import (
    CONFIG, APPROUVED,
    PAGES, PRODUCTS_PER_PAGE,
    URL, FIELDS,
)
#from settings.install import Setup
#import dotenv


class Retrieval:
    def __init__(self):
        self.products = []
        self.data = None
#        self.setup = Setup()

    def retrieve(self):
#        for i in range(os.getenv("PRODUCT_PER_PAGE")):
        for i in range(PAGES):
            parameters = {
                "action": "process",
                "sort_by": "unique_scan_n",
                "fields": FIELDS,
                "country": "france",
                "page_size": PRODUCTS_PER_PAGE,
                "page": i + 1,
                "json": True,
            }
            r = rq.get(url=URL, params=parameters)
            if r.status_code == APPROUVED:
                self.data = r.json()
                # Clean the data before storing them
                # by removing uppercase and white space
                for product in self.data['products']:
                    for field, infos in product.items():
                        if isinstance(infos,dict) and infos == "nutriments":
                            for k, v in infos.items():
                                if '100g' in k:
                                    infos = infos.pop(k)
                        else:
                            product[field] = infos
                    self.products.append(product)

        return self.products
R = Retrieval()
ret = R.retrieve()
data = R.data
prt(ret)
#prt(data)
#    def register(self):
#        for field in self.products:
#            try:
#                c = sql.connect(**CONFIG)
#
#            except sql.Error as e:
#                if e.errno == sql.errorcode.ER_ACCESS_DENIED_ERROR:
#                    print("Something is wrong with you username or password")
#                elif e.errno == sql.errorcode.ER_BAD_DB_ERROR:
#                    print("Database does not exist")
#                    csr = c.cursor()
#                    self.setup.createDB(csr)
#                else:
#                    print(e)
#            
#            for product in products:
#                if product.keys() == ''
#                brand_id = csr.lastrowid
#                add_brand = ("INSERT INTO BRAND brand_id, name")
#                csr.execute(add_brand)
#
#            c.commit()
#            csr.close()
#            c.close()
#                
        



