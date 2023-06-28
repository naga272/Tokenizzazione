import re


EXIT_FAILED = -1


def rimuovi_elementi(x):
    try:
        for i in range(0, len(x), 1):
            x.remove("")
        return x
    except Exception:
        return x


def main(stri): #compile e match
    #pattern per requisiti stringa
    reg1 = re.compile(r"\s*\d+\s*[/*+%\-\(\)]*\s*\d+\s*")
    
    if (not reg1.match(stri)):
        print("syntax error!")
        return EXIT_FAILED

    a = re.split(r"[/\*\-\+\s()%]\s*", stri) # contenitore numeri
    b = re.split(r"[\d\s]\s*", stri) # contenitore operandi / parentesi
    '''
        *
        *  Uso la funzione rimuovi_elementi(x) per togliere dalle due liste gli elementi vuoti
        *  che si vanno a generare dal re.split()
        *
    '''
    a = rimuovi_elementi(a) 
    b = rimuovi_elementi(b)
    c = []
    d = []
    i = 0

    if "(" in stri:
        while b[i] != "(":        
            i += 1
        b.remove(b[i])

        z = 0
        while b[i] != ")":
            c.append(b[i])
            b.remove(b[i])
            d.append(a[i])
            a.remove(a[i])
            z += 1
        d.append(a[i])
        a.remove(a[i])
        b.remove(b[i])

        # print(c) # c gli operatori dentro alle parentesi
        a.insert(z, risolvi(d, c)) # d contine numeri dentro alla parentesi

    print(stri) # input 
    print(b)    # contiene gli operatori fuori dalle parentesi tonde
    print(a)    # contiene gli operandi
    print(c)    # contiene gli operatori all'interno delle parentesi tonde
    print(d)    # contiene gli operandi all'interno delle parentesi tonde 
    return risolvi(a, b)


def risolvi(numeri, operatori):
    print("\n")
    while operatori != []:
        z = 0
        if '*' in operatori or '/' in operatori or '%' in operatori:
            while operatori[z] != '*' or operatori[z] != '/' or oroperatori[z] != '%': 
                if operatori[z] == '*':
                    operatori.remove(operatori[z])
                    numeri[z] = str(int(numeri[z]) * int(numeri[z + 1])) 
                    numeri.remove(numeri[z + 1])
                    break

                if operatori[z] == '/':
                    operatori.remove(operatori[z])
                    numeri[z] = str(int(numeri[z]) // int(numeri[z + 1])) 
                    numeri.remove(numeri[z + 1])
                    break

                if operatori[z] == '%':
                    operatori.remove(operatori[z])
                    numeri[z] = str(int(numeri[z]) % int(numeri[z + 1])) 
                    numeri.remove(numeri[z + 1])
                    break
                z += 1
        else:
            if operatori != []:
                if operatori[0] == '+':
                    operatori.remove(operatori[0])
                    numeri[0] = str(int(numeri[0]) + int(numeri[1]))
                    numeri.remove(numeri[1])

            if operatori != []:
                if operatori[0] == '-':
                    operatori.remove(operatori[0])
                    numeri[0] = str(int(numeri[0]) - int(numeri[1]))
                    numeri.remove(numeri[1])
    return int(numeri[0])


if __name__ == "__main__":
    x = "22 * 33 + 15 - 22 / 2 + 2 / 10"
    print(f"risultato di {x}: {main(x)}") #main("22 * 3 / 12 % 5")
