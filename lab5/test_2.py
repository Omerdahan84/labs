import code2


def test_fizz():
    assert code2.fizz(3) == "Fizz"
    assert code2.fizz(23) == "Fizz"
    assert code2.fizz(5) == 5
    assert code2.fizz(4) == 4


def test_buzz():
    assert code2.buzz(5) == "Buzz"
    assert code2.buzz(52) == "Buzz"
    assert code2.buzz(7) == 7
    assert code2.buzz(8) == 8


def test_fizzbuzz():
    assert code2.fizzbuzz(300) == "FizzBuzz"
    assert code2.fizzbuzz(513) == "FizzBuzz"
    assert code2.fizzbuzz(7) == 7
    assert code2.fizzbuzz(8) == 8
