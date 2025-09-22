

def get_wordcount(string):
    wordlist = string.split()
    return len(wordlist)

def get_charcount(string):
    string = string.lower()
    dict = {}

    for c in string:
        if c in dict:
            dict[c] += 1
        else:
            dict.update({c:1})
    

    return dict

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    list = []
    for x in dict:
        list.append({"char":x,"num":dict[x]})

    list.sort(reverse=True, key=sort_on)
    return list