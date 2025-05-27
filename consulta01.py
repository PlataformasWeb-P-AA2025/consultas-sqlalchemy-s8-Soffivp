

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

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


#1. Obtener las entregas de todos los estudiantes que pertenecen al
# departamento de Arte. En función de la entrega, 
#presentar, nombre del tarea, nombre del estudiante, calificación, 
#nombre de instructor y nombre del departamento
#mdl = session.query(Matricula).join(Estudiante).filter(Estudiante.nombre == "Tony").all()
#for m in mdl:
#    print(m.modulo)


#se obtiene los datos de Tarea
tareas = session.query(Entrega).join(Tarea).all()
for t in tareas:
	#obtengo a traves de la union de curso  
	curso = tareas.join(Curso).all()
	#print(t.tarea)






