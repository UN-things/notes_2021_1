def main():
    n = int(input("Ingrese n:\t"))

    p_1 = 1 / ((2 ** n) - 1)
    t = p_1
    for j in range(n):
        p_j = p_1 * (2 ** j)
        print(j+1, p_j)
        t += p_j
    print("Total", t)

if __name__ == "__main__":
    main()