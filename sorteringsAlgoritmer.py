import random, math, sys

def bogoSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    isSorted = None # Boolean til markering af, om listen er sorteret
    attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
    while not isSorted:
        attempts += 1
        if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
            print('Afbryder på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
            items.sort()
            return items
        random.shuffle(items) # Bland alle elementer helt tilfældigt
        isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
        # ...og prøver i denne løkke at bevise det modsatte
        for index in range(len(items)-1):
            if items[index] > items[index+1]:
                isSorted = False
                break # Bryd løkken hvis et eneste element er forkert sorteret
    print('Sorteret efter {} forsøg'.format(attempts))
    return items



def bubbleSort(CopyCat):
    CopyCat = CopyCat.copy()
    PlaceHolder = 0

    for x in range(len(CopyCat)):
        for y in range(len(CopyCat)-1):
            if CopyCat[y] > CopyCat[y+1]:
                Placeholder = CopyCat[y+1]
                CopyCat[y+1] = CopyCat[y]
                CopyCat[y] = PlaceHolder

    return CopyCat


def InsertionSort(CopyCat):
    Min = 0
    PlaceHolder = 0
    CopyCat = CopyCat.copy()

    for x in range(len(CopyCat)):
        Min = x
        for y in range(x, len(CopyCat), 1):
            if CopyCat[Min]>CopyCat[y]:
                Min = y
            PlaceHolder = CopyCat[x]
            CopyCat[x] = CopyCat[Min]
            CopyCat[Min] = PlaceHolder

    return CopyCat



if __name__ == '__main__':
    for i in range(10):
        listen = list(range(1, 8))
        sorteret = InsertionSort(listen)
        random.shuffle(listen)
        print('Shuffled:\t', listen)
        print('Sorted:\t\t', sorteret)
        print('==============================================================')
