text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)





text = input("Enter a string: ")
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")





text = input("Enter a string: ")
if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")





sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)





sentence = input("Enter a sentence: ")
words = sentence.split()
last_word_length = len(words[-1])
print("Length of the last word:", last_word_length)
