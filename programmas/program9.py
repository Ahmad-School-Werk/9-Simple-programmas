def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "oneven"

def main():
    try:
        input_number = int(input("Voer een getal in: "))
        result = even_or_odd(input_number)
        print(f"Het ingevoerde getal is {result}.")
    except ValueError:
        print("Ongeldige invoer. Voer alstublieft een geldig getal in.")

if __name__ == "__main__":
    main()
