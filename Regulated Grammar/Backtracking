with  open("input.txt") as f:
#citim din fisier si curatam de simboluri
    S=f.readline()
    P=[x.strip().split(' ') for x in f.readlines()]
    bad_chars = [',', '{', '}', "-", ">"]
    bad_chars2=['|','->',' ','\n']
    print(P)
    for x in P:
        x.remove('->')
        i=0
        while i< (len(x)):
            if x[i]=='|':
                del x[i]
                i=i-1
            i=i+1


    print(P)

    keys=[]
    values=[]
    val=[]
    #
    for x in P:
        val=[]
        keys.append(x[0])
        for i in range(1,len(x)):
            val.append(x[i])

        values.append(val)

    myDict = dict(zip(keys, values))

    print(myDict)
    grammar = [(k, v) for k, v in myDict.items()]

    # Printing list of tuple 
    print(grammar)
    #reguli ale gramaticii
    lista_finala=[]
    def generate_words(grammar, n):
        def backtrack(word, length):

            if length<=n:
                for rule in grammar:
                    if str(rule[0]) in word:
                        for i in range(len(rule[1])):
                            if len(word)-1+len(rule[1][i])==n:
                                ok = 1
                                for j in range(len(word.replace(rule[0],rule[1][i]))):
                                    if word.replace(rule[0],rule[1][i])[j].isupper():
                                        ok = 0
                                if len(word.replace(rule[0],rule[1][i])) == n and ok == 1:
                                    lista_finala.append(word.replace(rule[0],rule[1][i]))
                                    return
                else:
                    for rule in grammar:
                        if str(rule[0]) in word:
                            for i in range(len(rule[1])):
                                  if len(word) - 1 + len(rule[1][i]) <= n:
                                        backtrack(word.replace(rule[0],rule[1][i]),len(word)-1+len(rule[1][i]))


        for rule in grammar:
            if rule[0] == S[0]:  # Start with the initial symbol
                backtrack(rule[1][0], len(rule[1]))

    n =int(input("n= "))

    print(f"Cuvinte de lungime {n}:")
    generate_words(grammar, n)
    print(list(set(lista_finala)))
    #facem set de cuvinte facute pentru a nu se repeta anumite cuvinte
    cuv=input("cuvant=")
    lungime=len(cuv)
    generate_words(grammar,lungime)
    if cuv in lista_finala:
        print("ok")
    else:
        print("nu")
    #am verif daca un cuvant se afla in limbaj sau nu
