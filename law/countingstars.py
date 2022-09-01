from flask import Flask, jsonify, request, render_template
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import numpy as np
import psycopg2
import pandas as pd
#데이터 베이스를 불러온다

def namecheck(nick_name):
    #대충 여기서 있는지 없는지를 확인한다.
    #불러와서 확인하는 방법으로 그리고 정렬까지
    conn_string="dbname='ddtk33j69v200c' host='ec2-54-225-234-165.compute-1.amazonaws.com' user='uxweficayqkvnb' password='191795f6687a563f2d49dd25fa1d4a3b481604b2bfb416f11811f430377a463f'"
    conn=psycopg2.connect(conn_string)

    cur = conn.cursor()
    sql = "SELECT * FROM public.userrank;"
    cur.execute(sql)
    rows = cur.fetchall()
    result = pd.DataFrame(rows, columns=['name', 'point'])
    #불러왔다.

    if (result["name"] == nick_name).all():
        print(nick_name)
    else:
        sql = "INSERT INTO userrank(name, point) VALUES ({}', 0)".format(nick_name) 
        cur.execute(sql)

   
def countingstar():
    print("Tlqkf")   
    sql = "UPDATE userrank SET point = point +1 WHERE {}".format(nick_name)
    cur.execute(sql)

def rankup():
    conn_string="dbname='ddtk33j69v200c' host='ec2-54-225-234-165.compute-1.amazonaws.com' user='uxweficayqkvnb' password='191795f6687a563f2d49dd25fa1d4a3b481604b2bfb416f11811f430377a463f'"
    conn=psycopg2.connect(conn_string)

    cur = conn.cursor()
    sql = "SELECT * FROM public.userrank;"
    cur.execute(sql)
    rows = cur.fetchall()
    result = pd.DataFrame(rows, columns=['name', 'point'])
    
    top5 = result.sort_values("point", ascending=False)
    return top5.head