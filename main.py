from commons import hcfactor
from evens import evenwords

def print_menu():
    print("--- Main Menu ---")
    print("1. Calculate Highest Common Factor")
    print("2. Print Even Length Words")
    print("3. Exit")

def get_integer_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_string_input(prompt):
    return input(prompt)

def calculate_hcf():
    num1 = get_integer_input("Enter the first number: ")
    num2 = get_integer_input("Enter the second number: ")
    hcf = hcfactor.hc_factor(num1, num2)
    print("The highest common factor of", num1, "and", num2, "is:", hcf)

def print_even_length_words():
    sentence = get_string_input("Enter a sentence: ")
    words = evenwords.get_even_length_words(sentence)
    print("Even length words found in the sentence are:")
    for word in words:
        print(word)

def main():
    while True:
        print_menu()
        option = get_integer_input("Select an option: ")

        if option == 1:
            calculate_hcf()
        elif option == 2:
            print_even_length_words()
        elif option == 3:
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

