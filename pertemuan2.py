percent = float(input("Masukkan persentase nilai siswa (0-100): "))
nilai = percent
if percent >= 90 :
    print("Excellent performance")
elif percent >= 80 :
    print("Very Good performance")
elif percent >= 70 :
    print("Good performance")
elif percent >= 60 :
    print("Average performance")
else : 
    print("Need to Improve!")


print("find largest of three numbers!")
number1 = int(input("masukkan angka pertama:"))
number2 = int(input("masukkan angka kedua:"))
number3 = int(input("masukkan angka ketiga:"))

if (number1 >= number2) and (number1 >= number3):
    largest = number1
elif (number2 >= number1) and (number2 >= number3):
    largest = number2
else : 
    largest = number3

print("\nhasil perhitungan")
print(f"dari numbers {number1}, {number2}, and {number3},")
print(f"angka yang terbesar adalah : {largest}")

print("print Fibonacci series up to n!")
n = int(input("Masukkan jumlah suku: "))
angkapertama = 0
angkakedua = 1
suku_ke = 0

if n <= 0:
    print(f"masukkan angka.")
elif n == 1:
    print(f"fibonacci hingga suku ke-{n}:")
    print(angkapertama)

else :
    print(f"fibonacci hingga suku ke-{n}:")

    while suku_ke < n:
        print(angkapertama, end='')
        suku_berikutnya = angkapertama + angkakedua
        angkapertama = angkakedua
        angkakedua = suku_berikutnya

        suku_ke += 1
        print()


print("print odd numbers up to n!")
n = int(input("Masukkan sebuah angka batas (n): "))

if n <= 0:
        print("masukkan angka yang lebih besar.")
else:
        print(f"\nbilangan ganjil dari 1 hingga {n}:")
        for angka in range(1, n + 1, 2):
             print(angka, end=' ')
        print()
