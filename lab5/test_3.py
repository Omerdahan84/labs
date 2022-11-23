import code3


def test_fizz():
    assert code3.fizz(6) == "Fizz"
    assert code3.fizz(3) == 3
    assert code3.fizz(13) == "Fizz"


def test_buzz():
    assert code3.buzz(52) == "Buzz"
    assert code3.buzz(5) == 5
    assert code3.buzz(20) == "Buzz"


def test_fizzbuzz():
    assert code3.fizzbuzz(13) == "FizzBuzz"
    assert code3.fizzbuzz(3) == 3
    assert code3.fizzbuzz(25) == 25
    assert code3.fizzbuzz(7) == 7
