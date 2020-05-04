def isometric_strings(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True

    if not str1 or not str2:
        return False

    if len(str1) != len(str2):
        return False

    str1_to_str2 = [0 for i in range(256)]
    str2_to_str1 = [0 for i in range(256)]

    for char_str1, char_str2 in zip(str1, str2):
        if str1_to_str2[ord(char_str1)] != 0:
            if str1_to_str2[ord(char_str1)] != ord(char_str2):
                return False
        else:
            if str2_to_str1[ord(char_str2)] != 0 and str2_to_str1[ord(char_str2)] != ord(char_str1):
                return False
            else:
                str1_to_str2[ord(char_str1)] = ord(char_str2)
                str2_to_str1[ord(char_str2)] = ord(char_str1)
    return True
