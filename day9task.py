""" 1.) You are given a string sentence . Print the characters at even indices, sentence = "Python is amazing" . """
sentence = "Python is amazing"
for i in range(0,len(sentence),2):
    print(sentence[i],end='')

""" 2.) You are given a string s . Replace all spaces in the string with underscores
and print the modified string. s = "Python is fun and powerful". """

name_1 = "Python is fun and powerful"
replacing = name_1.replace(" ","_")
print(replacing)

""" 3.) You are given a string s . Check if the string contains only digits. s = "12345" """
s = "12345"
digit_check = s.isdigit()
print(digit_check)

""" 4.) You are given a string s . Print the string in reverse order.  s = "Python is amazing" ."""
sentence_1 = "Python is amazing"
reverse_1 = sentence_1[::-1]
print(reverse_1)

""" 5.) You are given a string sentence_2 . Capitalize the first letter of each word in the string 
and print the modified string. s = "python programming is fun" . """

sentence_2 = "python programming is fun"
capitalizing = sentence_2.title()
print(capitalizing)