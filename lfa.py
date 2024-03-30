with open("output.txt","w") as g:
    with  open ("input.txt") as f:

        nr_stari=int(f.readline())
        print(nr_stari)
        stari=[int(x) for x in f.readline().split()]
        print(stari)
        nr_muchii=int(f.readline())
        print(nr_muchii)
        muchii=[x for x in f.readline().split()]
        print(muchii)
        stare_init=int(f.readline())
        print(stare_init)
        nr_stari_finale=int(f.readline())
        print(nr_stari_finale)
        stari_finale=[int(x) for x in f.readline().split()]
        print(stari_finale)
        nr_tranzitii=int(f.readline())
        tranzitii=[]
        v=[0 for x in range(nr_tranzitii)]*nr_tranzitii
        for x in range(nr_tranzitii):
            tranzitii.append([x for x in f.readline().split()])
        # for i in range(nr_tranzitii):
        #     v[int(tranzitii[i][0])][i]=tranzitii[i][2];

        print(tranzitii)
        nr_cuvinte=int(f.readline())
        print(nr_cuvinte)
        cuvinte=[]
        for i in range (nr_cuvinte):
            cuvinte.append(f.readline().split())
        print(cuvinte)

    # for i in range(nr_tranzitii):
    #     print(tranzitii[i][2])

    inceput=0;
    for cuv in cuvinte:
        for cuv2 in cuv:
            nod_precedent = []
            nod_precedent2 = []

            inceput = 0
            cuv2=cuv2[::-1]
            for litera in cuv2:
                # print(litera)

                ok=1
                if inceput==0:
                    for i in range(nr_tranzitii):
                        if tranzitii[i][1]==litera and int(tranzitii[i][2]) in stari_finale:
                            inceput=1
                            nod_precedent.append(int(tranzitii[i][0]))
                            ok=0
                    if ok==1:
                        # print({cuv2},"nu este acceptat")
                        g.write("NU\n")
                        break
                else:
                    for i in range(nr_tranzitii):
                        if tranzitii[i][1]==litera and int(tranzitii[i][2]) in nod_precedent:
                            nod_precedent2.append(int(tranzitii[i][0]))
                            # print("drum")
                            ok=0
                    if(ok==1):
                        # print({cuv2},"nu e acceptat")
                        g.write("NU\n")
                        break
                    nod_precedent = nod_precedent2;
                    nod_precedent2=[]

            else:
                if stare_init in nod_precedent:
                    g.write("DA\n")
                else:
                    g.write("NU\n")
    g.close()