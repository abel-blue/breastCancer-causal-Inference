import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error
import os
import sys
import streamlit as st


def DBConnect(dbName=None):
    conn = mysql.connect(host=st.secrets['mysql']['host'], user=st.secrets['mysql']['user'],
                         password=st.secrets['mysql']['password'], database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur


def emojiDB(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    dbQuery = f"ALTER DATABASE {dbName} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
    cur.execute(dbQuery)
    conn.commit()


def createDB(dbName: str) -> None:
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()


def createTables(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    sqlFile = 'sql/database.sql'
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')
    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()


def insert_to_tweet_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:

    conn, cur = DBConnect(dbName)
    for _, row in df.iterrows():

        sqlQuery = f"""INSERT INTO {table_name} (radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave points_mean,symmetry_mean,fractal_dimension_mean,area_se,smoothness_se,compactness_se,concavity_se,concave points_se,fractal_dimension_se,radius_worst,texture_worst,diagnosis)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20])

        try:
            cur.execute(sqlQuery, data)
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return


def db_execute_fetch(*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)
    field_names = [i[0] for i in cursor1.description]
    res = cursor1.fetchall()
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} recrods fetched from {tablename} table")
    cursor1.close()
    connection.close()
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res


if __name__ == "__main__":
    createDB(dbName='score_db')
    emojiDB(dbName='score_db')
    createTables(dbName='score_db')
    df = pd.read_csv('../data/data.csv')
    df.info()
    insert_to_tweet_table(dbName='score_db', df=df,
                          table_name='TB')