"""
This question was asked by: Postmates

Given an array of integer N, return an array of integers so
that the subsequent integers in an array get filtered out if
they are less than a larger integer at a further index in the array.


Example 1:

n = [20,17,19,18,12,16,10,4,6,3]

output = [20,19,18,16,10,6,3]

Example 2:

n = [25,30,21,22,14,10,5,26]

output = [30,26]
"""


def dec_subsq_val(arr):
    """Function to calculate decreasing subsequent values"""

    n = len(arr)
    output = []

    for i in range(0, n):
        curr = arr[i]
        correct = True

        for j in range(i, n):
            if (curr < arr[j]):
                correct = False
                break

        if correct:
            output.append(curr)

    return output


def main():
    """Main Function"""

    n = [25,30,21,22,14,10,5,26]

    output = dec_subsq_val(n)

    print(output)



if __name__ == "__main__":
    main()
