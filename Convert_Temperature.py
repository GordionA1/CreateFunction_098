def converts_temperature(value,unit):
    if unit.upper == 'C' :
        return (value *9/5) + 32
    elif unit.upper == 'F' :
        return (value -32) * 5/9
    else :
        print ("unit harus 'C' atau 'f' ")

print("========KONVERSI SUHU=======")

input_suhu = float(input("Masukkan nilai suhu:"))
unit = input("Masukkan satuan suhu ('C' untuk celcius atau 'F' untuk Fahrenheit):")
konversi = converts_temperature(input_suhu, unit)

