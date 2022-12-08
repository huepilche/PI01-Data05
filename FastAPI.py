from fastapi import FastAPI
import pandas as pd
import sqlalchemy
import numpy as np


# importación de la base de datos creada a partir de un dataframe de pandas
DATABASE_URL= 'sqlite:///Datasets/filmes.db'
engine = sqlalchemy.create_engine(DATABASE_URL)

#Se define la WebApp
app = FastAPI(title= 'Movies-queries', description= 'ETL - API project', version='1.0.1')

#Se definen las funciones para las consultas a realizar en el navegador
# EL retorno de las funciones se acomoda para la compatibilidad del tipo de archivo que se disponibiliza en el navegador (json)
@app.get('/duracion_maxima/')
async def MaxDuracion(year:int, tipo:str, plataforma:str): #
        DF = pd.read_sql('filmes', engine)
        Filtro_consulta = (DF['Platform'] == plataforma) & (DF['release_year'] == year) & (DF['type'] == tipo)
        indice = DF[Filtro_consulta]['duration'].idxmax()
        return [DF.loc[indice,'title'], DF.loc[indice,'duration']]

@app.get('/n°_programas/')
async def Programas(plataforma:str):
        #engine = sqlalchemy.create_engine(DATABASE_URL)
        DF = pd.read_sql('filmes', engine)
        Filtro_consulta = (DF['Platform'] == plataforma)
        Nro_Movies = DF[Filtro_consulta]['type'].str.contains('Movie').sum()
        Nro_TVShows = DF[Filtro_consulta]['type'].str.contains('TV Show').sum()
        return {"Movies":int(Nro_Movies) , "TVShows":int(Nro_TVShows)}

@app.get('/genero_por_plataforma/')
async def FrecuenciaGenero(genero:str):
        #engine = sqlalchemy.create_engine(DATABASE_URL)
        DF = pd.read_sql('filmes', engine)
        Filtro_consulta = DF['listed_in'].str.contains(genero)
        Nro_genero = DF[Filtro_consulta].groupby('Platform')['listed_in'].count()
        return Nro_genero.to_dict()

@app.get('/actores_repetidos/')
async def ActoresRepetidos(year:int, plataforma: str):
        #engine = sqlalchemy.create_engine(DATABASE_URL)
        DF = pd.read_sql('filmes', engine)
        condicion = (DF['Platform']==plataforma) & (DF['release_year']==year) 
        actores = DF[condicion]['cast'].str.split(pat =',', expand=True)
        union = pd.concat(objs = [actores[i] for i in range(len(actores.columns))], ignore_index = True)
        dic = union.value_counts().to_dict()
        return list(dic.items())[0]
        
