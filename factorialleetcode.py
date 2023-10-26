x = int(input('Enter a positive natural number please!: '))

def factorial():
   
    factlist = list()
    for i in range(1, x + 1):
        x_fact = 1
        x_fact = x_fact * i
        print(x_fact)
        factlist.append(x_fact)
        print(factlist)
       
factorial()