from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from clases import Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

# se importa información del archivo configuracion
from config import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()





#Obtener todas las tareas asignadas a los siguientes estudiantes 

#Jennifer Bolton 
#Elaine Perez
#Heather Henderson
#Charles Harris

#En función de cada tarea, presentar el número de entregas que tiene

#A partir de tarea se una la clase entrega y estudiante
tareas = session.query(Tarea).join(Entrega).join(Estudiante).filter(
	#el or filtra varios nombres de la clase estudiante
	or_(Estudiante.nombre == ("Jennifer Bolton"),
    	Estudiante.nombre == ("Elaine Perez"),
    	Estudiante.nombre == ("Heather Henderson"),
    	Estudiante.nombre == ("Charles Harris" ))).all()

#presentamos el titulo y el numero de entregas
for t in tareas:
	print("Tarea Titulo: %s,Numero Entregas : %s " 
		#len suma el numero de entregas 
		% (t.titulo, len(t.entregas)))


