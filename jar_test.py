from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw


def test_init():
    j = Jar()
    assert j.capacity == 12
    assert j.size == 0

def test_str():
    j = Jar()
    assert str(j) == ""
    j.deposit(1)
    assert str(j) == "🍪"
    j.deposit(11)




def test_deposit(size, deposit):
    j = Jar()
    j.deposit(5)
    assert j.size ==5

    # assert j.deposit == size
    # assert j.deposit > 
    



    # j.deposit(2)

    # assert  == "🍪🍪🍪🍪

def test_withdraw():
    j = Jar()
    j.deposit(10)
    j.withdraw(5)
    assert j.size == 5
    j.withdraw(4)
    assert j.size == 1

if __name__ == "__main__":
    main()
