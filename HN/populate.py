import psycopg2
import json
import psycopg2.extras
import sys

#read json file
with open('data.json', 'r') as f:
        data = json.load(f)

def do_insert(rec: dict):
        cols = rec.keys()
        cols_str = ','.join(cols)
        vals = [ rec[k] for k in cols ]
        vals_str = ','.join( ['%s' for i in range(len(vals))] )
        sql_str = """INSERT INTO hack_basemodel ({}) VALUES ({})""".format(cols_str, vals_str)
        cur.execute(sql_str, vals)
        con.commit()


                                
#connect to database
con = psycopg2.connect("dbname=jobdb user=u0_a292 password = ngoziKAMA")
cur = con.cursor()

for dat in data:
        print(dat)
        print("inserting to db")
        do_insert(dat)
        




