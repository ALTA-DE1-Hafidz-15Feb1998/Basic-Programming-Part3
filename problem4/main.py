def palindrome(input_string):
    # Menghapus spasi dan mengubah huruf menjadi huruf kecil agar tidak sensitif terhadap huruf besar/kecil
    input_string = input_string.replace(" ", "").lower() 
    # Membalikkan string
    reversed_string = input_string[::-1]  
    # Memeriksa apakah string asli dan string yang dibalik sama
    return input_string == reversed_string

if __name__ == '__main__':
    print(palindrome("civic")) # True
    print(palindrome("katak")) # True
    print(palindrome("kasur rusak")) # True
    print(palindrome("kupu-kupu")) # False
    print(palindrome("lion")) # False