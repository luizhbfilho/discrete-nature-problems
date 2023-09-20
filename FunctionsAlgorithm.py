def f(x): 
    return x ** 2;

def g(x):
    return x - 1;

def g_of_f(x):
    return g(f(x))  # (g ° f)(x)

def g_of_g(x):
    return g(g(x))  # (g ° g)(x)

def f_of_f(x):
    return f(f(x))  # (f ° f)(x)

def f_of_g(x):
    return f(g(x))  # (f ° g)(x)

x = 4

print(f"g(f({x})) = {g_of_f(x)}")
print(f"g(g({x})) = {g_of_g(x)}")
print(f"f(f({x})) = {f_of_f(x)}")
print(f"f(g({x})) = {f_of_g(x)}")
