import price_info

def test_total_cost_shopping(): 
    result = []
    ans = 46.75
    result = price_info.total_cost_shopping()
    assert (result == ans)

def test_cost_of_fruit(): 
    result = []
    fruit_name = "apple"
    quantity = 10 
    ans = 12.0 
    result = price_info.cost_of_fruits(fruit_name, quantity)
    assert (result == ans)