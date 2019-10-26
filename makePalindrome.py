def make_palindrome(input):
    if not input:
        return input
    i = 0
    j = len(input) - 1

    results = ""

    while i <= j:
        results += input[i]
        if input[i] == input[j]:
            j -= 1
        else:
            j = len(input) - 1
        i += 1
    while j >= 0:
        results += input[j]
        j -= 1
    return results

make_palindrome(None)
make_palindrome("")
make_palindrome("aba")
make_palindrome("race")
make_palindrome("rad")
make_palindrome("abc")
make_palindrome("madam")
make_palindrome("abbacbab")
make_palindrome("abbacbaab")

make_palindrome("madami")
