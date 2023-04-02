"""Una PyME, tiene la siguiente estructura de pagos para sus 10 empleados: 

Un sueldo base

Una bonificación del 1% del sueldo base, por cada mes trabajado

Una asignación familiar del 5% del sueldo base por cada hijo


La suma de los tres valores anteriores, conforman
la “base imponible”.
Todos los empleados están en FONASA, así que
deben cotizar el 7% de la base imponible en salud. Los empleados están en una de dos: AFPs, la
primera cobra (entre imposición y otros gastos) el 12 % de la base imponible, mientras que la
segunda cobra el 11.4%
a) Pida el ingreso de datos de los 10 empleados
y los almacene. Debe pedir: nombre, apellido, sueldo base, afap, fecha de ingreso
y cantidad de hijos.

b) El programa debe calcular la base imponible,
según lo indicado arriba y luego descontar según corresponda.

c) El programa debe calcular lo que se debe
pagar a FONASA y el monto de cada AFAP.

d) El programa debe calcular los promedios de
pago a los empleados

e) El programa debe implementar control de
excepciones en cada ingreso de información.

El mensaje debe ser claro al usuario, indicando
que debe corregir en cada intento de ingresar los datos."""

import time
from datetime import datetime
import mysql.connector

def infoprincipal():
    print("iniciando programa de salario...")
    time.sleep(2)
    print("Bienvenido, a continuacion se le pedira sus credenciales")
    nombre=input("ingrese su nombre: ")
    apellido=input("ingrese su apellido: ")
    return nombre, apellido

def sueldo_hijo():
    sueldobase = int(input("ingrese su sueldo base mensual: "))
    hijo = int(input("ingrese la cantidad de hijos que tiene: "))
    return sueldobase, hijo

def pago_empresarial(sueldobase, hijo):
    bonificacion = (((sueldobase * 1)/100))
    asignacion = ((sueldobase * 5)/100 * hijo)
    print(f"A usted le corresponde una bonificacion de ${bonificacion} y una asignacion por hijo de ${asignacion} ")
    print("Le queda un total como base imponible de $",(sueldobase + bonificacion + asignacion))
    sueldoimponible = (sueldobase + bonificacion + asignacion)
    return sueldoimponible


def descuentos(sueldoimponible):
    salud= ((sueldoimponible*7)/100)
    afps1= ((sueldoimponible*12)/100)
    afps2= ((sueldoimponible*11.4)/100)
    print(f"Usted debe pagar ${salud} en salud y ademas la primera AFP debe pagar {afps1} y en la segunda AFP debe pagar {afps2}")
    descuentototal=(salud + afps1 + afps2)
    return descuentototal

continuar="SI"   
while continuar.upper=="SI":
    nombre_completo = infoprincipal()

    nombre = nombre_completo[0]

    apellido = nombre_completo[1]

    sueldobase, hijo = sueldo_hijo()

    sueldoimponible=pago_empresarial(sueldobase, hijo)

    descuentototal=descuentos(sueldoimponible)

    sueldoimp_descontado= sueldoimponible - descuentototal

    fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    mibase=mysql.connector.connect(
        host="localhost",
        user="root",
        password="joajoa123",
        database = "Empleados")

    micursor=mibase.cursor()

    micursor.execute("USE Empleados")

    #micursor.execute("create database Empleados")

    tablainfo="create table tabla_informativa(id_empleado int primary key not null auto_increment, nombre varchar(50) not null, apellido varchar(50) not null, fecha_ingreso varchar(50) not null, cant_hijos int, sueldo_base int not null, sueldo_imponible int not null, descuentos int not null, sueldo_descontado int not null)"
    micursor.execute(tablainfo)
    insercion="insert into tabla_informativa(id_empleado, nombre, apellido, fecha_ingreso, cant_hijos, sueldo_base, sueldo_imponible, descuentos, sueldo_descontado) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    datos =(None, nombre, apellido, fecha_actual, hijo, sueldobase, sueldoimponible, descuentototal, sueldoimp_descontado)
    micursor.execute(insercion, datos)
    mibase.commit()

    micursor.close()
    mibase.close()
    continuar=input("deseas continuar ingresando nuevos datos de empleados?(SI o NO)")
    
   














