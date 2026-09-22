def main():
    print("Welcome to Health Literacy Checker!")
    health_message = input("Paste your health message here: ")
    print("Your health message is:", health_message)
    if "utilize" in health_message.lower():
            print ("Jargon found: 'utilize' - try using 'use' instead.")
    critical = input("Is your health message critical? (yes/no): ")
    length = len(health_message.split())

    if critical.lower() == "yes":
        if length <= 8:
            print("Your health message is good.")
        elif length <= 15:
            print("Your health message is acceptable.")
        else:
            print("Your health message is too complex.")
    elif critical.lower() == "no":
        if length <= 10:
            print("Your health message is good.")
        elif length <= 20:
            print("Your health message is acceptable.")
        else:
            print("Your health message is too complex.")
    print ("Your health message has", length, "words.")
main()