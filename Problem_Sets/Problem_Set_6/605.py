def isVowel(letter: str) -> bool:
    return letter.lower() in ["a", "e", "i", "o", "u"]

def transform_to_boolean(word: str) -> list:
    result = []
    for ind in range(len(word)):
        letter = word[ind]
        result.append(letter) if isVowel(letter) else result.append(False)
    return result
word = input()
final_list = transform_to_boolean(word)
print("Yes" if any(final_list) else "No")