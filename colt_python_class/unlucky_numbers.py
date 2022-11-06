# For the numbers 1 - 20 (inclusive), print if the number is even or odd. If the number is 4 or 13, print "UNLUCKY!"

for num in range(1, 21):
    if num == 4 or num == 13:
        print(f'{num} is UNLUCKY!')
    elif num % 2:
        print(f'{num} is odd!')
    else:
        print(f' {num} is even!')