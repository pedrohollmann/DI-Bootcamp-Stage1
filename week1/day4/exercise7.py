#Exercise 7: Temperature advice

import random

def get_random_temp():
    return random.randint(-10, 40)

def main():
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")

    if temperature < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temperature <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 17 <= temperature <= 23:
        print("Nice weather.")
    elif 24 <= temperature <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()