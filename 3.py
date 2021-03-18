a = int(input("Nilai Ujian Teori : "))
b = int(input("Nilai Ujian Praktek : "))

if a >= 70 and b >= 70:
    print("Selamat, Anda lulus!")
elif a >= 70 and b < 70:
    print("Anda harus mengulang ujian praktek")
elif a < 70 and b >=70:
    print("Anda harus mengulang ujian teori")
elif a < 70 and b < 70:
    print("Anda harus mengulang ujian teori dan praktek")