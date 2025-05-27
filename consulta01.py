

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

#A partir de Entrega vamos uniendo cada una de las clases que necesitamos.
#Una vez unimos todas las tablas filtramos por el nombre Arte
#con all traemos todos los resultados del filtro y la union. 

entregas = (session.query(Entrega).join(Entrega.tarea).join(Tarea.curso)
	.join(Curso.departamento).join(Curso.instructor).join(Entrega.estudiante)
    .filter(Departamento.nombre == 'Arte')
    .all()
)

for e in entregas:
	#El for recorre la consulta y vamos obeniendo los datos solicitados de la consulta entregas.
	print("Tarea: %s,Estudiante: %s,Calificación %.2f,Instructor %s,Departamento %s " 
		% (e.tarea.titulo,e.estudiante.nombre, e.calificacion,e.tarea.curso.instructor.nombre,
		e.tarea.curso.departamento.nombre))
