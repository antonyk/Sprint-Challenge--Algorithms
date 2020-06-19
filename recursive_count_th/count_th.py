'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    target = "th"
    t_arr = list("th")
    target_size = len(target)
    w_arr = list(word)
    word_size = len(w_arr)

    if word_size < target_size:
        return 0

    elif word[:2] == target:
        return count_th(word[1:]) + 1

    else:
        return count_th(word[1:])


    
    
print(count_th("abcthxyz"))
