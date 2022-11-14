"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    df_raw = open('clusters_report.txt')

    raw_rows = []
    for row in df_raw:
        row = row.replace('\n', '')
        raw_rows.append(row)

    index = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
    key_words = []
    porcentaje = []
    cantidad = []
    cluster = []
    key_word = ""
    for row in range(4, len(raw_rows)):
        if len(raw_rows[row].split()) > 0:
            if raw_rows[row].split()[0] in index:   
                aux = raw_rows[row].split()    
                cluster.append(int(aux[0]))
                cantidad.append(int(aux[1]))
                porcentaje.append(float(aux[2].replace(',','.')))
            key_word += raw_rows[row][41:] + " "  
        else:
            key_word = key_word[:-1]
            key_word = key_word.replace(".","")
            key_words.append(key_word)
            key_word = ""

    for i in range(len(key_words)):
        key_words[i] = key_words[i].replace(" ", "*")

    """ for i in range(len(key_words)):
        for j in range(5,0,-1):
            key_words[i] = key_words[i].replace("*"*j, "*") """

    for i in range(len(key_words)):
        key_words[i] = key_words[i].replace("*****", "*")

    for i in range(len(key_words)):
        key_words[i] = key_words[i].replace("****", "*")

    for i in range(len(key_words)):
        key_words[i] = key_words[i].replace("***", "*")

    for i in range(len(key_words)):
        key_words[i] = key_words[i].replace("**", "*")

    for i in range(len(key_words)):   
        key_words[i] = key_words[i].replace("*", " ")

    dict = {'cluster': cluster, 
        'cantidad_de_palabras_clave': cantidad,
        'porcentaje_de_palabras_clave': porcentaje,
        'principales_palabras_clave': key_words}

    df = pd.DataFrame(dict)

    return df