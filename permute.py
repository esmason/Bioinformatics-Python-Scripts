def permutList(l):
    listOfPerm = []
    if len(l)== 1:
        return [l]
    else:

        for p in permutList(l[1:]):
            for i in range((len(p) + 1) ):
                t=list(p)

                t.insert(i , l[0])
                
                listOfPerm.append(t)

    return listOfPerm
        

        


def permut(n):
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    ll = [1, 2, 3, 4]
    ll.insert(4, 33)
    print(ll)

    lista=permutList(numbers)
    lenList = len(lista)
    for l in lista:
        for t in l:
            print(str(t) + ' ', end='')
        print('\n')
    print(lenList)
