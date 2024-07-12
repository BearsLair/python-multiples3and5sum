# (Accept input for testing purposes)
# Determine all multiples of 3 below number, push to multiplesof3 list.
#   If number less than 3, immediately return 0
#   If number is greater than 3, multiply 3 by 1, push sum to multiplesof3 list
#   Keep increasing by 1 the number that is by 3, and pushing that sum to multplesof3 list,
#   until a multiples exceeds user number.
# Determine all multiples of 5 below number, push to multiplesof5 list.
#   If number less than 5, immediately return 3
#   If number is greater than or equal to 5, multiply 5 by 1, push sum to multiplesof3 list
#   Keep increasing by 1 the number that is by 5, and pushing that sum to multplesof5 list,
#   until a multiples exceeds user number.
# Combine both into multiplesof3and5 list
# Create a set out of both lists, so it contains unique numbers
# Iterate over set, adding numbers together
# return sum
# (print sum for testing purposes)

user_input = input('Pick a number to determine the sum of the multiples of 3 and 5 below it.')
user_number = int(user_input)

def solution(number):
    multiplesof3 = []
    multiplesof5 = []

    if number < 3:
        return 0
    elif number >= 3 & number < 5:
        return 3
    elif number == 5:
        return 3
    else:
        for num in range(3, number):
            if num / 3 == 0:
                multiplesof3.append(num)

        for num in range(5, number):
            if num / 5 == 0:
                multiplesof5.append(num)

        multipleof3and5 = set(multiplesof3 + multiplesof5)

        sum = 0

        for unique_num in multipleof3and5:
            sum += unique_num

        return sum
    
answer = solution(user_number)
print(answer)