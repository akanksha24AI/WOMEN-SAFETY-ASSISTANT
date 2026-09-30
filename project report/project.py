# ============================================================
#                 WOMEN SAFETY ASSISTANT
# ============================================================


def line():
    print("=" * 55)


def safety_tips():
    line()
    print("                    SAFETY TIPS")
    line()

    tips = [
        "Keep your mobile phone charged.",
        "Save emergency numbers in your phone.",
        "Avoid isolated and poorly lit places.",
        "Inform a trusted person about your plans.",
        "Stay aware of your surroundings.",
        "Use safe and familiar routes.",
        "Trust your instincts in unsafe situations.",
        "Keep some emergency money with you.",
        "Learn basic self-defence techniques.",
        "Ask for help when you feel unsafe."
    ]

    for number in range(len(tips)):
        print(str(number + 1) + ". " + tips[number])

    line()


def emergency_numbers():
    line()
    print("                 EMERGENCY NUMBERS")
    line()

    print("112  - National Emergency Number")
    print("1091 - Women Helpline")
    print("181  - Women Helpline")
    print("108  - Ambulance")
    print("100  - Police")
    print("101  - Fire Emergency")
    print("1930 - Cyber Crime Helpline")

    print()
    print("Save these numbers for emergency situations.")
    line()


def sos_help():
    line()
    print("                      SOS HELP")
    line()

    print("If you are in immediate danger:")
    print()
    print("1. Stay calm.")
    print("2. Move to a safe and crowded place.")
    print("3. Call 112 for immediate emergency help.")
    print("4. Contact a trusted person.")
    print("5. Share your location when safe to do so.")
    print("6. Ask nearby people for assistance.")
    print("7. Avoid confronting a dangerous person.")

    line()


def emergency_contact():
    line()
    print("                 EMERGENCY CONTACT")
    line()

    name = input("Enter trusted person's name: ").strip()
    number = input("Enter phone number: ").strip()

    if name == "" or number == "":
        print()
        print("Contact details cannot be empty.")
    else:
        print()
        print("Emergency Contact")
        print("-----------------")
        print("Name   : " + name)
        print("Number : " + number)
        print("Contact details saved for this session.")

    line()


def main():
    while True:
        print()
        line()
        print("              WOMEN SAFETY ASSISTANT")
        line()
        print("1. Safety Tips")
        print("2. Emergency Numbers")
        print("3. SOS Help")
        print("4. Emergency Contact")
        print("5. Exit")
        line()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            safety_tips()

        elif choice == "2":
            emergency_numbers()

        elif choice == "3":
            sos_help()

        elif choice == "4":
            emergency_contact()

        elif choice == "5":
            print()
            line()
            print("Thank you for using Women Safety Assistant.")
            print("Stay alert. Stay safe!")
            line()
            break

        else:
            print()
            print("Invalid choice.")
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()