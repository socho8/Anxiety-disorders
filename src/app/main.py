import streamlit as st
import numpy as np
import pandas as pd
import pickle



# Cargamos nuestro modelo anteriormente ya entrenado
with open('../model/production/modelo_listo.pkl', 'rb') as archivo:
        model = pickle.load(archivo)

#Imagenes en linea
imagen_ansiedad = 'https://www.lavanguardia.com/files/article_main_microformat/files/fp/uploads/2019/04/10/5fa51829b4517.r_d.496-279-0.jpeg'
imagen_nivel_4 = 'https://www.holanuna.com/es/blog/wp-content/uploads/2021/09/Anxiety-infographic-ES.png'
img_ans = 'https://www.clinicbarcelona.org/media/cache/960_jpeg/uploads/media/default/0001/11/5e2c024973095b7913c8e20603b94a19d34d0ad9.png'

#Imagen modelo
imagen_modelo = 'imagenes\mdc.jpg'

#Funcion para cargar nuestros datasets
@st.cache_data
def cargar_datos(ruta):
    data = pd.read_csv(ruta, index_col=0)
    return data



#ESTRUCTURA PRINCIPAL DE NUESTRA APP
def main():


    st.sidebar.title("Secciones")
    section = st.sidebar.radio("", ["Introduccion", "Data y modelo", "¿Sabias que?", "Prediccion"])

    if section == "Introduccion":
        render_section1()
    elif section == "Data y modelo":
        render_section2()
    elif section == "¿Sabias que?":
        render_section3()
    elif section == "Prediccion":
        render_section4()



#Seccion 1
def render_section1():

    st.title('La ansiedad y su lado oculto')
    st.image(imagen_ansiedad, use_column_width=True)
    st.subheader('¿Que es la ansiedad?')
    st.markdown("""
**La ansiedad** es una reacción normal que se activa ante una amenaza o un peligro. La ansiedad puede no ser saludable cuando se convierte en trastorno de ansiedad. Esta reacción se activa en situaciones habitualmente no amenzantes/peligrosas o de manera persistente, hasta el punto que interfiere de manera importante en la vida diaria. 
Sentir ansiedad de modo ocasional es una parte normal de la vida. Sin embargo, las personas con **trastornos de ansiedad** con frecuencia tienen preocupaciones y miedos intensos, excesivos y persistentes sobre situaciones diarias. Con frecuencia, en los trastornos de ansiedad se dan episodios repetidos de sentimientos repentinos de ansiedad intensa y miedo o terror que alcanzan un máximo en cuestión de minutos (ataques de pánico).
Estos sentimientos de ansiedad y pánico interfieren con las actividades diarias, son difíciles de controlar, son desproporcionados en comparación con el peligro real y pueden durar un largo tiempo. Con el propósito de prevenir estos sentimientos, puede suceder que evites ciertos lugares o situaciones. Los síntomas pueden empezar en la infancia o la adolescencia y continuar hasta la edad adulta.
""")
    st.subheader('Clasificacion')
    st.markdown('''
Podemos clasificar los niveles de ansiedad en 4 tipos:  
                
• **Ansiedad leve:** asociada a tensiones de la vida diaria. La persona se encuentra en situación de alerta y su campo de percepción aumenta. Este tipo de ansiedad puede propiciar el aprendizaje y la creatividad.  

• **Ansiedad moderada:** en la cual la persona se centra sólo en las preocupaciones inmediatas. Esto implica una disminución del campo de percepción. La persona bloquea determinadas áreas, pero puede reconducirse si se centra en ello.  

• **Ansiedad grave:** hay una reducción significativa del campo perceptivo. La persona puede centrarse en detalles específicos, sin poder pensar nada más. La conducta se centra en aliviar la ansiedad.  

• **Angustia:** temor, miedo, terror. La persona es incapaz de realizar ninguna actividad, ni aun siendo dirigida. La angustia supone una desorganización de la personalidad, y puede ser fatal, ya que un período prolongado de angustia podría producir agotamiento y depresion. Se manifiesta por un aumento de la actividad motora, disminución de la capacidad para relacionarse, percepción distorsionada y pérdida del pensamiento racional .

''')
    st.subheader('Causas')
    st.write('''
No está del todo claro cuáles son las causas de los trastornos de ansiedad. Ciertas experiencias de vida, como acontecimientos traumáticos, parecen provocar los trastornos de ansiedad en personas que ya son propensas a la ansiedad. Los rasgos heredados también pueden ser un factor.
''')
    

    st.subheader('Tratamientos')
    st.markdown('''
Los trastornos de ansiedad son altamente tratables, sin embargo, solo el 36.9% de los que los padecen reciben tratamiento.
                  
**Terapia**  
Uno de los mejores métodos de tratamiento para la ansiedad es la terapia cognitiva-conductual (TCC). Esto ayuda a los pacientes a comprender los pensamientos y sentimientos que influyen en los comportamientos.
                  
**Medicamentos**  
La medicación es otra forma de ayudar a aliviar los síntomas de ansiedad. A menudo, un paciente utilizará medicamentos y terapia juntos para el tratamiento.
                  
**Medicamentos complementarios y alternativos**  
Los medicamentos complementarios y alternativos son tratamientos que normalmente no se consideran parte de la medicina convencional; sin embargo, se ha encontrado que son útiles para aliviar algunos síntomas de ansiedad. Ejemplos:  
•	Acupuntura,  
•	Meditación,  
•	Ejercicio (especialmente yoga),  
•	Técnicas de relajación,  
•	Modificación en la dieta al disminuir la ingesta de azúcar, alcohol y cafeína.

''')




    
#Seccion 2
def render_section2():
    st.title('Datasets y modelo utilizado')
    
    st.subheader('Datasets')
    # Cargar el primer archivo CSV
    dataset_original = cargar_datos("../data/Data_junta.csv")
    st.write("Primeros registros de la data original")
    st.dataframe(dataset_original.head())

    # Cargar el segundo archivo CSV
    dataset_modificado = cargar_datos("../data/Ansiedad_final.csv")
    st.write("Primeros registros del dataset con su feature engineering ya realizado:")
    st.dataframe(dataset_modificado.head())

    st.subheader('Modelo')
    st.markdown('Para este proyecto utilice un modelo de **Random Forest Classifier**')
    st.write('Precisión (Accuracy): 100.00%')
    st.image(imagen_modelo, use_column_width=True)




