"""demon slayer"""
def main():
    """:3"""
    demon = {"Spider Demon": 1 , "Swamp Demon": 2,"Arrow Demon": 1 , "Hand Demon": 2,
            "Drum Demon": 3 ,"Mugen Train": 2,"Upper Moon": 3}
    index = list(demon.keys())
    kill = 0
    count =0
    again=0
    while True:
        key = int(input())
        if key == demon[index[0]]:
            print(index[0])
            print("kill")
            demon.pop(index[0])
            index.pop(0)
            kill += 1
            again = 0
        else:
            if again == 1:
                print(index[0])
                print("back")
                index.append(index.pop(0))
                again = 0
            else:
                again =1
        count += 1
        if kill == 5:
            print(count)
            break
main()
