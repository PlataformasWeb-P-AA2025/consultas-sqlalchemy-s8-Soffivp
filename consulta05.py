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

#5. 
#5.1 En una consulta, obtener todos los cursos.
#5.2 Realizar un ciclo repetitivo para obtener en cada iteración 
#las entregas por cada curso (con otra consulta),
# y presentar el promedio de calificaciones de las entregas

#obtenemos todos los cursos
cursos = session.query(Curso).all()


for c in cursos:
    entregas = session.query(Entrega).join(Tarea).filter(Tarea.curso_id == c.id).all()

    suma = 0
    # calcula el número de entregas del curso actual
    nentregas = len(entregas)

    # se suman las calificaciones de las entregas
    for e in entregas:
        suma += e.calificacion

    # Si el número de entregas es mayor a 0 se obtiene el promedio
    if nentregas > 0:
        promedio = suma / nentregas
    else:
        promedio = 0

    print("Curso: %s, Promedio: %.2f" % (c.titulo, promedio))




