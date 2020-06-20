'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count(word, sub=None):
    if sub == None or sub == "":
        return 0
        # raise Exception("Substring must not be empty or None")

    if len(sub) > len(word):
        return 0
    elif word[:len(sub)] == sub:
        return count(word[1:], sub) + 1
    else:
        return count(word[1:], sub)
        

def count_th(word):
    return count(word, "th")

print(count_th("abcthxythzth"))

print(count("abcthxhthzth", "h"))

print(count("abcthxhthzth"))
