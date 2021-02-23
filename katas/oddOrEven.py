''' Welcome a user then ask them for a number between 1 and 1000.

When the user gives you the number, you check if it's odd or even and then you print a message letting them know.

Example:

Prompt: What number are you thinking?
Input: 25
Output: That's an odd number! Have another?  '''   


print('What number are you thinking ?')
x = int(input())
if x%2 == 0 :
    print("It's even")
else:
    print("It's odd")
    