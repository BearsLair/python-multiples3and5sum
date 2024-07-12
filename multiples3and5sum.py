user_input = input('Pick a number to determine the sum of the multiples of 3 and 5 below it:\n')
user_number = int(user_input)

def solution(number):
    
    multiplesof3 = []
    multiplesof5 = []

    for num in range(1, number):
        if num % 3 == 0:
            multiplesof3.append(num)
    

    for num in range(1, number):
        if num % 5 == 0:
            multiplesof5.append(num)

    multipleof3and5 = set(multiplesof3 + multiplesof5)

    sum = 0

    for unique_num in multipleof3and5:
            sum += unique_num

    return sum
    
answer = solution(user_number)
print('The sum is ' + str(answer) + ".")