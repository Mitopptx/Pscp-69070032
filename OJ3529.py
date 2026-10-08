"""Caesar cipher"""

def main():
    word = input()
    common = (
        "what", "when", "why", "which", "this",
        "there", "where", "the", "is", "am",
        "are", "you", "we", "they", "he", "she", "it")
    for shift in range(26):
        check = ""
        for ch in word.lower():
            if 'a' <= ch <= 'z':
                check += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
            else:
                check += ch
        words = check.split()
        if any(word in common for word in words):
            break
    result = ""
    for ch in word:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += ch
    print(result)
main()
