def containPrefix(query):
    set=['dog','deer','deal']
    return list(filter(lambda t:t.startswith(query),set))

print(containPrefix('de'))