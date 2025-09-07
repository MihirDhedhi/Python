import math
degrees = 90
radians = math.radians(degrees)
print(f"{degrees} degrees is equal to {radians} radians.")




import math
x = 2
y = 6 * x**2 + 4 * math.sin(x)
print(f"The value of y is {y}")




import math
def evaluate_functions(x):
    fx = math.cos(2 * x)
    f_prime_x = -2 * math.sin(2 * x)
    f_double_prime_x = -4 * math.cos(2 * x)
    return fx, f_prime_x, f_double_prime_x
x = math.pi
fx_val, f_prime_x_val, f_double_prime_x_val = evaluate_functions(x)
print(f"For x = π:")
print(f"f(x) = cos(2x) = {fx_val}")
print(f"f'(x) = -2sin(2x) = {f_prime_x_val}")
print(f"f''(x) = -4cos(2x) = {f_double_prime_x_val}")