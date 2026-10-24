"""kang"""
def main():
    """:3"""
    n = int(input())
    word = []
    for _ in range(n):
        w = input()
        if word:
            for j in range(len(word)):
                if len(word[j])>len(w):
                    word.insert(j,w)
                    break
        if w not in word:
            word.append(w)
    for i in word:
        print(i)
main()
