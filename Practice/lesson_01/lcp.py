#--------------------------------#
# Taken from practice 1 slide 11 #
#--------------------------------#


def common_prefix(s1, s2):
    """
:   finds the largest prefix
:   between two strings.
:   param s1: string number 1
:   type s1: str
:   param: string number 2
:   type s2: str
    """
    length = min(len(s1), len(s2))
    
    for i in range(length):
        if s1[i] != s2[i]:
            return s1[:i]

    return s1[:length]


def LCP(strings, s, e):
    """
:   find recursivly the Longest Common Prefix
:   of list of strings.
:
:   complex: T(n) = {
:                       n = 1: 1
:                       n > 1: 2T(n/2) + O(n)
:                   }
:                 ==> O(n*log(n))
:
:   param strings: the strings to find there LCP
:   type strings: array of str
:   param s: start index to check from
:   type s: int
:   param e: end index to check until it
:   type e: int
    """
    if s == e:
        return strings[s]
        
    mid = (s + e) // 2
    
    # for left side
    llcp = LCP(strings, s, mid)
    
    # for right side
    rlcp = LCP(strings, mid + 1, e)
    
    return common_prefix(llcp, rlcp)


def main():

    words1 = ["algebra", "algorithms", "algory", "algeirs"]
    words2 = ["abcabcabcdefg", "abcabcab12324", "abcabckgkgd", "abcabcabdfgdf", "abcabcabc"]
    
    
    print("first list: " + str(words1))
    print("first LCP: " + str(LCP(words1, 0, len(words1) - 1)))
    print()
    print("second list: " + str(words2))
    print("second LCP: " + str(LCP(words2, 0, len(words1) - 1)))

if __name__ == "__main__":
    main()