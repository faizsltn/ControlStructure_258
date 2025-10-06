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

