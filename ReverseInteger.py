def reverseNumber(number):
    reverse=0

    while number>0:
        last_digit=number%10
        reverse=reverse*10+last_digit
        number=number//10
    return reverse


print(reverseNumber(12399))