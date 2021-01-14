'''

Q1. Given an example paragraph string and an integer N,
write a function that returns the top N frequent words
in the posting and the frequencies for each word.

Q2. What's the function run-time?


>>Example:

n = 3
posting = """
Herbal sauna uses the healing properties of herbs in combination with distilled water.
The water evaporates and distributes the effect of the herbs throughout the room.
A visit to the herbal sauna can cause real miracles, especially for colds.
"""

output = [
    ('the', 6),
    ('herbal', 2),
    ('sauna', 2),
]

'''


def get_top_n(posting, n):
    """Function to get top n most frequent words"""

    # Clean up input string
    posting = posting.replace(".", "")
    posting = posting.replace(",", "")
    posting = posting.replace("!", "")
    posting = posting.replace("@", "")
    posting = posting.replace("$", "")
    posting = posting.replace("#", "")

    # Split the input string
    posting = posting.split(' ')

    # Dictionary to store result
    output = dict()

    # Iterate over each word
    for word in posting:

        word = word.lower()

        if word in output:
            output[word] = output[word] + 1
        else:
            output[word] = 1

    # Sort the Dictionary
    import operator

    output = sorted(output.items(), key=operator.itemgetter(1), reverse=True)

    return output


def main():
    """Main Function"""

    n = 3
    posting = "Herbal sauna uses the healing properties of herbs in combination with distilled water. The water evaporates and distributes the effect of the herbs throughout the room. A visit to the herbal sauna can cause real miracles, especially for colds."

    output = get_top_n(posting, n)

    print(output)


if __name__ == "__main__":
    main()
