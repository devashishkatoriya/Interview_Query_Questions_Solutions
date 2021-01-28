
"""
This question was asked by: Starbucks

1. Given a list of stock prices in ascending order by datetime, write a function that outputs the max profit by buying and selling at a specific interval.

Example:

stock_prices = [10,5,20,32,25,12]

get_max_profit(stock_prices) -> 27
"""


def get_max_profit(stock_prices):
    """Function to get max profit"""

    # Length of input array
    n = len(stock_prices)

    left_min = []       # Array to store min value on left side of ith pos
    right_max = []      # Array to store max value on right side of ith pos

    for _ in range(0, n):
        left_min.append(-1)
        right_max.append(-1)

    # Initialize base case
    left_min[0] = stock_prices[0]
    right_max[n-1] = stock_prices[n-1]

    # Compute for every position
    for i in range(1, n):
        left_min[i] = min(stock_prices[i], left_min[i-1])
        right_max[n-i-1] = max(stock_prices[n-i-1], right_max[n-i])

    # Find maximum difference of min and max values for each position
    max_diff = -1
    for i in range(0, n):
        if max_diff < right_max[i] - left_min[i]:
            max_diff = right_max[i] - left_min[i]

    # Return the maximum difference
    return max_diff


def main():
    """Main Function"""

    stock_prices = [10,5,20,32,25,12]

    print(get_max_profit(stock_prices))


if __name__ == "__main__":
    main()
