"""weather"""
def main():
    weather = input()
    speed = input()
    if weather == "Gloomy" and (speed == "High" or speed == "Medium"):
        print("100%")
    elif weather == "Cloudy":
        print("50%")
    elif weather == "Clear" and speed == "Low":
        print("0%")
    else:
        print("Not sure.")
main()
