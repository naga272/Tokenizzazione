import re


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
    
    a = re.split(r"[/\*\-\+\s()]\s*", stri) # contenitore numeri
    b = re.split(r"[\d\s]\s*", stri) # contenitore operandi / parentesi
    '''
        *
        *  Uso la funzione rimuovi_elementi(x) per togliere dalle due liste gli elementi vuoti
        *  che si vanno a generano dal re.split()
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
        a.insert(z - 1, risolvi(d, c))
    return risolvi(a, b)


def risolvi(a, d):
    i = 0
    while i < len(d):
        if '*' in d:
            z = 0
            while d[z] != '*':
                z += 1
            if d[z] == '*':
                d.remove(d[z])
                a[z] = str(int(a[z]) * int(a[z + 1]))
                a.remove(a[z + 1])
                
        if '%' in d:
            z = 0
            while d[z] != '%':
                z += 1
            if d[z] == '%':
                a.remove(a[z + 1])
                d.remove(d[z])
                a[z] = str(int(a[z]) % int(a[z + 1]))
                a.remove(a[z + 1])

        if '/' in d:
            z = 0
            while d[z] != '/':
                z += 1

            if d[z] == '/':
                d.remove(d[z])
                a[z] = str(int(a[z]) // int(a[z + 1]))
                a.remove(a[z + 1])

        if '*' not in d and '/' not in d and '%' not in d:
            try:
                if len(d) >= 1:
                    if d[0] == '+':
                        d.remove(d[0])
                        a[0] = str(int(a[0]) + int(a[1]))
                        a.remove(a[1])
                    if d[0] == '-':
                        d.remove(d[0])
                        a[0] = str(int(a[0]) - int(a[1]))
                        a.remove(a[1])
            except Exception:
                return int(a[0])
    return int(a[0])


if __name__ == "__main__":
    a = ['22', '33', '5']
    d = ['*', '-']
    print(main("22 * 3 / 12 % 5"))
