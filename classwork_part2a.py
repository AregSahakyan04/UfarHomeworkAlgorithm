def lcs_length(str1, str2):
    if not str1 or not str2:
        return 0
        
    if str1[-1] == str2[-1]:
        return 1 + lcs_length(str1[:-1], str2[:-1])
    else:
        return max(lcs_length(str1, str2[:-1]), lcs_length(str1[:-1], str2))

def find_lcs_length(wordlist):
    if not wordlist:
        return 0
    current_lcs_length = len(wordlist[0])
    for i in wordlist[1:]:
        current_lcs_length = lcs_length(wordlist[0], i)
        if current_lcs_length == 0:
            return 0
    return current_lcs_length

wordlist = []
print("Enter finish if you want to end.")
while True:
    word = input("Enter a string: ")
    if word == "finish":
        break
    wordlist.append(word)

length = find_lcs_length(wordlist)
print(f"The length of LCS is {length}")
