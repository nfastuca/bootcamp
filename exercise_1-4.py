def substrings(seq_A, seq_B):
"""Finds largest common substrings in strings 'seq_A' and 'seq_B'"""
#ensure seq_A is smaller if not initially
    if seq_B < seq_A:
        (seq_B, seq_A) = (seq_A, seq_B)
    length = len(seq_A)
    while length > 0:
        wiggle = len(seq_A)-length
        #range(x) creates list of integers from 0-(x-1)
        for a in range(wiggle + 1):
            #search for slice of seq_A form a to (a+length) in seq_B
            if seq_A[a: (a+length)] in seq_B:
                return seq_A[a: (a+length)]
        length -= 1
    return ""
