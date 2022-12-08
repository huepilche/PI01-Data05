from fastapi import FastAPI
import pandas as pd
import sqlalchemy
import numpy as np

DATABASE_URL= 'sqlite:///../Datasets/filmes.db'
engine = sqlalchemy.create_engine(DATABASE_URL)


app = FastAPI(title= 'Movies-queries', description= 'ETL - API project', version='1.0.1')

@app.get('/get_max_duration/')
async def MaxDuracion(year:int, tipo:str, plataforma:str):
        DF = pd.read_sql('filmes', engine)
        Filtro_consulta = (DF['Platform'] == plataforma) & (DF['release_year'] == year) & (DF['type'] == tipo)
        indice = DF[Filtro_consulta]['duration'].idxmax()
        return [DF.loc[indice,'title'], DF.loc[indice,'duration']]

@app.get('/get_count_platform/')
async def Programas(plataforma:str):
        DF = pd.read_sql('filmes', engine)
        Filtro_consulta = (DF['Platform'] == plataforma)
        Nro_Movies = DF[Filtro_consulta]['type'].str.contains('Movie').sum()
        Nro_TVShows = DF[Filtro_consulta]['type'].str.contains('TV Show').sum()
        return {"Movies":int(Nro_Movies) , "TVShows":int(Nro_TVShows)}

@app.get('/get_listedin/')
async def FrecuenciaGenero(genero:str):
        DF = pd.read_sql('filmes', engine)
        Filtro_consulta = DF['listed_in'].str.contains(genero)
        Nro_genero = DF[Filtro_consulta].groupby('Platform')['listed_in'].count()
        return Nro_genero.to_dict()

@app.get('/get_actor/')
async def ActoresRepetidos(year:int, plataforma: str):
        DF = pd.read_sql('filmes', engine)
        condicion = (DF['Platform']==plataforma) & (DF['release_year']==year) 
        actores = DF[condicion]['cast'].str.split(pat =',', expand=True)
        union = pd.concat(objs = [actores[i] for i in range(len(actores.columns))], ignore_index = True)
        dic = union.value_counts().to_dict()
        return list(dic.items())[0]

        