#Seccion 3
def render_section3():
    st.title('Conociendo un poco mas sobre este trastorno')
    st.image(img_ans, use_column_width=True)
    st.markdown('''
**Tenemos que tener en cuenta que aunque la ansiedad es una emoción normal es un aspecto importante para aquellos que la tienen, ya que el objetivo no puede ser eliminarla, sino aprender a tolerarla y gestionarla.**
                  
El trastorno de ansiedad no implica solamente estar preocupado. También puede ocasionar, o empeorar, otros trastornos mentales y físicos, como los siguientes:  
                
•	Depresión   
•	Abuso de sustancias  
•	Problemas para dormir (insomnio)  
•	Problemas digestivos o intestinales  
•	Dolor de cabeza y dolor crónico  
•	Aislamiento social  
•	Fatigabilidad fácil  
•	Dificultad para concentrarse o tener la mente en blanco  
•	Irritabilidad
''')
    st.subheader('¿Sabias que el problema de salud mental más frecuente es el trastorno de ansiedad?')

    st.markdown('''
**La Organización Mundial de la Salud afirma que 1 de cada 13 personas tiene ansiedad**  
                
•  	Se estima que 264 millones de adultos en todo el mundo padecen ansiedad. (Fuente: Organización Mundial de la Salud, 2017).  
•	De estos adultos, 179 millones eran mujeres (63%) y 105 millones eran hombres (37%). (Fuente: Our World in Data, 2018).  
•	La prevalencia de todos los trastornos mentales aumentó en un 50% a nivel mundial, de 416 millones a 615 millones entre 1990 y 2013. (Fuente: Organización Mundial de la Salud, 2016).  
•	Se estima que el 31% de todos los adultos experimentarán un trastorno de ansiedad en algún momento de su vida.  
•   Durante la pandemia la palabra ansiedad fue la mas buscada en Google a nivel mundial.


''')
    



