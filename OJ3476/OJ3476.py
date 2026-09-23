"""FUBUKI?"""
def main():
    """:3"""
    n = int(input())
    cat = {}
    fox = {}
    for _ in range(n):
        data = input()
        name, tag = data.split(":", 1)
        name = name.strip().strip("{}\" ")
        tag = tag.strip().strip("{}\" ")
        if tag.upper().startswith("CAT"):
            tag = "Cat" + tag[3:]
            cat[tag] = name
        elif tag.upper().startswith("FOX"):
            tag = "Fox" + tag[3:]
            fox[tag] = name
    if "Cat01" not in cat and not ("Garfield" in cat.values() or "Garfield" in fox.values()):
        cat["Cat01"] = "Garfield"
    if "Fox01" not in fox and not ("Fubuki" in cat.values() or "Fubuki" in fox.values()):
        fox["Fox01"] = "Fubuki"
    cat = dict(sorted(cat.items()))
    fox = dict(sorted(fox.items()))
    print("Cat :", len(cat))
    print("Fox :", len(fox))
    for tag, name in cat.items():
        print(name, ":", tag)
    for tag, name in fox.items():
        print(name, ":", tag)
main()
