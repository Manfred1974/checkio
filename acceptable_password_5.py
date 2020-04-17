# Taken from mission Acceptable Password IV

# Taken from mission Acceptable Password III

# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I
import re

def is_acceptable_password(password: str) -> bool:
    if len(password) < 7:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    if len(password) < 7:
        return False
    else:
        number_flag = False
        for i in password:
            if i.isdigit():
                number_flag = True
        return number_flag


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    if len(password) < 7:
        return False
    else:
        number_flag = False
        letter_flag = False
        for i in password:
            if i.isdigit():
                number_flag = True
            if i.isalpha():
                letter_flag = True
        return number_flag and letter_flag


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    if len(password) < 7:
        return False
    elif len(password) > 9:
        return True
    else:
        number_flag = False
        letter_flag = False
        for i in password:
            if i.isdigit():
                number_flag = True
            if i.isalpha():
                letter_flag = True
        return number_flag and letter_flag


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")



def is_acceptable_password(password: str) -> bool:
    if len(password) < 7 or re.search('password', password, re.IGNORECASE):
        return False
    elif len(password) > 9:
        return True
    else:
        number_flag = False
        letter_flag = False
        for i in password:
            if i.isdigit():
                number_flag = True
            if i.isalpha():
                letter_flag = True
        return number_flag and letter_flag


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
