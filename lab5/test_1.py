import code1


def test_fizz():
    assert code1.fizz(3) == "Fizz"
    assert code1.fizz(6) == "Fizz"
    assert code1.fizz(5) == 5
    assert code1.fizz(4) == 4


def test_buzz():
    assert code1.buzz(5) == "Buzz"
    assert code1.buzz(10) == "Buzz"
    assert code1.buzz(7) == 7
    assert code1.buzz(8) == 8


def test_fizzbuzz():
    assert code1.fizzbuzz(15) == "FizzBuzz"
    assert code1.fizzbuzz(30) == "FizzBuzz"
    assert code1.fizzbuzz(7) == 7
    assert code1.fizzbuzz(8) == 8
