from math import sqrt

from sympy import symbols, pi, integrate, sqrt, E


def calc_avg_x(x: list[float]) -> float:
    result = 0
    for i in x:
        result += i

    return result / len(x)


def calc_S_sq(x: list[float]) -> float:
    result = 0
    avg = calc_avg_x(x)

    for i in x:
        result += i ** 2

    result -= avg ** 2
    result /= len(x)

    return result


def task1() -> None:
    x = [9.1, 8.6, 9.1, 8.1, 6.6, 10.1, 9.8, 11.1, 14.4, 11.6]
    x_check = 8
    a = 0.05
    Tna = 2.294

    Tn = (x[x_check] - calc_avg_x(x)) / sqrt(calc_S_sq(x))

    print(f"{Tn = }")
    if Tn > Tna:
        print(f"Tn > Tna, гіпотеза відкидається, x не є помилковим, при N={len(x)}, a={a}")
    else:
        print(f"Tn < Tna, гіпотеза приймається, x є помилковим, при N={len(x)}, a={a}")


def task2() -> None:
    A = 1
    B = 3

    xs = [3.13, 2.91, 0.73, 1.5, 3.93, 2.03, 1.6, 1.45, 2.48, 2.6, 1.91, 2.1, 2.51, 1.07, 1.84, 0.24, 2.24, 4.02]
    x_filtered = []
    n1 = 0
    n3 = 0

    for x in xs:
        if x < A:
            n1 += 1
        elif x > B:
            n3 += 1
        else:
            x_filtered.append(x)

    n2 = len(x_filtered)
    print(f"N1 = {n1}")
    print(f"N2 = {n2}")
    print(f"N3 = {n3}")

    avg = calc_avg_x(x_filtered)
    sq0 = calc_S_sq(x_filtered)
    so0 = sqrt(sq0)
    a0 = (A - avg) / so0
    b0 = (B - avg) / so0

    print("0:")
    print(f"    Математичне очікування x0: {avg:.2f}")
    print(f"    Дисперсія S0^2: {sq0:.2f}")
    print(f"    СКВ S0: {so0:.2f}")

    print(f"    a0: {a0:.2f}")
    print(f"    b0: {b0:.2f}")
    print()

    t, x, su, so, a, b = symbols("t, x, su, so, a, b", real=True)

    fx = (1 / sqrt(2 * pi)) * E ** (-(t ** 2) / 2)
    Fx = (1 / sqrt(2 * pi)) * integrate(E ** (-(t ** 2) / 2), (t, 0, x))

    avgn = avg
    sqn = sq0
    son = so0
    an = a0
    bn = b0
    for n in range(2):
        fxan = fx.evalf(subs={t: an})
        Fxan = Fx.evalf(subs={x: an})
        fxbn = fx.evalf(subs={t: bn})
        Fxbn = Fx.evalf(subs={x: bn})

        avgn = avg - son * (n1 / n2) * (fxan / Fxan) + son * (n3 / n2) * (fxbn / (1 - Fxbn))
        sqn = sq0 + (avg - avgn) ** 2 - sqn * (n1 / n2) * an * (fxan / Fxan) + \
              sqn * (n3 / n2) * bn * (fxbn / (1 - Fxbn))

        son = sqrt(sqn)

        an = (A - avgn) / sqn
        bn = (B - avgn) / sqn

        print(f"{n+1}:")
        print(f"    Математичне очікування x{n+1}: {avgn:.2f}")
        print(f"    Дисперсія S{n+1}^2: {sqn:.2f}")
        print(f"    СКВ S{n+1}: {son:.2f}")
        print(f"    a{n+1}: {an:.2f}")
        print(f"    b{n+1}: {bn:.2f}")


def main() -> None:
    print("Завдання 1")
    task1()

    print()

    # print("Завдання 2")
    # task2()


if __name__ == '__main__':
    main()
