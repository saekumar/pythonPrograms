# Method to print maximum possible number
def max_number(s):
    # N stores the length of String
    n = len(s)

    # string ans to store the answer
    ans = ""

    # freq list to store frequency of elements in window
    freq = [0] * 10

    # Left End of the window
    left = 0

    # Two pointer algorithm to find window of same
    # parity consecutive elements
    while left < n:
        # Right end of window
        right = left

        # Incrementing right End to find the window of
        # same parity elements
        while right < n - 1 and int(s[right]) % 2 == int(s[right + 1]) % 2:
            # Adding elements into freq vector
            freq[int(s[right])] += 1
            right += 1

        # Adding the last element of the window
        freq[int(s[right])] += 1

        # Adding elements into list
        for i in range(9, -1, -1):
            while freq[i] > 0:
                ans += str(i)
                freq[i] -= 1

        # Left End of next window
        left = right + 1

    # Printing the answer
    print(ans)


# Driver Function
if __name__ == "__main__":
    # Input String
    input_str = "7596801"

    # Function call
    max_number(input_str)
