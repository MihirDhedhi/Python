f = open(r"C:\Users\mihir\ICT\sem-3\PWP\Spyder\ict.txt", "r")
data = f.read()
f.close()

lines = data.split("\n")
words = data.split()
chars = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Chars:", chars)







f1 = open(r"C:\Users\mihir\ICT\sem-3\PWP\Spyder\ict.txt", "r")

lines = f1.readlines()
f1.close()

print(lines)








import csv

f3 = open(r"C:\Users\mihir\ICT\sem-3\PWP\Spyder\ict.txt", "r")
reader = csv.reader(f3)

for row in reader:
    print(row)

f3.close()








f1 = open(r"C:\Users\mihir\ICT\sem-3\PWP\Spyder\ict.txt", "r")
f2 = open(r"C:\Users\mihir\ICT\sem-3\PWP\Spyder\ict(1).txt", "r")

data1 = f1.read()
data2 = f2.read()

f1.close()
f2.close()

f3= open(r"C:\Users\mihir\ICT\sem-3\PWP\Spyder\merged.txt", "w")
f3.write(data1)
f3.write(data2)
f3.close()

print("Files merged into merged.txt")