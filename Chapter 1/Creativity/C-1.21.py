done = False
lines =[]

while not done:
    try:
        line = input('Enter text, i shall print it in reversed order, ctrl-d to stop')
        lines.append(line)
    except (EOFError):
        print("End of file")

        for x in range(len(lines)-1 , -1, -1):
            print(x, lines[x])

            done = True
        print(len(lines))
        
            
