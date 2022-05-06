def capital_indexes(text):
    return [count for count, rec in enumerate(text)  if rec.isupper()]


print (capital_indexes("HeLlO"))
