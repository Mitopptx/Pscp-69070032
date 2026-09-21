"""FUBUKI?"""
def main():
    """:3"""
    n = int(input())
    cat = {}
    fox = {}
    for i in range(n):
        keyword = input()
        name,tag = keyword.split(":")
        name = name.strip("{\"").rstrip().strip("\"")
        tag = tag.strip("\"}").lstrip().strip("\"")
        if tag[:3]=="Cat":
            cat[tag] = name
        elif tag[:3]=="Fox":
            fox[tag] = name
    if "Cat01" not in cat and not ("Garfield" in cat.values() or "Garfield" in fox.values()):
        cat["Cat01"] = "Garfield"
    if "Fox01" not in fox and not ("Fubuki" in cat.values() or "Fubuki" in fox.values()):
        fox["Fox01"] = "Fubuki"
    cat = dict(sorted(cat.items()))
    count=0
    for _ in cat:
        count +=1
    print("Cat :",count)
    count =0
    for _ in fox:
        count +=1
    print("Fox :",count)
    for i in cat:
        print(cat[i],":",i)
    fox = dict(sorted(fox.items()))
    for i in fox:
        print(fox[i],":",i)
main()
