def prime_number(num):
    if num <= 1:
        return "Not Prime"  # Bilangan negatif, 0, dan 1 bukan bilangan prima
    
    if num <= 3:
        return "Prime"  # 2 dan 3 adalah bilangan prima

    if num % 2 == 0:
        return "Not Prime"  # Bilangan genap selain 2 bukan bilangan prima

    # Memeriksa faktor dari 3 hingga akar kuadrat dari bilangan
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return "Not Prime"

    return "Prime"


if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"