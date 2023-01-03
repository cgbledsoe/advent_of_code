import math

with open('2022/puzzle_inputs/25.txt') as file:
    strInput = file.read()

test_strInput = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""

# split list
# convert each base 5 number to decimal
## decode each position and multiply by the corresponding value
# sum the numbers 
# then convert back to base 5


def decode(b5_str):
    """
    Convert string representation of base 5 to decimal integer
    """
    decoder = {'2':2,'1':1,'0':0,'-':-1,'=':-2}
    decimal = 0
    for i, component in enumerate(b5_str[::-1]):
        decimal += ((5**i)*decoder[component])
    return decimal

def encode(decimal):
    # need to factor the number
    # encoder = 
    result = decimal
    b5_str = ""
    while result != 0:
        quotient = result / 5
        remainder = round(5*(quotient - math.floor(quotient)),1)
        # now I need to account for having -2 to 2 not 0-5
        b5_str += str(int(remainder))
        result = int(quotient)

    # so a 3 in one position gets turned into
    b5_str_aug = [x for x in b5_str]
    for i in range(len(b5_str_aug)):
        value = b5_str_aug[i]
        if int(value) == 3:
            b5_str_aug[i] = "="
            try:
                b5_str_aug[i+1] = str(int(b5_str_aug[i+1]) + 1)
            except:
                b5_str_aug.append("1")
        elif int(value) == 4:
            b5_str_aug[i] = "-"
            try:
                b5_str_aug[i+1] = str(int(b5_str_aug[i+1]) + 1)
            except:
                b5_str_aug.append("1")
        else:
            continue
    return ''.join(b5_str_aug)[::-1]

def main(input):
    b5_list = [x for x in input.split('\n') if x != '']
    decimals = []
    for b5_str in b5_list:
        decimals.append(decode(b5_str))
    
    sum_decimals = sum(decimals)
    return encode(sum_decimals)



if __name__ == '__main__':
    print(main(strInput))
