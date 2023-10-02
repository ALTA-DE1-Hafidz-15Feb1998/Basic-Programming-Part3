# Input
bilangan = int(input("Masukkan bilangan: "))

# Process
def faktor(bilangan):
    for i in range(1, bilangan + 1):
        if bilangan % i == 0:
            print(i)

# Output
print(f"Faktor dari {bilangan} adalah:")
faktor(bilangan)