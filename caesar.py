import string

def alphabet_position(letter):
    if string.ascii_letters.index(letter) <= 25:
        return string.ascii_letters.index(letter)
    else:
        return (string.ascii_letters.index(letter) - 26)

def rotate_character(char, rot):
    if str.islower(char):
        if alphabet_position(char) + rot <= 25:
            return string.ascii_lowercase[alphabet_position(char) + rot]
        else:
            return string.ascii_lowercase[(alphabet_position(char) + rot)%26]
    elif str.isupper(char):
        if alphabet_position(char) + rot <= 25:
            return string.ascii_uppercase[alphabet_position(char) + rot]
        else:
            return string.ascii_uppercase[(alphabet_position(char) + rot)%26]
    else:
        return char


def encrypt(text, rot):
    novusText = ''
    
    for i in range(len(text)):
        novusText += rotate_character(text[i], rot)

    return novusText


## User input
#usrTXT = input("Type a message: ")
#usrROT = int(input("Rotate by: "))
#
## Encrypt user input using caesar cipher, then print to STDOUT
#print(encrypt(usrTXT, usrROT))

# User input
## ROT as cmd-line arg
## Validation
#
###import sys
###
###def user_input_is_valid(cl_args):
###    if (len(cl_args)  > 1) and str.isdigit(cl_args[1]):
###        return True
###    else:
###        return False 
###    
###def main():
###    if user_input_is_valid(sys.argv):
###        usrROT = int(sys.argv[1])
###        usrTXT = input("Type a message: ")
###
###        # Encrypt user input using caesar cipher, then print
###        # to STDOUT
###        print(encrypt(usrTXT, usrROT))
###    else:
###        print("usage: python3 caesar.py n")
###
###if __name__ == '__main__':
###    main()
###
