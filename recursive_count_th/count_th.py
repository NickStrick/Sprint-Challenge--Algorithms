'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):

    # TBC
    if len(word) > 1:
        print(word)
        if word[0] + word[1] == 'th':
            count += 1
        return count_th(word[1:], count)
    return count


word = "abcthxyz"
count = count_th(word)
print(1, count)
