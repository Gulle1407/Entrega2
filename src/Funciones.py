def searchLargestStr(titles):
    """
    Recibe una lista de cadenas y devuelve la de mayor longitud, 
    si recibe otro tipo de dato retorna un mensaje de error 
    """
    max=0
    if isinstance(titles, list):    #Comprobamos haber recibido una lista de strings
        if not all(isinstance(item, str) for item in titles):
            return "Tipo incorrecto de parametro ingresado"      #se considero mas correcto que un exit(1)
    else:
        return "Tipo incorrecto de parametro ingresado"
    for i in titles:
        act=len(i.replace(" ",""))  #guardo la cantidad de caracteres sin contar espacios
        if act<max:
            continue
        else:
            max=act
            may=i
    return may

def checkUsserName(nombre):
    """
    Recibe, un string y verifica que cumpla los criterios 
    de un nombre de usuario.
    Asume que se lee una entrada del teclado
    """
    #Verifica que tenga una longitud mayor a 5 caracteres y que estos sean letras y/o numeros
    if (len(nombre)<5) or not(nombre.isalnum()): 
        return "El nombre de usuario no cumple con los requisitos."
    digit=any(i.isdigit() for i in nombre) #verifica que haya almenos un numero
    uper=any(i.isupper() for i in nombre) #verifica que haya almenos una mayuscula
    if digit and uper:
        return "El nombre de usuario es válido."
    else:
        return "El nombre de usuario no cumple con los requisitos."
    
def evaluateReactionTime(tiempo):
    match tiempo:
        #a la variable num se le asigna el valor de tiempo y se evalua la condicion 
        case num if num in range(0,200):
            print("categoria: rapido")
        case num if num in range(200,500):
            print("categoria: normal")
        case _:     #caso contrario
            print("categoria: lento")
  

  
def deleteVoid(list):
    """
    Remueve los items vacios; ya sean None, string vacios 
    o strings compuestos por espacio de una lista
    """
    while None in list:
        list.remove(None)
    while "" in list:
        list.remove("")
    while " " in list:
        list.remove(" ")



def evaluateAccent(word):
    """
    Retorna True si hay una vocal acentuada en el string enviado
    """
    #a pesar de que en este caso se va recibir un string en minusculas se busca darle reusabilidad al modulo
    acVowels=["Á","É","Í","Ó","Ú","á","é","í","ó","ú"]
    for i in word:
        if i in acVowels:
            return True
    else:
        return False

def replaceAccent(word):
    """
    Recibe un string y lo retorna libre de acentos en la vocales
    """
    bothVowels={"Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U","á":"a","é":"e","í":"i","ó":"o","ú":"u"}
    #junta los valores del key y el value en tuplas y los va asignando a acc y nor
    for acc,nor in bothVowels.items():
        word=word.replace(acc,nor)  #reemplaza todas las vocales acentuadas por su contraparte normal 
    return word

def printRound(round,n):
    if(n<5):
        print("\n Ronda: "+str(n)+"\n")
    else:
        print("\n Ronda Final: \n")

    header = f"{'Player':<10} {'Kills':<6} {'Assists':<8} {'Deaths':<7} {'MVPs':<5} {'Puntos':<7}"
    print(header)
    print('-' * len(header))

    for player, stats in round.items():
        row = f"{player:<10} {stats['kills']:<6} {stats['assists']:<8} {stats['deaths']:<7} {stats['MVPs']:<5} {stats['Puntos']:<7}"
        print(row)


def getMVP(data):
    maxPlayer=None
    maxValue=-1
    for player,points in data.items():
        if points>maxValue:
            maxPlayer=player
            maxValue=points
    return maxPlayer



def sortRound(round):
    sortedKeys=list(round.keys())
    for i in range(len(sortedKeys)):
        for j in range(i + 1, len(sortedKeys)):
            if round[sortedKeys[i]]['Puntos'] < round[sortedKeys[j]]['Puntos']:
                sortedKeys[i], sortedKeys[j] = sortedKeys[j], sortedKeys[i]
    sorted_dict = {x: round[x] for x in sortedKeys}
    return sorted_dict

def processRounds(rounds):

    roundImprimir={
    'Shadow':{'kills': 0, 'assists': 0, 'deaths':0,'MVPs':0,'Puntos':0},
    'Blaze':{'kills': 0, 'assists': 0, 'deaths':0,'MVPs':0,'Puntos':0},
    'Viper':{'kills': 0, 'assists': 0, 'deaths':0,'MVPs':0,'Puntos':0},
    'Frost':{'kills': 0, 'assists': 0, 'deaths':0,'MVPs':0,'Puntos':0},
    'Reaper':{'kills': 0, 'assists': 0, 'deaths':0,'MVPs':0,'Puntos':0},
    }
    
    
    puntuaciones=[3,1,-1]
    for nRound,roundAct in enumerate(rounds,start=1):   #Se crea una tupla conteniendo el diccionario de rondas y un numero asociado a cada una: ((1,ronda1),(2,ronda2))
        puntosAct={'Shadow':0,'Blaze':0,'Viper':0,'Frost':0,'Reaper':0,}
        for playerAct in roundAct:
            i=0
            for key,value in roundAct[playerAct].items():
                roundImprimir[playerAct][key]+=value
                puntosAct[playerAct]+=puntuaciones[i]*value
                i+=1
        #sumo toda la info a la ronda a imprimir
            roundImprimir[playerAct]['Puntos']+=puntosAct[playerAct]#puntosPlayerRoundAct
        roundImprimir[getMVP(puntosAct)]['MVPs']+=1       #!!!!
        roundImprimir=sortRound(roundImprimir)
        printRound(roundImprimir,nRound)
