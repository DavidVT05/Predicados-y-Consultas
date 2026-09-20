# Se a creado el universo con el cuan se comprobara si  las consultas a realizar son correctas o estan bien formuladas 
universo = { 
        "estudiantes": {
            "David": {
                "No_Control": 23760356,
                "Edad": 20,
                "Materias": ["Aprobadas"],
                "Universidad":["Graduado"],
                "Asiste_a_escuela": ["Carro"],
                "Pago_Inscripcion":["Si"],
                "Tiene_260_Creditos":260,
                "Realiza_Practicas_Profesionales":["No"],
                "Realiza_modalidad_DUAL":["Si"],
                "Presentado_Extraordinario":["No"]
            },
            "Jose": {
                "No_Control": 23760312,
                "Edad": 19,
                "Materias": ["Reprobadas"],
                "Universidad":["No se a graduado"],
                "Asiste_a_escuela": ["Carro"],
                "Pago_Inscripcion":["No"],
                "Tiene_260_Creditos":250,
                "Realiza_Practicas_Profesionales":["No"],
                "Realiza_modalidad_DUAL":["No"],
                "Presentado_Extraordinario":["Si"]
            },
            "Ericka": {
                "No_Control": 23760347,
                "Edad": 23,
                "Materias": ["Aprobadas"],
                "Universidad":["Graduado"],
                "Asiste_a_escuela": ["Moto"],
                "Pago_Inscripcion":["Si"],
                "Tiene_260_Creditos":260,
                "Realiza_Practicas_Profesionales":["Si"],
                "Realiza_modalidad_DUAL":["No"],
                "Presentado_Extraordinario":["No"]
            },
            "Carlos": {
                "No_Control": 23760321,
                "Edad": 25,
                "Materias": ["Aprobadas"],
                "Universidad":["Graduado"],
                "Asiste_a_escuela": ["Moto"],
                "Pago_Inscripcion":["Si"],
                "Tiene_260_Creditos":260,
                "Realiza_Practicas_Profesionales":["Si"],
                "Realiza_modalidad_DUAL":["No"],
                "Presentado_Extraordinario":["No"]
            },
            "Maria": {
                "No_Control": 23760366,
                "Edad": 18,
                "Materias": ["Aprobadas"],
                "Universidad":["No se a graduado"],
                "Asiste_a_escuela": ["Carro"],
                "Pago_Inscripcion":["Si"],
                "Tiene_260_Creditos":260,
                "Realiza_Practicas_Profesionales":["Si"],
                "Realiza_modalidad_DUAL":["No"],
                "Presentado_Extraordinario":["No"]
            },
        },
        "Profesores": {
            "Emanuel": {
                "No_Empleado":25436875
            },
            "Rogelio": {
                "No_Empleado":34578963
            },
            "Carolina": {
                "No_Empleado": 4194938
            },
            "Melissa": {
                "No_Empleado":22563534
            }
        },
        "Carreras": {
            "Ing. Sistemas",
            "Ing. Industrial",
            "Ing. Arquitectura"
        },
        "Salones": {
            "Salon_101": 30,
            "Salon_405": 0,
            "Salon_403": 15,
            "Salon_204": 25
        }, 
    }
# Creacion de los predicados y las consultas 
# 1 E(x) = x es un estudiante
def estudiantes(x):
    for estudiantes, No_Control in universo["estudiantes"].items():
        print(estudiantes, type(estudiantes))
        if estudiantes == x:
            return True
    return False
#Consultas
print(estudiantes("Jose"))
print(estudiantes("Rogelio"))

# 2 M(x,y) = x tiene la matricula y
def estudiantes(x,y):
    for estudiantes, No_Control in universo["estudiantes"].items():
        print(estudiantes, type(estudiantes))
        if estudiantes == x:
            if No_Control["No_Control"] == y:
                return True
    return False 
#Consultas 
print(estudiantes("Carlos", 23760321))
print(estudiantes("Ericka", 23760321))

# 3 C(x) = x asiste a la escuela con carro
def estudiantes(x):
    for estudiantes, asiste_a_escuela in universo["estudiantes"].items():
        print(estudiantes, type(estudiantes))
        if estudiantes == x:
            if asiste_a_escuela["Asiste_a_escuela"] == ["Carro"]:
                return True
    return False
# Consultas
print(estudiantes("Maria"))
print(estudiantes("Ericka"))

# 4 Tiene_260_Cretidos(x) = x cuenta con 260 creditos o mas
def estudiantes(x):
    for estudiantes, tiene_260_creditos in universo["estudiantes"].items():
        print(estudiantes, type(estudiantes))
        if estudiantes == x:
            if tiene_260_creditos["Tiene_260_Creditos"] >= 260:
                return True
    return False
# Consultas
print(estudiantes("Ericka"))
print(estudiantes("Jose"))

# 5 Es_Carrera(x) = x es una carrera universitaria
def Carreras_Universitarias(x):
    for carreras in universo["Carreras"]:
        print(carreras, type(carreras))
        if carreras == x:
            return True
    return False
#Consultas
print(Carreras_Universitarias("Ing. Sistemas"))
print(Carreras_Universitarias("Jose"))

# 6 Es_Maestro(w) = w es un maestro
def Profesores(w):
    for profesores, No_Empleado in universo["Profesores"].items():
        print(profesores, type(profesores))
        if profesores == w:
            return True
    return False
#Consultas
print(Profesores("Rogelio"))
print(Profesores("Jose"))

#7 Tiene_Mesabancos(z) = El salon z tiene mesabancos
def Salon(z):
    for mesabancos, Tiene_Mesabancos in universo["Salones"].items():
        print(mesabancos, type(mesabancos))
        if mesabancos == z:
            if Tiene_Mesabancos > 0:
                return True
    return False
#Consultas
print(Salon("Salon_101"))
print(Salon("Salon_405"))