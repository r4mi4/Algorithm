"""
    buy sell stock
        [7,1,5,3,6,4] => 5
        [9,7,6,5,4,3,1] => 0
"""

def max_profit(prices):
    cur_max, max_so_far = 0, 0
    for i in range(1,len(prices)):
        print(cur_max,max_so_far)
        cur_max = max(0, cur_max + prices[i] - prices[i-1])
        max_so_far = max(cur_max, max_so_far)
    return max_so_far

print(max_profit([7,1,5,3,6,4]))