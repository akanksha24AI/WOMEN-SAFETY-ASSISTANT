# Women Safety Assistant

## Project Statement

The **Women Safety Assistant** is a Python-based terminal application designed to provide quick access to safety guidance, emergency information, SOS instructions, and trusted emergency contact details.

## Project Objective

The objective of this project is to provide a simple and easy-to-use terminal application that helps users access important safety information during normal or emergency situations.

## Main Features

1. **Safety Tips**
   - Displays practical safety precautions.
   - Provides awareness tips for different situations.
   - Encourages users to stay alert and prepared.

2. **Emergency Numbers**
   - Displays important emergency and helpline numbers.
   - Includes national emergency, police, ambulance, fire, women helpline, and cyber crime numbers.
   - Keeps important numbers available in one place.

3. **SOS Help**
   - Provides simple instructions for immediate danger.
   - Guides the user to move to a safe and crowded place.
   - Advises contacting emergency services and trusted people.
   - Encourages sharing location when it is safe.

4. **Emergency Contact**
   - Accepts the name of a trusted person.
   - Accepts the trusted person's phone number.
   - Checks that the entered details are not empty.
   - Displays the saved contact for the current session.

5. **Menu-Based Navigation**
   - Provides a clear numbered menu.
   - Allows the user to select features easily.
   - Continues running until the user chooses Exit.

6. **Input Validation**
   - Handles invalid menu choices.
   - Prevents empty emergency contact details.
   - Gives clear messages when incorrect input is entered.

## Working of the Application

The program starts with the main menu and provides five options. The user selects an option by entering its corresponding number. The selected function performs the required task and returns the user to the main menu. The application continues until the user selects the Exit option.

## Technology Used

- **Programming Language:** Python
- **Interface:** Command Line / Terminal
- **Platform:** Any system with Python installed
- **Concepts:** Functions, lists, loops, conditional statements, input handling, string methods, and menu-driven programming.

## Program Structure

The project is divided into separate functions for different tasks:

- `line()` – Displays separator lines.
- `safety_tips()` – Displays safety tips.
- `emergency_numbers()` – Displays emergency numbers.
- `sos_help()` – Displays SOS guidance.
- `emergency_contact()` – Takes and displays emergency contact details.
- `main()` – Controls the menu and overall program flow.

## Advantages

- Simple and beginner-friendly interface.
- Easy to run through the terminal.
- Provides important safety information quickly.
- Organizes multiple safety features in one application.
- Uses basic Python concepts, making the project easy to understand and maintain.

## Scope of the Project

The project can be further developed by adding features such as permanent contact storage, location sharing, a graphical interface, real-time emergency services, notifications, and integration with mobile devices.

## Limitations

- The current application works through the terminal only.
- Emergency contact details are stored only for the current session.
- The program does not automatically place calls or send messages.
- Location sharing is provided as guidance rather than an automated feature.

## Conclusion

The **Women Safety Assistant** is a practical Python terminal project that combines safety tips, emergency numbers, SOS guidance, and emergency contact handling in a single application. It demonstrates the use of fundamental Python programming concepts to create a useful, structured, and user-friendly safety application.
