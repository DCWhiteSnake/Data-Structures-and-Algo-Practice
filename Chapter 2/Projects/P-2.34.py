with open('lorem1000.txt','r') as file:
    countriesStr = file.read()

stream_book = ""
for y in range(len(countriesStr)):
    if countriesStr[y] == '\n':
        pass
    else:
        stream_book += countriesStr[y].lower()

dicti= {}
alphabets = list("abcdefghijklmnopqrstuvwxyz")

for p in range(len(stream_book)):
    if stream_book[p] in alphabets:
        if dicti.get(stream_book[p]) == None:
            dicti[stream_book[p]] = 1
        else:
           dicti[stream_book[p]] += 1
    else:
        pass

for key in dicti.keys():
    count = ""
    if(dicti[key] > 0):
        for c in range(dicti[key]):
            count += "."
    print(key, count)
        
    


        
            
            
        

   
