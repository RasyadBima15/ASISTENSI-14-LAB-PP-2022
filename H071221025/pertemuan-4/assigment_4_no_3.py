bilangan = int(input("bilangan bulat : "))

def faktorial(bilangan):
    if bilangan > 1 :
        return bilangan*faktorial(bilangan-1)

    return 1

print(f"{bilangan}! = {faktorial(bilangan)}") 