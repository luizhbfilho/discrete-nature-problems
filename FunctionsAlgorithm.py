def composite_function(function1, function2, value):
    inner_value = calculate_function(function2, value)
    return calculate_function(function1, inner_value)

def calculate_function(function_str, val):
    return eval(function_str.replace('x', str(val)))

def main():
    print("Insira a função f(x):")
    f_str = input("f(x) = ").replace("^", "**")
    print("Insira a função g(x):")
    g_str = input("g(x) = ").replace("^", "**")

    while True:
        print("\nEscolha a função composta a ser calculada:")
        print("1. (g ° f)(x)")
        print("2. (f ° g)(x)")
        print("3. (f ° f)(x)")
        print("4. (g ° g)(x)")
        print("5. Sair")
        choice = int(input())

        if choice == 5:
            break

        value = int(input("\nInsira o valor de x: "))

        if choice == 1:
            result = composite_function(g_str, f_str, value)
            print(f"(g ° f)({value}) = {result}")
        elif choice == 2:
            result = composite_function(f_str, g_str, value)
            print(f"(f ° g)({value}) = {result}")
        elif choice == 3:
            result = composite_function(f_str, f_str, value)
            print(f"(f ° f)({value}) = {result}")
        elif choice == 4:
            result = composite_function(g_str, g_str, value)
            print(f"(g ° g)({value}) = {result}")

if __name__ == "__main__":
    main()

