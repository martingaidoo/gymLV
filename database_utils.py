import tkinter
from tkinter import PhotoImage
import customtkinter
from customtkinter import CTk, CTkFrame, CTkButton
from PIL import ImageTk,Image
import tkinter as tk
import pygame
import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Obtener la fecha actual
fecha_actual = datetime.now()

fecha_con_mes_adicional = fecha_actual + relativedelta(months=1)

# Formatear la fecha como días/mes/año
actual = fecha_actual.strftime("%d/%m/%Y")
actaulMasMes = fecha_con_mes_adicional.strftime("%d/%m/%Y")

def registrarAsistencia(id):
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Asistencia (Cliente, Fecha) VALUES (?, ?)",
                        (id, actual))
    conn.commit()
    conn.close()
    
def agregar_cliente(cliente_data):
    # Conectar a la base de datos SQLite (asegúrate de que la base de datos exista)
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    # Obtener los datos del cliente
    apellido, nombre, documento, correo, fecha_nacimiento, telefono = cliente_data
    # Verificar que ningún dato esté vacío
    if apellido and nombre and documento and correo and fecha_nacimiento and telefono:
        try:
            # Insertar los datos en la tabla
            cursor.execute("INSERT INTO Clientes (Apellido, Nombre, Documento, Correo, Fecha_Nacimiento, Telefono) VALUES (?, ?, ?, ?, ?, ?)",
                        (apellido, nombre, documento, correo, fecha_nacimiento, telefono))
            # Confirmar la transacción
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
        finally:
            conn.close()
def registrarPago(data):
    # Conectar a la base de datos SQLite (asegúrate de que la base de datos exista)
    mixconexion = sqlite3.connect("BaseDatos.db")
    cursor = mixconexion.cursor()
    # Obtener los datos del cliente
    documento, Haber, Plan, Profesor= data

    consulta = """
    SELECT * FROM Clientes WHERE Documento = ?;
    """
    cursor.execute(consulta, (documento,)) 

    datos_cliente = cursor.fetchone()

    id = datos_cliente[0]
    id_cliente =  id

    consulta = """
    SELECT * FROM Programa WHERE Nombre = ?;
    """
    cursor.execute(consulta, (Plan,)) 
    datos_programa = cursor.fetchone()

    id_programa = datos_programa[0]

    # Verificar que ningún dato esté vacío
    if id and Haber and Plan and Profesor:
        try:
            Haber = str(int(datos_programa[2])-int(Haber))

            # Insertar los datos en la tabla
            cursor.execute("INSERT INTO Cuotas (id, Haber, PLAN, PROFESOR, Fecha , Vencimiento, id_cliente, id_programa) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id, Haber, Plan, Profesor, actual, actaulMasMes, id_cliente, id_programa))
            # Confirmar la transacción
            mixconexion.commit()
        except sqlite3.Error as ex:
            mixconexion.rollback()
        finally:
            mixconexion.close()


def obtener_datos_cliente(documento):
    # Consulta SQL para obtener los datos de un cliente por su documento
    conn = sqlite3.connect("BaseDatos.db")
    cursor = conn.cursor()
    consulta = """
    SELECT * FROM Clientes WHERE Documento = ?;
    """
    cursor.execute(consulta, (documento,)) 
    datos_cliente = cursor.fetchone()    
    #id_cliente, apellido, nombre, documento, correo, fecha_nacimiento, telefono = datos_cliente
    consulta = """
    SELECT * FROM Cuotas WHERE id_cliente = ?;
    """
    cursor.execute(consulta, (datos_cliente[0],))
    datos_cliente = datos_cliente + cursor.fetchone()
    conn.close()
    return datos_cliente
