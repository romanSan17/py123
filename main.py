
logs = []

def liitumine(a,b):
    logs.append('liitumine')
    if isinstance (a, str) or isinstance (b, str):
        print ("Vale andmed")
        return ""
    return a+b

print (liitumine (9, 5))



def lahuta(a,b):
    logs.append('lahuta')
    if isinstance (a, str) or isinstance (b, str):
        print ("Vale andmed")
        return ""
    return a-b

print (lahuta (9, 5))

def umnozh(a,b):
    logs.append('umnozh')
    if isinstance (a, str) or isinstance (b, str):
        print ("Vale andmed")
        return ""
    return a*b

print (umnozh (9, 5))

def deleniye(a,b):
    try:
        logs.append('deleniye')
        if isinstance (a, str) or isinstance (b, str):
            print ("Vale andmed")
            return ""
        return a/b
    except ZeroDivisionError:
        print ("ei saa jagada null") 

print (deleniye (9, 0))

def logsKuuvamine(logs):
    jag = 0
    korr = 0
    liit = 0
    lahut = 0
    for elem in logs:
        if elem == 'liitumine':
            liit += 1
        elif elem == 'lahuta':
            lahut += 1
        elif elem == 'umnozh':
            korr += 1
        else:
            jag += 1
    return [jag, korr, liit, lahut]

print(logsKuuvamine(logs))