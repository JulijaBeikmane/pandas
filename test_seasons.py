from seasons import number_to_words
from seasons import calculate_age_in_minutes
from seasons import get_user_input
from datetime import date

def main():
     test_n_to_w()
    # calc()
    # us_inp()

# def calc():
    
#     try:
#         assert calculate_age_in_minutes(23) == 33120
#     except AssertionError:
#         print("Šeit 33120")

def test_n_to_w():

    assert number_to_words(1440) == "One thousand, four hundred forty"
   
# def calc():
#     pass

# def us_inp():
#     pass

if __name__ == "__main__":
    main()
