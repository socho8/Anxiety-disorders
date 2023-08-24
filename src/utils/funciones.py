def asignar_nivel(ataques):
    antecedentes = ataques["Antecedentes familiares"]
    estres = ataques['Nivel de estres']
    sintomas = ataques['Sintomas']
    severidad = ataques['Severidad']
    impacto = ataques['Impacto en la vida']
    apoyo = ataques['Apoyo social']
    diagnostico = ataques['Panic Disorder Diagnosis']

    # Asigna el nivel de ataques basado en las condiciones dadas
    if diagnostico == 1:
            return 4
    elif diagnostico == 0:
        if sintomas in ['Ataques de panico']:
            return 4
        elif sintomas in ['Dificultad para respirar'] and antecedentes == 'Si' and apoyo == 'Bajo':
            return 4
        elif sintomas in ['Dificultad para respirar'] and antecedentes == 'Si' and apoyo in ['Moderado', 'Alto']:
            return 3
        elif sintomas in ['Dificultad para respirar'] and antecedentes == 'No':
            return 3
        elif sintomas in ['Dolor de pecho'] and antecedentes == 'Si' :
            return 3
        elif sintomas in ['Miedo a perder el control']:
            return 2
        elif sintomas in ['Mareos'] and antecedentes == 'Si' and apoyo in ['Bajo', 'Moderado']:
            return 2
        elif sintomas in ['Mareos'] and antecedentes == 'No' and apoyo in ['Alto']:
            return 1
        else:
            return 1
    else:
        return None  # Si no cumple ninguna de las condiciones, puede devolver un valor predeterminado o None
    



def cambiar_panic(ataques):
    antecedentes = ataques['Antecedentes familiares']
    sintomas = ataques['Sintomas']

    if sintomas == 'Ataques de panico':
        return 1
    else:
        return 0