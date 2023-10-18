"""
" @brief A program that counts the number of occurrences of a string S in a string L.
"""

def count_occurrences(S, L):
    """
    " @brief Counts the number of occurrences of a string S in a string L.
    " @param S The string to be searched for.
    " @param L The string to be searched in.
    " @return A tuple of three integers, where the first integer is the number of occurrences of S in L,
    "         the second integer is the number of occurrences of S in L by removing one character from L,
    "         and the third integer is the number of occurrences of S in L by adding one character to L.
    """
    def count_type_2(S, L):
        count = 0
        for i in range(len(S)):
            modified = S[:i] + S[i + 1:]
            if modified not in L:
                continue
            count += L.count(modified)
        return count

    def count_type_3(S, L):
        unique_strings = set()
        for i in range(len(S) + 1):
            for base in "AGCT":
                modified = S[:i] + base + S[i:]
                unique_strings.add(modified)
        return sum(L.count(modified) for modified in unique_strings)

    count_type_1 = L.count(S)
    count_type_2 = count_type_2(S, L)
    count_type_3 = count_type_3(S, L)

    return count_type_1, count_type_2, count_type_3

def main():
    print("Enter test cases (S L) one by one. Enter '0' to terminate the program.")
    while True:
        input_line = input("Enter a test case (S L): ")
        if input_line == "0":
            break
        S, L = input_line.split()
        type_1, type_2, type_3 = count_occurrences(S, L)
        print(type_1, type_2, type_3)

if __name__ == "__main__":
    main()
