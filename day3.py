data = open('input/03').read().strip()
total = 0
inMul = False
todo = True
global i
i = 0

def nextToken():
    global i
    global data
    i += 1
    return data[i]

def currToken():
    global i
    global data
    return data[i]

def hasNext():
    global i
    global data

    return len(data)-1>i

def handleMul():
    global i
    global data
    global total
    global inMul
    a = ''
    while currToken().isdigit() and hasNext():
        a = a + currToken()
        if hasNext():
            nextToken()
    if currToken() != ',':
        inMul = False
        if hasNext():
            nextToken()
        return 
    nextToken()
    b =  ''
    while currToken().isdigit() and hasNext():
        b = b + currToken()
        if hasNext():
            nextToken()
    if currToken() != ')' or (not a.isdigit()) or (not b.isdigit()):
        inMul = False
        if hasNext():
            nextToken()
        return 
    total = int(a)*int(b) + total
    if hasNext():
        nextToken()
    inMul = False
while hasNext():
    if inMul and todo:
        handleMul()
    
    if currToken() == 'd':
        if hasNext():
            if nextToken() == 'o':
                if hasNext():
                    tok = nextToken()
                    if tok == 'n' and hasNext() and  nextToken() == "'"  and hasNext() and nextToken() == 't' and hasNext() and nextToken() == '('  and hasNext() and nextToken() == ')':
                        todo = False
                    if  tok == '('  and hasNext() and nextToken() == ')':
                        todo = True

    if currToken() == 'm':
        if hasNext():
            if nextToken() == 'u' and hasNext() and  nextToken() == 'l' and hasNext() and  nextToken() == '(':
                inMul = True
                if hasNext():
                    nextToken()
                continue
    i += 1

print(total)
