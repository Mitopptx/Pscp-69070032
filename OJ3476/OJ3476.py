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
            tag = int(tag[3:])
            cat[int(tag)] = name
        elif tag.upper().startswith("FOX"):
            tag = int(tag[3:])
            fox[int(tag)] = name
    if 1 not in cat and not ("Garfield" in cat.values() or "Garfield" in fox.values()):
        cat[1] = "Garfield"
    if 1 not in fox and not ("Fubuki" in cat.values() or "Fubuki" in fox.values()):
        fox[1] = "Fubuki"
    cat = dict(sorted(cat.items(), key =lambda item: int(item[0])))
    fox = dict(sorted(fox.items(), key =lambda item: int(item[0])))
    print("Cat :", len(cat))
    print("Fox :", len(fox))
    for tag, name in cat.items():
        if tag<10:
            print(name," : Cat0", tag,sep="")
        else:
            print(name, " : Cat", tag,sep="")
    for tag, name in fox.items():
        if tag<10:
            print(name, " : Fox0", tag,sep="")
        else:
            print(name, " : Fox", tag,sep="")
main()
