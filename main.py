year = int(input("Introduce un año: "))

if year >= 1582:  # Verifica si está dentro del período del calendario Gregoriano
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Año bisiesto")
    else:
        print("Año común")
else:
    print("No dentro del período del calendario Gregoriano")
	