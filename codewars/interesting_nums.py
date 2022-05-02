def is_interesting(number, awesome_phrases):
    str_number = str(number)
    
    #print(number, awesome_phrases)
    def interesting(str_number, awesome_phrases):
        
        res = [digits_followed_by_zeros(str_number),
        same_number_digits(str_number),
        in_awesome_phrase(number, awesome_phrases),
        sequentially_decrementing(str_number),
        sequentially_incrementing_digits(str_number),
        palindrome(str_number)
        ]
        print(res)
        return True if any(res) else False

    def interesting_in_2_miles(number, awesome_phrases):
        in_2 =number+2
        in_1 = number+1
        res = [digits_followed_by_zeros(in_1),
        same_number_digits(in_1),
        in_awesome_phrase(in_1, awesome_phrases),
        sequentially_decrementing(in_1),
        sequentially_incrementing_digits(in_1),
        palindrome(in_1),
        digits_followed_by_zeros(in_2),
        same_number_digits(in_2),
        in_awesome_phrase(in_2, awesome_phrases),
        sequentially_decrementing(in_2),
        sequentially_incrementing_digits(in_2),
        palindrome(in_2),
        ]
        return True if any(res) else False

    def digits_followed_by_zeros(str_number):
        
        rest = str(str_number)[1:]
        sub_str = '0'*(len(rest))
        return True if sub_str == rest else False

    def same_number_digits(str_number):
        first =str(str_number)[0]
        if len(str(str_number)) == str(str_number).count(first):
            return True
        return False

    def sequentially_incrementing_digits(str_number):
        #For incrementing sequences, 
        #0 should come after 9, and not before 1, as in 7890.
        increment = '1234567890'
        if str(str_number) in increment:
            return True
        return False

    def sequentially_decrementing(str_number):
        # For decrementing sequences, 
        #0 should come after 1, and not before 9, as in 3210.
        decrement = '9876543210'
        if str(str_number) in decrement:
            return True
        return False

    def palindrome(str_number):

        return True if str(str_number) == str(str_number)[::-1] else False

    def in_awesome_phrase(number, awesome_phrases):

        return True if number in awesome_phrases else False

        
    if number < 98:
        return 0
    elif interesting(number, awesome_phrases) and number >=100:
        return 2
    elif interesting_in_2_miles(number, awesome_phrases):
        return 1
    return 0
number= 98 

awesome_phrases = []

print(is_interesting(number, awesome_phrases))