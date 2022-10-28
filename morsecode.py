MORSE_CODE_DICT = { ' ':'\\', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}


def Txt_to_Morse():
    txt = input('Enter Text to Convert to Morse: ')
    code = [MORSE_CODE_DICT[i.upper()] + ' ' for i in txt if i.upper() in MORSE_CODE_DICT.keys()]
    morse=''.join(code)
    return morse


def Morse_to_Txt():
    txt = input('Enter Morse to Convert to Text: ')
    code = [f for i in txt.split() for f,v in MORSE_CODE_DICT.items() if i==v ]
    newtxt = ''.join(code)
    return newtxt

n = 'Y'
while  n == 'Y':
    print('''\n1 - Convert Text to Morse \n2 - Convert Morse to Text\n3 - Quit\n ''')
    try:
        selection = int(input('Select Your Choice: '))
        if selection == 1:
            print(Txt_to_Morse())

        elif selection == 2:
            print('use " \ " for spaces'.upper())
            print(Morse_to_Txt())

        elif selection == 3:
            print('... . . \ -.-- --- ..- \ -. . -..- - \ - .. -- . \ -.-. .... ..- - .. -.-- . ')
            break

        else:
            print('Wrong Selection, enter again')
    except:
        print('Wrong Selection, enter again')
    n=input("If you want to continue press Y\n").upper()
    if n == 'Y':
        continue
    else:
        exit()
