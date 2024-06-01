import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="informatica1",
  password="bio123"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS INFORMATICA1")
mydb.database = "INFORMATICA1"
mycursor = mydb.cursor()
def Menu_ingreso(user,passw):
    """Esta función se encarga de verificar la existencia del usuario y contraseña proporcionados, en la base de datos.
    Argumentos= Usuario y contraseña.
    Retorna= True si existe al menos una linea de datos que se cumpla. 
    """
    cursor=mycursor
    sql= f"SELECT * FROM Ingreso WHERE Usuario = '{user}' AND contrasena = '{passw}'"
    cursor.execute(sql)
    return cursor.fetchone()


def Menu_1():
    op=int(input('Gestionar información de:\n1.Medicamentos\n2.Proveedores\n3.Ubicaciones\n4.Salir'))

def Tablas_vacias(tabla):
    """Esta función se encarga de revisar si cierta tabla está vacía, en caso de ser así retorna True.
    Argumentos= tabla
    Retorna= True si la tabla no tiene información
    """
    mycursor.execute(f"SELECT COUNT(*) FROM {tabla}")
    espacio = mycursor.fetchone()[0]
    return espacio == 0
