import psycopg2

def postgresdb():
    try:
        con = psycopg2.connect(
            host='pilotni',
            databse='postgres',
            user='postgres',
            password='bugslife',
            port='5432'
        )
        cur = con.cursor()
        sql = '''INSERT INTO postgresdb (NAMES, MD5, SHA1, SHA 256) VALUES (%s, %s, %s, %s)'''
        sql_insert = ('Names', 'MD5', 'SHA1', 'SHA256')
        cur.execute(sql, sql_insert)
        rows = cur.fetchall()
        print(rows)

        con.commit()
        count = cur.rowcount
        print(count, "successfully inserted data")

    except (Exception, psycopg2.Error) as error:
        print("failed to insert data")
    finally:
        if con:
            cur.close()
            con.close()
            print("database closed")