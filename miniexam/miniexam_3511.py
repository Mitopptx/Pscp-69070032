"""weather"""
def main():
    """:3"""
    cloud = input()
    speed = input()
    if cloud == "Gloomy" and speed in ("High","Medium"):
        print("100%")
    elif cloud == "Cloudy":
        print("50%")
    elif cloud == "Clear" and speed == "Low":
        print("0%")
    else:
        print("Not sure.")
main()
