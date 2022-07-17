def isAnagram(a, b):

    if len(a) != len(b):
        return False

    # sort the first string
    first = sorted(a)
    # sort the second string
    second = sorted(b)

    if first == second:
        return True
    else:
        return False


# driver code
if __name__ == '__main__':
    ans = isAnagram("listen", "silent")
    print(ans)
