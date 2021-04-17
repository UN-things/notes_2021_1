import random
import math

def main():
    beta = float(input("Ingrese beta:\t"))
    repetitions = int(input("Ingrese la cantidad de repeticiones:\t"))
    real = 0
    for i in range(repetitions):
        c = round(random.uniform(-beta, beta), 3)
        b = round(random.uniform(-beta, beta), 3)
        if(b**2 >= c):
            real += 1
    area = 4 * (beta ** 2)
    curve = (4 * math.sqrt(beta ** 3)) / 3

    teo_probability = (area - curve) * 100 / area
    sim_probability = (real/repetitions)

    print("La probabilidad teórica de obtener un resultado real es del {}%."\
        .format(round(teo_probability, 3)))
    print("La probabilidad simulada de obtener un resultado real es del {}%."\
        .format(round(sim_probability, 3) * 100))

if __name__ == "__main__":
    main()