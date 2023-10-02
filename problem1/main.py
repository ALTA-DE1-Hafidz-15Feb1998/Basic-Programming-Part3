# input
nama = input("Masukan Nama : ")
student_score = float(input("Masukan Score: "))

# Process: Your Solution Code Here
def konversi_nilai(student_score):
    if 80 <= student_score <= 100:
        return 'A'
    elif 65 <= student_score <= 79:
        return 'B+'
    elif 50 <= student_score <= 64:
        return 'B'
    elif 35 <= student_score <= 49:
        return 'C'
    elif 0 <= student_score <= 34:
        return 'D'
    else:
        return 'Nilai tidak valid'

# Output "Nilai A"
if student_score < 0 or student_score > 100:
    print("Nilai harus berada dalam rentang 0 hingga 100.")
else:
    nilai = konversi_nilai(student_score)
    print(f"Nilai : {nilai}")