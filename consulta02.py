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


#se obtiene los datos de Departamento, junto a los de curso, tarea y entrega
# Filtramos las calificaciones menores o iguales a 0.3 

departamento = (session.query(Departamento).join(Curso).join(Tarea) 
    .join(Entrega).filter(Entrega.calificacion <= 0.3) 
    .all() 
)



for dp in departamento:

	print("Nombre Departamento: %s,Numero de cursos: %d" 
		#len obtiene la cuenta de los cursos
		% (dp.nombre, len(dp.cursos)))
