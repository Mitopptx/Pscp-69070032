"""kang"""
def main():
    """:3"""
    word = input().strip("[]")
    me = list(map(int,word.split(", ")))
    word = input().strip("[]")
    enemy = list(map(int,word.split(", ")))
    me = sorted(me)
    enemy = sorted(enemy)
    newme = me.copy()
    for i in me:
        cop = enemy.copy()
        while True:
            if min(cop)<i:
                enemy.remove(min(cop))
                break
            if min(cop)==max(cop):
                cop.clear()
                break
            cop.remove(min(cop))
        if not cop:
            enemy.remove(max(enemy))
            newme.remove(i)
    print(sum(newme))
main()
