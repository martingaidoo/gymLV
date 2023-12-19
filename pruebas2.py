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
from datetime import datetime

import sqlite3
import tkinter as tk
from tkinter import ttk

fecha_actual = datetime.now()

fecha_con_mes_adicional = fecha_actual + relativedelta(months=1)

# Formatear la fecha como días/mes/año
actual = fecha_actual.strftime("%d/%m/%Y")
actaulMasMes = fecha_con_mes_adicional.strftime("%d/%m/%Y")

mixconexion = sqlite3.connect("BaseDatos.db")
cursor = mixconexion.cursor()

documento = 45087673

consulta = """
SELECT * FROM Clientes WHERE Documento = ?;
"""
cursor.execute(consulta, (documento,)) 
    

datos_cliente = cursor.fetchone()

consulta = """
SELECT * FROM Cuotas id_cliente WHERE id_cliente = ?;
"""
cursor.execute(consulta, (datos_cliente[0],)) 
datos_cuota = cursor.fetchone()

fecha_actual = datetime.strptime(actual, "%d/%m/%Y")
fecha_vencimiento = datetime.strptime(datos_cuota[5], "%d/%m/%Y")

if fecha_actual > fecha_vencimiento:
    print("entre")
    conexion = sqlite3.connect("BaseDatos.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE Cuotas SET Haber = ?, PLAN = ?, PROFESOR = ?, Fecha = ?, Vencimiento = ?, id_programa = ? WHERE id_cliente = ?",
                ("5000", "pase libre", "kevin", actual, "12/1/2023", "4", "1"))
    conexion.commit()
    print("Terminé")
