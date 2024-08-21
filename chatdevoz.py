import pyjokes
import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import datetime
import wikipedia
import cv2
from ejemploMachinelearning import machinaejemplo as machEjemplo

#escuchar nuestro microfono y devolver el audio como texto
def transformar_audio_en_texto():
    #almacenar recognizer en variable
    r = sr.Recognizer()
    #configurar microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold=0.8

        #informar de la grabacion
        print('ya puedes hablar')

        #guardar lo que escuche como audio
        audio= r.listen(origen)

        try:
            #buscar en google lo escuchado
            pedido=r.recognize_google(audio,language='es-mx')
            #prueba de que pudo ingresar
            print('dijiste: '+pedido)

            #return pedido
            return pedido
        #fallo de no entender audio
        except sr.UnknownValueError:
            #prueba de que no comprendio el audio
            print('No entendi')
            #devolver error
            return 'Error de audio'
        #em caso de no poder resolver el pedido
        except sr.RequestError:
            # prueba de no poder resolver el pedido
            print('error de pedido')
            # devolver error
            return 'lo siento tuve un error'
        #error inesperado
        except:
            # prueba de que no comprendio el audio
            print('algo salio mal')
            # devolver error
            return 'error inesperado'


#funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    #encender el motor de pyttssx3
    engine=pyttsx3.init()
    engine.setProperty('voice',id1)
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


#funcion que da el dia
def pedir_dia():
    #crear variable con datos de hoy
    dia= datetime.date.today()
    print(dia)
    #dia de la semana
    dia_semana=dia.weekday()


    #dicionario con nombres de dias
    dias_dic={0:'Lunes',
              1:'Martes',
              2:'Miercoles',
              3:'jueves',
              4:'Viernes',
              5:'sabado',
              6:'Domingo'}

    hablar(f'Hoy es dia {dias_dic[dia_semana]} de cheve')


#informar que hora es
def pedir_hora():
    #crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora=f'Son las : {hora.hour} con {hora.minute} perfecto para beber y los {hora.second} segundos'
    print(hora)
    #decir hora
    hablar(hora)

#saludo inicial
def saludo_inicial():
    #crear variable con datos de hora
    hora=datetime.datetime.now()
    if 6<=hora.hour>20:
        momento= 'Buenas noches'
    elif hora.hour>=6 and hora.hour<13:
        momento='Buen dia'
    else:
        momento='Buenas tardes'



    hablar(f'Hola soy un asistente virtual,{momento}')


def pedido_wiki(wikipedido):
    hablar('Buscando en wikipedia')
    pedido = wikipedido.replace('wikipedia', '')
    wikipedia.set_lang('es')
    resultado = wikipedia.summary(pedido, sentences=1)
    hablar(resultado)

def busqueda_internet(pedidoB):
    hablar('buscando')
    pedido = pedidoB.replace('busca en internet', '')
    pywhatkit.search(pedido)
    hablar('esto es lo que encontre')

def busqueda_youtube(pedidoYt):
    hablar('reproduciendo')
    pywhatkit.playonyt(pedidoYt)

def mostrartutorial():
    hablar("Este son mis funciones")
    tuto=cv2.imread('tutorial.jpg')
    cv2.imshow("funciones",tuto)
    cv2.waitKey()
    cv2.destroyAllWindows()


#funcion central de asistente
def pedir_cosas():
    saludo_inicial()
    #varaible de corte
    comenzar= True

    while comenzar:
        #activar micro y guardar el pedido en un string
        pedido=transformar_audio_en_texto().lower()

        if 'curso' in pedido:
            hablar('claro')
            pedido = pedido.replace('busca curso de', '')
            webbrowser.open(f'https://www.udemy.com/courses/search/?src=ukw&q={pedido}')
            continue
        elif 'navegador' in pedido:
            hablar('claro')
            webbrowser.open('https://www.google.com')
            continue
        elif 'día' in pedido:
            pedir_dia()
            continue
        elif 'hora' in pedido:
            pedir_hora()
            continue
        elif 'wikipedia' in pedido:
            pedido_wiki(pedido)
            continue
        elif 'internet' in pedido:
            busqueda_internet(pedido)
            continue
        elif 'reproducir' in pedido:
            busqueda_youtube(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'Hola' in pedido:
            hablar(saludo_inicial())
            continue
        elif 'ayuda' in pedido:
            mostrartutorial()
            continue
        elif 'machine learning' in pedido:
            hablar("Claro aqui tienes un ejemplo basado en gente con problemas del corazon en cleveland")
            hablar("donde el numero de enfermedades puede ser de 1 a 4")
            hablar("Tambien te muestro su arbol de desiciones que por cierto es muy grande")
            machEjemplo()
            continue
        elif 'adiós' in pedido:
            hablar('adiós')
            break


#opciones de voz/idioma
id1='HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0'
id2='HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'


mostrartutorial()
pedir_cosas()
