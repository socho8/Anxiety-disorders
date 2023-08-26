def asignar_nivel(ataques):
    antecedentes = ataques["Antecedentes familiares"]
    genero = ataques['Genero']
    estres = ataques['Nivel de estres']
    sintomas = ataques['Sintomas']
    severidad = ataques['Severidad']
    impacto = ataques['Impacto en la vida']
    apoyo = ataques['Apoyo social']
    diagnostico = ataques['Panic Disorder Diagnosis']

    # Asigna el nivel de ataques basado en las condiciones dadas
    if sintomas == 'Ataques de panico':
        if genero == 'Mujer':
            return 4
        elif genero == 'Hombre':
            if antecedentes == 'Si':
                if apoyo == 'Bajo':
                    if estres == 'Alto':
                        if impacto in ['Alto', 'Moderado']:
                            if severidad == 'Alto':
                                return 4
                            elif severidad in ['Moderado', 'Bajo']:
                                return 4
                        elif impacto == 'Bajo':
                            return 3
                    elif estres in ['Moderado', 'Bajo']:
                        if impacto in ['Alto', 'Moderado']:
                            return 4
                        elif impacto == 'Bajo':
                            return 3
                elif apoyo in ['Moderado', 'Alto']:
                    if estres == 'Alto':
                        if impacto in ['Alto', 'Moderado']:
                            return 3
                        elif impacto == 'Bajo':
                            return 2
                    elif estres in ['Moderado', 'Bajo']:
                        return 2
                    
                else:
                    return 4
            elif antecedentes == 'No':
                if apoyo == 'Bajo':
                    if estres in ['Alto', 'Moderado']:
                        if impacto in ['Alto', 'Moderado']:
                            return 4
                        elif impacto == 'Bajo':
                            return 3
                    elif estres == 'Bajo':
                        return 2
                else: 
                    return 3
            else:
                return 4



    elif sintomas == 'Dificultad para respirar':
        if antecedentes == 'Si':
            if apoyo == 'Bajo':
                if estres == 'Alto':
                    if impacto in ['Alto', 'Moderado']:
                        if severidad == 'Alto':
                            return 4
                        elif severidad in ['Moderado', 'Bajo']:
                            return 4
                    elif impacto == 'Bajo':
                        return 3
                elif estres in ['Moderado', 'Bajo']:
                    if impacto in ['Alto', 'Moderado']:
                        return 4
                    elif impacto == 'Bajo':
                        return 3
            elif apoyo in ['Moderado', 'Alto']:
                if estres == 'Alto':
                    if impacto in ['Alto', 'Moderado']:
                        return 3
                    elif impacto == 'Bajo':
                        return 2
                elif estres in ['Moderado', 'Bajo']:
                    return 2
            else:
                return 4
        elif antecedentes == 'No':
            if apoyo == 'Bajo':
                if estres in ['Alto', 'Moderado']:
                    if impacto in ['Alto', 'Moderado']:
                        return 4
                    elif impacto == 'Bajo':
                        return 3
                elif estres == 'Bajo':
                    return 2
            else:
                return 3



    elif sintomas == 'Dolor de pecho':
        if antecedentes == 'Si':
            if apoyo == 'Bajo':
                if estres == 'Alto':
                    if impacto in ['Alto', 'Moderado']:
                        if severidad == 'Alto':
                            return 3
                        elif severidad in ['Moderado', 'Bajo']:
                            return 3
                    elif impacto == 'Bajo':
                        return 2
                elif estres in ['Moderado', 'Bajo']:
                    if impacto in ['Alto', 'Moderado']:
                        return 3
                    elif impacto == 'Bajo':
                        return 2
            elif apoyo in ['Moderado', 'Alto']:
                if estres == 'Alto':
                    if impacto in ['Alto', 'Moderado']:
                        return 2
                    elif impacto == 'Bajo':
                        return 1
                elif estres in ['Moderado', 'Bajo']:
                    return 1
            else:
                return 3
        elif antecedentes == 'No':
            if apoyo == 'Bajo':
                if estres in ['Alto', 'Moderado']:
                    if impacto in ['Alto', 'Moderado']:
                        return 3
                    elif impacto == 'Bajo':
                        return 2
                elif estres == 'Bajo':
                    return 1
            else:
                return 2



    elif sintomas == 'Miedo a perder el control':
        if antecedentes == 'Si':
            if apoyo == 'Bajo':
                if estres == 'Alto':
                    if impacto in ['Alto', 'Moderado']:
                        if severidad == 'Alto':
                            return 3
                        elif severidad in ['Moderado', 'Bajo']:
                            return 3
                    elif impacto == 'Bajo':
                        return 2
                elif estres in ['Moderado', 'Bajo']:
                    if impacto in ['Alto', 'Moderado']:
                        return 3
                    elif impacto == 'Bajo':
                        return 2
            elif apoyo in ['Moderado', 'Alto']:
                if estres == 'Alto':
                    if impacto in ['Alto', 'Moderado']:
                        return 2
                    elif impacto == 'Bajo':
                        return 1
                elif estres in ['Moderado', 'Bajo']:
                    return 1
            else:
                return 3
        elif antecedentes == 'No':
            if apoyo == 'Bajo':
                if estres in ['Alto', 'Moderado']:
                    if impacto in ['Alto', 'Moderado']:
                        return 3
                    elif impacto == 'Bajo':
                        return 2
                elif estres == 'Bajo':
                    return 1
            else : 
                return 2
            
                

    elif sintomas == 'Mareos':
        if antecedentes == 'Si':
            if apoyo == 'Bajo':
                if estres == 'Alto':
                    if impacto in ['Alto', 'Moderado']:
                        if severidad == 'Alto':
                            return 3
                        elif severidad in ['Moderado', 'Bajo']:
                            return 2
                    elif impacto == 'Bajo':
                        return 2
                elif estres in ['Moderado', 'Bajo']:
                    if impacto in ['Alto', 'Moderado']:
                        return 2
                    elif impacto == 'Bajo':
                        return 1
            elif apoyo in ['Moderado', 'Alto']:
                if estres == 'Alto':
                    if impacto in ['Alto', 'Moderado']:
                        return 2
                    elif impacto == 'Bajo':
                        return 1
                elif estres in ['Moderado', 'Bajo']:
                    return 1
            else: 
                return 2
        elif antecedentes == 'No':
            if apoyo == 'Bajo':
                if estres in ['Alto', 'Moderado']:
                    if impacto in ['Alto', 'Moderado']:
                        return 3
                    elif impacto == 'Bajo':
                        return 2
                elif estres == 'Bajo':
                    return 1
            else:
                return 1

    else:
        return 2  # Si no cumple ninguna de las condiciones, puede devolver un valor predeterminado o None
    



def cambiar_panic(ataques):
    antecedentes = ataques['Antecedentes familiares']
    sintomas = ataques['Sintomas']

    if sintomas == 'Ataques de panico':
        return 1
    else:
        return 0
    

def cargar_datos(nombre_archivo):
    ruta_archivo = os.path.join("..", "data", nombre_archivo)
    data = pd.read_csv(ruta_archivo, index_col=0)
    return data

def cargar_modelo(nombre_archivo):
    ruta_modelo = os.path.join("..", "model","production", nombre_archivo)
    modelo = joblib.load(ruta_modelo)
    return modelo
