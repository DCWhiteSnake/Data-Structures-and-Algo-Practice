
print("Put the sequence you wish to evaluate here" )


def oddproduct(listofintegers):
    listofintegers = listofintegers.split(',')
    found = False
    product = 0
    if(len(listofintegers) == 1):
        print("Your sequence must be greater than 1")
    else:
        try:
            for x in range(len(listofintegers)):
                for y in range(x+1, len(listofintegers)):
                    product = int(listofintegers[x]) * int(listofintegers[y])
                    if product % 2 == 1:
                        found = True
                        break
            print( found)
        except IndexError:
            print("Problems with index")
        

    
oddproduct(input())
