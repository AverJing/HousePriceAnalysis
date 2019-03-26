

def asc_sort(str):
    list = [i for i in str]
    list.sort()
    res = []
    temp = '\a'
    index = 0
    while len(list) != 0:
        if list[index] > temp:
            res.append(list[index])
            temp = list.pop(index)
        else:
            index += 1
        if index == len(list) and len(list)>0:
            index = 0
            temp = '\a'
    return ''.join(res)


# s = asc_sort('sdfasdghe345jdflgjlgj')
# print(s)
def word_length(str):
    index = str.rfind(' ')
    print(len(str)-index-1)

word_length("asdfas  sadfasd  asdfgadgfsadf  sdafasdf")