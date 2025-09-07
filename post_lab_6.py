num = 1
while num <= 100:
    if num % 2 != 0:
        print(num, end=' ')
        num += 1




n = int(input("Enter n: "))
sum_n = n * (n + 1) // 2
print("Sum of natural numbers from 1 to", n, "is:", sum_n)





def count_digits(number):
    return len(str(abs(number)))

num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))



num = int(input("Enter a number: "))
num_str = str(abs(num))
first_digit = num_str[0]
last_digit = num_str[-1]
print("First digit:", first_digit)
print("Last digit:", last_digit)



num = input("Enter a number: ")
if len(num) > 1:
    swapped = num[-1] + num[1:-1] + num[0]
else:
    swapped = num
print("Number after swapping first and last digits:", swapped)




num = int(input("Enter a number: "))
product = 1
for digit in str(abs(num)):
    product *= int(digit)
print("Product of digits:", product)




num = input("Enter a number: ")
reversed_num = num[::-1]
print("Reversed number:", reversed_num)
