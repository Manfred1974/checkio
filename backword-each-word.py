

def backward_string_by_word(text: str) -> str:
    words = text.split(' ')
    reversed_words = [w[::-1] for w in words]
    new_sentence = ' '.join(reversed_words)
    return new_sentence
