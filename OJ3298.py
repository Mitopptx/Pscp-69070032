"""another rabbit"""
def main():
    """clank clank labubu"""
    text = input()
    s = text.lower()
    best = 0
    for i, char in enumerate(s):
        if char == "b":
            count = 0
            for next_char in s[i + 1:]:
                if next_char == "u":
                    count += 1
                else:
                    break
            if count > best:
                best = count
    if best >= 2:
        print("Yes", best)
    elif "b" in s:
        pos = s.index("b")
        print(text[:pos + 1] + "U" * (len(text) - pos - 1))
    else:
        print(("BUU" * len(text))[:len(text)])
main()
