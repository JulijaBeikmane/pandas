from datetime import date
import sys
import inflect

def main():
    dzims_datums = get_user_input()
    vecums_minutes = calculate_age_in_minutes(dzims_datums)
    vardos = number_to_words(vecums_minutes)
    print(vardos + " minutes")
def get_user_input():
    try:
        ievade = input("Ievadi dzimšanas datus formā GGGG-MM-DD: ")
        gads, menesis, diena = map(int, ievade.split("-"))
        dzims_datums = date(gads, menesis, diena)
        # gads, menesis, diena = ievade.split("-")
        # dzims_datums = date(int(gads), int(menesis), int(diena))
        return dzims_datums
    except ValueError:
        print("Invalid date")
        sys.exit(1)
    
def calculate_age_in_minutes(dzims_datums):
    sodien = date.today()
    vecums = sodien - dzims_datums
    vecums_minutes = vecums.days * 24 * 60
    return vecums_minutes

def number_to_words(skaitlis):
    parveide = inflect.engine()
    vardi = parveide.number_to_words(skaitlis).replace(" and ", " ")
    return vardi.capitalize()


if __name__ == "__main__":
    main()