#Seccion 4
def render_section4():

    with open('../model/production/modelo_listo.pkl', 'rb') as archivo:
        model = pickle.load(archivo)

    st.title("Comprobacion del nivel de ansiedad y su gravedad")

    # Entradas de usuario
    edad = st.slider('Edad:', min_value=0, max_value=100, value=30)
    genero = st.radio('Género:', ['Masculino', 'Femenino', 'Prefiero no especificar'])
    #antecedentes_familiares = st.checkbox('Antecedentes Familiares')
    antecedentes_familiares = st.radio('Antecedentes Familiares (algun familiar paso por un trastorno de ansiedad)', ['Si', 'No'])
    nivel_estres = st.selectbox('Nivel de Estrés:', ['Bajo', 'Moderado', 'Alto'])
    #sintomas = st.multiselect(
    #    'Síntomas (selecciona uno o varios):',
        #    ['Mareos', 'Miedo a perder el control', 'Dolor de pecho', 'Dificultad para respirar', 'Ataques de pánico'])
    sintomas = st.selectbox('Sintomas experimentados:', ['Mareos', 'Miedo a perder el control', 'Dolor de pecho', 'Dificultad para respirar', 'Ataques de panico'])
    #sintomas = st.selectbox('Sintomas experimentados:', [0, 1 , 2 , 3  , 4])
    severidad = st.selectbox('Severidad:', ['Bajo', 'Moderado', 'Alto'])
    impacto_vida = st.selectbox('Impacto en la Vida:', ['Bajo', 'Moderado', 'Alto'])
    apoyo_social = st.selectbox('Apoyo Social:', ['Bajo', 'Moderado', 'Alto'])


        # Convertir las entradas a valores numéricos (ajusta esto según tus categorías)
    genero_num = 0 if genero == 'Masculino' else 1
        #antecedentes_num = 0 if antecedentes_familiares == 'False' else 1
    antecedentes_num = {'No' : 0 , 'Si' : 1}[antecedentes_familiares]
    nivel_estres_num = {'Bajo': 0, 'Moderado': 1, 'Alto': 2}[nivel_estres]
    sintomas_num = {'Mareos' : 0, 'Miedo a perder el control' : 1, 'Dolor de pecho' : 2, 'Dificultad para respirar':3,'Ataques de panico' : 4}[sintomas]
    severidad_num = {'Bajo': 0, 'Moderado': 1, 'Alto': 2}[severidad]
    impacto_vida_num = {'Bajo': 0, 'Moderado': 1, 'Alto': 2}[impacto_vida]
    apoyo_social_num = {'Bajo': 0, 'Moderado': 1, 'Alto': 2}[apoyo_social]


        # Realizar la predicción
    if st.button('Realizar prediccion'):
        input_data = np.array([[edad, genero_num, antecedentes_num, nivel_estres_num, sintomas_num, severidad_num, impacto_vida_num, apoyo_social_num]])
        prediction = model.predict(input_data)
        prediction = int(prediction)

        # Mostrar resultados
        if prediction == 1:
            st.markdown('**TU NIVEL DE ANSIEDAD ES RELATIVAMENTE BAJO**')
            st.markdown('''Afortunadamente podemos decir que tu problema de ansiedad es algo muy leve que se puede
                        tratar con diferentes metodos, aqui algunos ejemplos:  
                        ''')
            st.markdown(''' 
                        • Realizando algun deporte  
                        • Meditando  
                        • Leyendo   
                        • Manteniendote activo y no sedentario  
                        • Comiendo saludablemente y no ingiriendo bebidas con mucha cafeina  
                        • Buscar reirse con series, peliculas o documentales  
                        • Escuchar la musica que te guste  
                        • Practicar mindfullnes  
                        • Tomar una sesion de masajes  
                        • Activar sentidos tales como el olfato (prediendo una vela aromatica por ejemplo)  
                        • Pasar tiempo de calidad con amigos y familiares  
                        • Practica yoga  
''')
            st.write('Espero que estos consejos puedan ayudarte a controlar esa ansiedad y estres. Buena suerte!')



        elif prediction == 2:
            st.markdown('**TU NIVEL DE ANSIEDAD ES MODERADO**')
            st.markdown('''Seguramente estas experimentando algunas sensaciones que no sabes como controlar, 
                        lo primero seria poder reconocer algunos de estos sintomas. Aqui una lista de los posibles sintomas:  
                        • Nervios repentinos   
                        • Poco control de tus emociones  
                        • Irritabilidad  
                        • Baja autoestima  
                        • Estres  
                        • Pensamientos negativos  
                        • Falta de concetracion  
                        • Miedo a situaciones poco probables    
                        
''')
            st.markdown('''
                        Estos y entre otros son algunos de los sintomas que puedes estar experientando. Puede que pienses que
                        normal o le restes importancia, lo primero que debemos hacer es reconocer estos sintomas y reconocer el 
                        momento en el que lo estamos padeciendo. Al poder saber en el momento exacto que lo estas padeciendo
                        es mucho mas facil llegar a controlarlos. Aqui te dejo algunos consejos y practicas para disminuir el
                        estres, la ansiedad y aprender a calmar estos sintomas.  
                        • Realizando algun deporte  
                        • Meditando   
                        • Leyendo  
                        • Practicar mindfullnes  
                        • Tomar una sesion de masajes  
                        • Practica yoga  
                        • Aqui te dejo un par de ejercicios para practicar la respiracion  
                            [Ejercicio 1](https://www.youtube.com/watch?v=I5tip6L5fOQ])  
                            [Ejercicio 2](https://www.youtube.com/shorts/xdMiU_ZRFS0)
''')        
            st.write('Espero que estos consejos y ejercicios te sean de ayuda. Buena suerte!')



        elif prediction == 3:
            st.markdown('**TU NIVEL DE ANSIEDAD ES ELEVADO**')
            st.markdown('''
                    Si estas en este nivel quiere decir que la ansiedad en tu vida es algo cotidiano y a veces imposible de controlar.
                    Lo primero decirte que mantengas la calma y que todo va a estar bien. Es posible aprender a controlar y a vivir 
                        con ella. No todo lo que te dice tu cabeza es real y mucho menos pasara. 
                        Todas las personas sufren la ansiedad de una manera diferente, pero la parte positiva en todo esto que es la 
                        manera de tratarla / neutralizarla / aprender a convivir con ella , en la mayoria de los casos es la misma. 
                        No te preocupes demasiado porque no eres la unica persona que lo padece. Aqui mismo te dejare varios ejercicios para
                        poder trabajarla y disminuir su sintomatologia
''')
            st.markdown('''
                        [Ejercicio respiracion](https://www.youtube.com/watch?v=I5tip6L5fOQ)  
                        [Ejercicio de meditacion](https://www.youtube.com/watch?v=9-IOMXpv7Ys)  
                        [Musica antiestres y ansiedad](https://www.youtube.com/watch?v=4YExd-nCYlI)  
                        [Ejercicio de concentracion](https://www.youtube.com/shorts/2d8ysmRWeoc)  
                        
''')
            st.markdown(''' Recuerda que estos son solo algunos ejercicios para controlar la ansiedad. Tambien puedes probar:  
                        • Manteniendote activo y no sedentario  
                        • Comiendo saludablemente y no ingiriendo bebidas con mucha cafeina  
                        • Buscar reirse con series, peliculas o documentales  
                        • Escuchar la musica que te guste  
                        • Tomar una sesion de masajes  
                        • Practica yoga  
                        • Pasando buenos momentos con amigos y familiares. Diciendo lo que te pasa y sientes  
''')
            st.write('''Si ves que implementando todos estos ejercicios y tecnicas no puedes llegar a controlar el trastorno,
                     lo mas recomendable es buscar ayuda profesional. La terapia es la forma mas eficaz para llegar a controlarlo.
                     Te recomiendo buscar a alguien de confianza quien te pueda derivar al profesional correspondiente.
                     Espero haber sido de ayuda, te deseo mucha suerte!''')

            
        elif prediction == 4:
            st.markdown('**TU NIVEL DE ANSIEDAD ES GRAVE**')
            st.markdown('''
                        No te asustes, todo estara bien. En estos momentos seguramente sientes que no tienes control de tu vida
                        pero dejame decirte que todo pasara, que tienes mas control del que piensas y que nada es tan malo como parece.
                        Es normal sentirse mal, tener dias malos y tener miedo del que vendra. Nadie puede minimizar lo que sientes, nadie
                        sabe bien por lo que estas pasando y con lo que vives. 
                        Tranquil@, todo tiene solucion y tu puedes con todo.  
                        Ahora lo mas importante es que ya supiste reconocer el problema, lo siguiente es tratarlo. Lo primero que te recomiendo
                        es que comiences terapia, vayas con un profesional adecuado y asi poder comenzar el tratamiento psicologico.  
                        Ademas te dejare un par de ejercicios y consejos para que puedas trabajar estos ataques de panico. Buena suerte!
''')
            st.markdown('''
                        • **RESPIRACION PROFUNDA**    
                        Si bien la hiperventilación es un síntoma de ataque de pánico que puede aumentar el miedo, 
                        respirar profundamente puede reducir los síntomas de pánico durante un ataque.  
                        Concéntrate en inhalar y exhalar por la boca, sintiendo cómo el aire llena lentamente tu pecho y abdomen, y luego expúlsalo lentamente. 
                        Inhala contando hasta cuatro, mantén el aire por un segundo y luego exhala contando hasta cuatro.  
                        • **CIERRA LOS OJOS**  
                        Algunos ataques de pánico provienen de factores desencadenantes que te abruman.
                        Si te encuentras en un entorno acelerado con muchos estímulos, esto puede provocar que sufras uno.  
                        Para reducir los estímulos, cierra los ojos durante el ataque de pánico. 
                        Esto puede bloquear cualquier estímulo adicional y hacer que sea más fácil concentrarte en tu respiración.  
                        • **PUNTO DE ENFOQUE**  
                        Algunas personas encuentran útil enfocarse en un solo objeto durante un ataque de pánico. 
                        Elije un objeto a la vista y ve con atención cada uno de sus detalles.    
                        • **IMAGINA TU LUGAR FELIZ**  
                        ¿Cuál es el lugar más relajante del mundo que puedas imaginar? 
                        ¿Una playa soleada frente a un mar de olas suavemente apacibles? ¿Una cabaña en las montañas?  
                        Imagínate en ese lugar, y trata de concentrarte en los detalles tanto como sea posible. 
                        Imagínate hundiendo los dedos de los pies en la arena cálida, o sintiendo el olor intenso de los pinos.
                        Este lugar debe ser tranquilo, calmado y relajante    
                        •**REPITE UN MANTRA INTERNAMENTE**  
                        Repetir un mantra internamente puede ser relajante y tranquilizador, 
                        y puede brindarte algo a lo cual aferrarte durante un ataque de pánico.  
                        Ya sea simplemente “Esto también pasará” o un mantra que sea personal para ti, 
                        repítelo en un bucle mental hasta que sientas que el ataque de pánico comienza a disminuir.   
                        • **AROMATERAPIA**  
                        El uso de ciertos aromas puede favorecer nuestra sensación de bienestar y aliviar los síntomas de ansiedad. La aromaterapia consiste en utilizar fragancias provenientes de aceites esenciales, velas, inciensos, etc., para actuar sobre el estado de ánimo. 
                        Entre los aromas relajantes más comunes se encuentran la lavanda, la manzanilla, el jazmín y la rosa.  
                        
''')
            st.markdown('''
                        Ahora te dejare algunos ejercicios en lineas con los cuales puedes ayudarte en estos casos:  
                        [Tecina de respiracion](https://www.youtube.com/shorts/2onJfaAPiQg)  
                        [Tecnica SOS](https://www.youtube.com/watch?v=INCMsVJzTsE)  
                        [Ejercicios](https://www.youtube.com/watch?v=axDOxpQUcOs)  
                        [Meditacion](https://www.youtube.com/watch?v=ekUC96MWAWk)  
                        [Otra tecnica de respiracion](https://www.youtube.com/shorts/1hqGFfXk8XM)
''')
            st.write('Aqui te dejo una imagen con diferentes tecnicas tambien. Y recordarte que tu puedes con todo!')
            st.image(imagen_nivel_4, use_column_width=True)



if __name__ == "__main__":
    main()