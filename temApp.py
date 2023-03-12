from db import get_connection, get_connection2

try:
    connection=get_connection2()
    with connection.cursor() as cursor:
        cursor.execute('call getAlumno()')
        resultset=cursor.fetchall()
        for row in resultset:
            print(row)
    connection.close()

except Exception as ex:
    print(ex)
    pass

"""try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call getAlumno(%s)',(2,))
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
except Exception as ex:
    pass"""

"""try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call getAlumno(%s,%s,%s)',("nombre","apellidos","correo"))
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
except Exception as ex:
    pass"""