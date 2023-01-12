#rövarspråket

def codifica(input):    #traduttore i -> r
    ret = ''
    vocali = ['a','e','i','o','u']
    speciali = [" ", ",", ".", "?", "!", '"',"'"]

    for i in range(len(input)):
        if input[i] in vocali or input[i] in speciali:
            ret += input[i]
        else:
            ret += (input[i] + 'o' + input[i])
    return ret

def decodifica(input):    #traduttore r -> i
    ret = ''
    vocali = ['a','e','i','o','u']
    speciali = [" ", ",", ".", "?", "!", '"',"'"]

    for i in range(len(input)):
        if input[i] in vocali or input[i] in speciali:
            ret += input[i]
        elif i + 1 < len(input) and input[i + 1] == 'o':
            if i+2 < len(input) and input[i+2] == input[i]:
                ret += input[i]
    return ret

def controllo(input):
    check = decodifica(input)
    if (codifica(check)) == input:
        ret = 'Traduzione affidabile!'
    else:
        ret = 'Attenzione, traduzione non affidabile!'
    return ret

continuita = True
while continuita == True:
    print('Vuoi tradurre dall\'Italiano[1] o in Italiano[2]?')     #scelta opzione di traduzione
    scelta = input('Inserisci il numero della casella scelta: ')

    if scelta == '1':
        stringa = input('Inserire frase/parola da tradurre in rövarspråket: ')     #input della I stringa da tradurre
        print('Input codificato: ' +codifica(stringa))
    elif scelta == '2':
        stringa = input('Inserire frase/parola da tradurre in italiano: ')     #input della II stringa da tradurre
        print('Input decodificato: ' +decodifica(stringa))
        print(controllo(stringa))

    risposta = input('Vuoi tradurre altro? si/no: ')    #continuità del ciclo
    if risposta == 'no':
        continuita = False
    else:
        continuita = True