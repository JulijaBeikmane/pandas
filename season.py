from datetime import date
import sys

def main():
    dzims_datums = get_user_input()
    vecums_minutes = calculate_age_in_minutes(dzims_datums)
    print(vecums_minutes)
def get_user_input():
    try:
        ievade = input("Ievadi dzimšanas datus formā GGGG-MM-DD ")
        gads, menesis, diena = map(int, ievade.split("-"))
        dzims_datums = date(gads, menesis, diena)
        return dzims_datums
    except ValueError:
        print("Invalid date")
        sys.exit(1)
    
def calculate_age_in_minutes(dzims_datums):
    sodien = date.today()
    vecums = sodien - dzims_datums
    vecums_minutes = vecums.days * 24 * 60
    return vecums_minutes

def number_to_words():
    pass

if __name__ == "__main__":
    main()
