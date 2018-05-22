animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
"""
def howMany(aDict):
    i = 0
    result = []
    values = aDict.values()
    print (values)
    for w in values:
        result.append(w)
    for word in result:
        i += len(word)
    return i

print (howMany (animals))
"""
def largest(aDict):
    larg_item = ['',0]
    if len(aDict) ==0:
        return None 
    for (k,v) in aDict.items():
        if len(v)>larg_item[1]:
            larg_item[0]=k
            larg_item[1]=len(v)

    return larg_item[0]
print (largest(animals))