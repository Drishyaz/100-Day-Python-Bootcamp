# LIST COMPREHENSION
# new_list = [new_item for item in list]
# YOU ADD 1 TO EACH ITEM IN LIST
numbers = [1,2,3]
num_list = [n+1 for n in numbers]
print(num_list)                                     # [2, 3, 4]

# TURN THE STRING INTO A LIST OF CHARACTERS
name = "drishya"
char_list = [letter for letter in name]
print(char_list)                                     # ['d', 'r', 'i', 's', 'h', 'y', 'a']

# DOUBLE EACH ITEM IN THE RANGE
doubles = [n*2 for n in range(1,5)]
print(doubles)                                     # [2, 4, 6, 8]

# CONDITIONAL LIST COMPREHENSION
# new_list = [item for item in list if test]
# PRINT ONLY THE NAMES WHICH HAVE LENGTH <= 4
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)                                     # ["Alex", "Beth", "Dave"]

# LIST OF NAMES WITH LENGTH > 5 IN ALL CAPS
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)                                     # ['CAROLINE', 'ELEANOR', 'FREDDIE']

# LIST OF SQUARED NUMBERS
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n*n for n in numbers]
print(result)                                         # [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

# LIST OF ONLY THE EVEN NUMBERS
result = [n for n in numbers if n % 2 == 0]
print(result)                                         # [2, 8, 34]

# HARD CHALLENGE
# CREATE A LIST result THAT HAS NUMBERS COMMON IN BOTH file1.txt and file2.txt
with open("file1.txt", "r") as f1:
  new_list = f1.readlines()                     # first we extract the contents of file1.txt
list1 = [int(n.strip()) for n in new_list]      # then we convert each item into integer, and strip the newline

with open("file2.txt", "r") as f2:
  new_list = f2.readlines()                     # next we extract the contents of file2.txt
list2 = [int(n.strip()) for n in new_list]      # then we convert each item into integer, and strip the newline

result = [n for n in list1 if n in list2]       # lastly we check for each item in list1, if present in list2
                                                # only then we consider those items

print(sorted(result))                           # sort the list as we print it, otherwise it is in the order of list1

# DICTIONARY COMPREHENSION coming up!!!

