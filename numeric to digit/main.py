def number_to_words(num):
    ones = [
        '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen'
    ]

    tens = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]  #purpose to use two extra white spaces just to handle indexing in a proper way

    if num == 0:
        return 'zero'

    
    billions = num // 1000000000
    millions = (num // 1000000) % 1000
    thousands = (num // 1000) % 1000
    hundreds = (num // 100) % 10
    remainder = num % 100

    result = ''

    if billions > 0:
        result += number_to_words(billions) + ' billion '

    if millions > 0:
        result += number_to_words(millions) + ' million '   # number_to_words(millions) recursive fucntion

    if thousands > 0:
        result += number_to_words(thousands) + ' thousand '# number_to_words(millions) recrsive 

    if hundreds > 0:
        result += ones[hundreds] + ' hundred '

    if remainder > 0:
        if remainder < 20:
            result += ones[remainder]
        else:
            result += tens[remainder // 10] + ' ' + ones[remainder % 10]

    return result.strip() #eliminate any extra white space 

number = int(input("Enter a number: "))
words = number_to_words(number)   #function calling
print(f"{number} in words: {words}")

