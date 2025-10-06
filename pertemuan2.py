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