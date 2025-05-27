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




#2. Todos los departamentos que tengan notas de entregas menores o iguales a 0.3 . 
#En función de los departamentos, presentar el nombre del departamento y el 
#número de cursos que tiene cada departamento



#mdl = session.query(Matricula).join(Estudiante).filter(Estudiante.nombre == "Tony").all()
#for m in mdl:
#    print(m.modulo)
#    session.query(Entrega)
#    .join(Tarea)
#    .join(Curso)
#    .join(Departamento)
#    .filter(Departamento.id == id_departamento)
#    .all()

#registros = session.query(Club, Jugador).join(Jugador).\
#         filter(Jugador.nombre.like("%Da%")).all()
 

#se obtiene los datos de Tarea


dpt = (
    session.query(Departamento.nombre, Entrega)
    .select_from(Entrega)
    .join(Entrega.tarea)
    .join(Tarea.curso)
    .join(Curso.departamento)
    .filter(Entrega.calificacion <= 0.3)
    .all()


)

for nombre_dpto, entrega in dpt:
	for curso 
    print(f"Departamento: {nombre_dpto}, Nota: {entrega.calificacion}")

