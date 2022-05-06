def mid(text):
    if len(text)%2 == 0:
        return ""
    else:
        for j,rec in enumerate(text):
            if len(text)//2 == j:
                return rec
print( mid("Pyn"))
