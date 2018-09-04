# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.

# skref 1 búa til breytur fyrir max_int og num_int
# skref 2 taka við num_int frá notanda
# skref 3 bera saman max_int og num_int, ef number er hærri breytist gildi max_int
# skref 4 endurtaka 2 og 3 þangað til sett er inn neikvæð tala
# skref 5 prenta max_int

max_int = 0
num_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int

print("The maximum is", max_int)