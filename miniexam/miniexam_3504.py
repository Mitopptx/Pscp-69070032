"""Ham?"""
def main():
    """:3"""
    word1 = input()
    word2 = input()
    count = 0
    for i,_ in enumerate(word1):
        if word1[i] != word2[i]:
            count += 1
    print(count)
main()
