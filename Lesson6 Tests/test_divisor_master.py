import divisor_master

def test_if_simple():
    assert divisor_master.if_simple(7) == True

def test_divisors():
    assert divisor_master.divisors(10) == [1,2,5,10]

def test_biggest():
    assert divisor_master.biggest(70) > 2

def test_simple_m():
    assert len(divisor_master.simple_m(91)) > 1

def test_biggest_d():
    assert divisor_master.biggest_d(93) % 2 != 0