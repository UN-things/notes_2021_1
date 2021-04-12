CONST = 273.15
def kelvin_to_celsius(k):
    result = k - CONST
    return result

def kelvin_to_fahrenheit(k):
    result = ((9 * (k - CONST)) / 5) + 32
    return result

def fahrenheit_to_celsius(f):
    result = (5 * (f - 32)) / 9
    return result

def fahrenheit_to_kelvin(f):
    result = ((5 * (f - 32)) / 9) + CONST
    return result

def celsius_to_kelvin(c):
    result = c + CONST
    return result

def celsius_to_fahrenheit(c):
    result = (9 * c / 5) + 32
    return result

def select_function(option, temperature):
    switcher = {
        1: kelvin_to_celsius(temperature),
        2: kelvin_to_fahrenheit(temperature),
        3: fahrenheit_to_celsius(temperature),
        4: fahrenheit_to_kelvin(temperature),
        5: celsius_to_kelvin(temperature),
        6: celsius_to_fahrenheit(temperature)
    }

    return switcher.get(option, "Opción inválida\n")

def main():
    print("\n\tElija la operación de conversión:\n\n\
        1) Kelvin a Celsius\n\
        2) Kelvin a Fahrenheit\n\
        3) Fahrenheit a Celsius\n\
        4) Fahrenheit a Kelvin\n\
        5) Celsius a Kelvin\n\
        6) Celsius a Fahrenheit\n")
    option = int(input())
    print("Ingrese la temperatura que desea convertir.\n")
    temperature = float(input())
    print("\nEl resultado de la operación es:\n")
    print(select_function(option, temperature), '\n')


if __name__ == "__main__":
    main()