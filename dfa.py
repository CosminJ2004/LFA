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
            nod_precedent = 0
            inceput = 0
            for litera in cuv2:
                # print(litera)
                if inceput==0:
                    for i in range(nr_tranzitii):
                        if tranzitii[i][1]==litera and int(tranzitii[i][0])==stare_init:
                            inceput=1
                            nod_precedent=int(tranzitii[i][2])


                            break
                    else:
                        # print({cuv2},"nu este acceptat")
                        g.write("NU\n")
                        break
                else:
                    for i in range(nr_tranzitii):
                        if tranzitii[i][1]==litera and int(tranzitii[i][0])==nod_precedent:
                            nod_precedent = int(tranzitii[i][2])
                            print("drum")
                            break
                    else:
                        # print({cuv2},"nu e acceptat")
                        g.write("NU\n")

                        break

            else:
                if int(nod_precedent) in stari_finale:
                    g.write("DA\n")
                else:
                    g.write("NU\n")
    g.close()






    # def delta(q,w):
    #     if w in tranzitii and

    # def delta_tilda(q,w):
    #     if len(w)==1:
    #         return delta(q,w)
    #     else:
    #         return delta_tilda(delta(q,w[0]),w[1:])









