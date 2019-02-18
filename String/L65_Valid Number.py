Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.strip()
        length = len(s)
        index = 0
        # Deal with symbol
        if index < length and (s[index] == '+' or s[index] == '-'):
            index += 1
        is_normal = False
        is_exp = True
        # Deal with digits in the front
        while index < length and s[index].isdigit():
            is_normal = True
            index += 1
        # Deal with dot ant digits behind it
        if index < length and s[index] == '.':
            index += 1
            while index < length and s[index].isdigit():
                is_normal = True
                index += 1
        # Deal with 'e' and number behind it
        if is_normal and index < length and (s[index] == 'e' or s[index] == 'E'):
            index += 1
            is_exp = False
            if index < length and (s[index] == '+' or s[index] == '-'):
                index += 1
            while index < length and s[index].isdigit():
                index += 1
                is_exp = True
        # Return true only deal with all the characters and the part in front of and behind 'e' are all ok
        return is_normal and is_exp and index == length
        
        
