"""
" @brief This function calculates the occurrences of S in L in three different forms:
"
"   1) Exact occurrences of S in L
"   2) Occurrences of S in L when one character from S is removed
"   3) Occurrences of S in L when one character is added to S from the base set "AGCT"
"
"   @param S: a string for which occurrences in L will be counted.
"   @param L: a string in which occurrences of S and its modified forms will be searched.
"""
def count_occurrences(S, L):
    
    """
    " @brief This nested function counts the occurrences of S in L after removing one character from S.
    "
    " @param S: a string to modify.
    "
    " @param L: a string in which modified forms of S will be searched.
    """
    def count_type_2(S, L):
        modified_strings = set()
        for i in range(len(S)):
            modified = S[:i] + S[i+1:]
            modified_strings.add(modified)
    
        total = 0
        for mod in modified_strings:
            for i in range(len(L) - len(mod) + 1):
                if L[i:i+len(mod)] == mod:
                    total += 1
        return total
    """
    "    @brief This nested function counts the occurrences of S in L after adding one character from the base set "AGCT" to S.
    "    @param S: a string to modify.
    "    @param L: a string in which modified forms of S will be searched.
    """
    def count_type_3(S, L):
        modified_strings = set()
        for i in range(len(S) + 1):
            for base in "AGCT":
                modified = S[:i] + base + S[i:]
                modified_strings.add(modified)

        total = 0
        for mod in modified_strings:
            idx = 0
            while idx < len(L) - len(mod) + 1:
                if L[idx:idx+len(mod)] == mod:
                    total += 1
                idx += 1
        return total

    count_type_1 = sum(1 for i in range(len(L) - len(S) + 1) if L[i:i+len(S)] == S)
    count_type_2_result = count_type_2(S, L)
    count_type_3_result = count_type_3(S, L)

    return count_type_1, count_type_2_result, count_type_3_result

"@brief This is the main function to execute the program. It takes input test cases from the user, processes them, and displays the results."
def main():
    print("Enter test cases (S L) one by one. Enter '0' to finish.")
    while True:
        input_line = input("Enter a test case (S L): ").strip()
        if input_line == "0":
            break
        S, L = input_line.split()
        type_1, type_2, type_3 = count_occurrences(S, L)
        print(type_1, type_2, type_3)

if __name__ == "__main__":
    main()
