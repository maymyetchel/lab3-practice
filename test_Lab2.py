import Lab2 

def test_find_min_max():
    result = []
    num_list = [1,2,3]
    ans = [1,3]

    result = Lab2.find_min_max(num_list)
    assert result == ans


def test_calc_average():
    result = []
    num_list = [11, 12, 13]
    ans = 12.0

    result = Lab2.calc_average(num_list)
    assert result == ans 

def test_calc_median_temperature():
    result = []
    num_list = [21, 22, 23]
    ans = 22

    result = Lab2.calc_median_temperature(num_list)
    assert result == ans 