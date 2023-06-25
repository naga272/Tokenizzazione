import re


#COSTANTI
EXIT_SUCCESS = 0
EXIT_FAILED = 1


def rimuovi_elementi(x):
    try:
        for i in range(0, len(x), 1):
            x.remove("")
    except Exception:
        return x


def main(stri): #compile e match
    #pattern per requisiti stringa
    reg1 = re.compile(r"\s*\d+\s*[/*+%\-\(\)]*\s*\d+\s*")
    
    if (not reg1.match(stri)):
        print("syntax error!")
        return False
    
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


def risolvi(a, d):
    while len(d) > 0:
        while '*' in d or '/' in d or '%' in d:
            c = 0
            while d[c] != '*' and d[c] != '/' and d[c] != '%':
                c += 1

            if len(d) > 0:
                if d[c] == '*':
                    a[c] = str(int(a[c]) * int(a[c + 1]))
                    a.remove(a[c + 1])
                    d.remove(d[c])

            try:
                if len(d) > 0:
                    if d[c] == '/':
                        a[c] = str(int(a[c]) // int(a[c + 1]))
                        a.remove(a[c + 1])
                        d.remove(d[c])

                    if d[c] == '%':
                        a[c] = str(int(a[c]) % int(a[c + 1]))
                        a.remove(a[c + 1])
                        d.remove(d[c])
                else:
                    return int(a[0])
            except Exception:
                return a[0]
        
        try:
            while len(d) > 0:
                if d[c] == '+':
                    a[c] = str(int(a[c]) + int(a[c + 1]))
                    a.remove(a[c + 1])
                    d.remove(d[c])

                if d[c] == '-':
                    a[c] = str(int(a[c]) - int(a[c + 1]))
                    a.remove(a[c + 1])
                    d.remove(d[c])
        except Exception:
            return a[0]
    return a[0]


if __name__ == "__main__":
    a = ['22', '33', '5', '6']
    d = ['*', '-', '/']
    print(main("22 * (3 + 12) % 5")) #main("22 * 3 / 12 % 5")
