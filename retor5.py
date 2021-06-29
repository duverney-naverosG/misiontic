def analisisTRM(rutaArchivo):
    import pandas as pd
    #1) Validar que el origen de los datos tenga formato (extensión) CSV antes de realizar
    # cualquier cómputo, retornando el mensaje “Extensión inválida” en caso de que no cumpla 
    if rutaArchivo[-3:].lower() != "csv":
        return "Extensión inválida"

    #2) Intentar realizar la carga del archivo CSV a un dataframe de pandas con separación de comas “,”. 
    # En caso de que falle el intento, retornar el mensaje “Error al leer el archivo de datos”.
    try:
        DataFrame  = pd.read_csv(rutaArchivo, sep=',')
    except:
        return "Error al leer el archivo de datos"
    
    #3) Cambiar el campo que contiene la fecha en formato string a tipo fecha de pandas, y convertirla en 
    # el índice del dataframe, dado que este especifica el día de cada registro,pero no se realizarán cómputos con esta información.
    DataFrame['Fecha'] = pd.to_datetime( DataFrame['Fecha'], dayfirst=True )
    DataFrame.set_index('Fecha',inplace=True)
    
    #4) Calcular el valor promedio de la variación absoluta del dólar.
    variacion_df = list()
    for i in range(len(DataFrame['TRM'])-1):
        calculo = (abs(DataFrame['TRM'][i] - DataFrame['TRM'][i+1])/DataFrame['TRM'][i]) * 100
        variacion_df.append(calculo)
    promedio = pd.Series(variacion_df).mean()

    #5) Obtener un dataframe que contenga únicamente los registros donde el número de contagios 
    # es mayor o igual a la media de casos de COVID-19.
    promedioCasos = DataFrame['Casos'].mean()
    df = DataFrame[DataFrame['Casos']>=promedioCasos]
    return {'Promedio Variación': promedio, 'Registros Mayores': df}


print(analisisTRM("BaseDeDatosReto5.csv"))
print(analisisTRM('https://raw.githubusercontent.com/luismescobarf/clasesCiclo1/master/BaseDeDatosReto5.csv'))