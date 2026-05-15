

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    prev = [0] * (m + 1)
    cur = [0] * (m + 1)

    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                cur[ind2] = 1 + prev[ind2 - 1]
            else:
                cur[ind2] = max(prev[ind2], cur[ind2 - 1])

        prev = cur[:]

    return prev[m]


# if __name__ == "__main__":
    # s1 = "AGGTAB"
    # s2 = "GXTXAYB"
    # lcs_value = lcs(s1,s2)
    # print(lcs_value)
    # print("len of s1 = " + str(len(s1)))
    # print("len of s2 = " + str(len(s2)))
    # print("score is " + str(lcs_value) + "/" + str(max(len(s1), len(s2))) + " = " + str(lcs_value/(max(len(s1), len(s2)))))
