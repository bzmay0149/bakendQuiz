import sqlite3


con = sqlite3.connect("quiz.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE if not exists preguntas(id, pregunta, respuesta1, respuesta2, respuesta3, acertada)")

def read_all():
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM preguntas")
        rows = res.fetchall()
        
        #Para cambiar los valores de la lista en tuplas (objetos)
        pregunta_list = []
        for row in rows:
            row = {"id": row[0],
                "pregunta": row[1],
                "respuesta1": row[2],
                "respuesta2": row[3],
                "respuesta3": row[4],
                "acertada": row[5]
                }
            pregunta_list.append(row) #esto es para incluir en pregunta_list cada uno de las tuplas creadas (row)
            print("que es esto ", row)
        return pregunta_list
    except:
        None
    finally:
        con.close()


def read(pregunta_id):
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM preguntas WHERE id=?", [pregunta_id])
        row = res.fetchone()

        pregunta = {"id": row[0],
                "pregunta": row[1],
                "respuesta1": row[2],
                "respuesta2": row[3],
                "respuesta3": row[4],
                "acertada": row[5]
                }
        return pregunta_id
    except:
        None
    finally:
        con.close()

def create(quiz):
    con = sqlite3.connect("quiz.db")
    cur = con.cursor()
    try:
        res = "INSERT INTO preguntas VALUES(?, ?, ?, ?, ?, ?)"
        valores = (quiz['id'], quiz['pregunta'],
                quiz['respuesta1'], quiz['respuesta2'], quiz['respuesta3'], quiz['acertada'])
        cur.execute(res, valores)
        con.commit()
        # print("Esto es mi data quiz", quiz)
        # Esto es mi data quiz 
        # {'id': '1', 'pregunta': '¿que es <p>?', 'respuesta1': 'una lista', 'respuesta2': 'un titulo', 'respuesta3': 'un parrafo', 'acertada': 'un parrafo'}
    except:
        None
    finally:
        con.close()

def remove_pregunta(id):
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM preguntas WHERE id=?", [id])
        con.commit()
    except:
        None
    finally:
        con.close()

#Modificar

def update(new_id, new_pregunta, new_respuesta1, new_respuesta2, new_respuesta3,  new_acertada):
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        res = "UPDATE preguntas SET pregunta = ?, respuesta1 = ?, respuesta2 = ?, respuesta3 = ?, acertada = ? WHERE id = ?"
        values = (new_pregunta, new_respuesta1, new_respuesta2, new_respuesta3, new_acertada, new_id)
        cur.execute(res, values)
        con.commit()
    except:
        None
    finally:
        con.close()

#Esta función recoge la data que viene del Front

def update_pregunta_data(pregunta_id, data): #recoge los datos del front: data
    #Esta función hace dos tareas:
    #1. Guardar los valores que vienen del front en variables
    new_pregunta = data.get("pregunta")
    new_respuesta1 = data.get("respuesta1")
    new_respuesta2 = data.get("respuesta2")
    new_respuesta3 = data.get("respuesta3")
    new_acertada = data.get("acertada")
    # print("esta es la pregunta", new_pregunta)
    # print("esto es data", data) 
    # data {
    #  'pregunta': '¿que es <p>',  
    #  'respuesta1': 'una lista',
    #  'respuesta2': 'un titulo',
    #  'respuesta3': 'un parrafo', 
    #  'acertada': 'un parrafo'
    #  }
    
    
    #2. Pasar eso valores a la función update que tenemos en la parte de arriba para actualizar la BBDD.
    #Estamos llamando a la función de update con los valores del front
    update(pregunta_id, new_pregunta, new_respuesta1,new_respuesta2, new_respuesta3,  new_acertada)
   
    
