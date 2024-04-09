""" Problem Statement:- Given a list of string. you have to find longest common prefix and return
the prefix.
Note :
If there is no common prefix, return an empty.
Example 1: I
Input: strs = ["tcsdigital","tcsninja", "tcsprime"]
Output: "tcs"
Example 2:
Input: strs = ["flower", "flow","flight"]
Output: "f1" """
def longest_common_prefix(strs):
    if not strs:
        return ""

    min_len = min(len(s) for s in strs)
    prefix = ""

    for i in range(min_len):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break

    return prefix

# Take input from the user
input_strings = input("Enter the strings separated by spaces: ")
strs = input_strings.split()

# Call the function with the input list
result = longest_common_prefix(strs)
print("Longest Common Prefix:", result)
