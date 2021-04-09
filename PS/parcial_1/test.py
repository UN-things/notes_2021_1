import numpy as np

def model(x):
    k = 20
    nat = 4
    mor = 0
    if x == 2:
        y = (nat - mor) * ((x-1)**2)/k
        return y;
    else:
        y = (nat - mor) * (model(x-1)**2)/k
        print(x, y)
        return y;

def main():
    print(model(20))


if __name__ == "__main__":
    main()