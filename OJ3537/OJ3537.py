"""IMposter"""
def main():
    """:3"""
    member = {}
    dead = {}
    while True:
        word = input()
        if word == "Start":
            break
        word = word.strip("{}\"")
        color,status = word.split("\" : \"")
        member[color] = status
    while True:
        word = input()
        if word == "End":
            break
        if word in member:
            dead[word] = member[word]
            member.pop(word)
    count = 0
    for _,i in member.items():
        if i == "Impostor":
            count+=1
    print(count,"Impostor Remains")
    print("***Alive***")
    for k, v in sorted(member.items(), key=lambda item: item[0]):
        print(k,":",v)
    print("***Dead***")
    for k, v in sorted(dead.items(), key=lambda item: item[0]):
        print(k,":",v)
main()
