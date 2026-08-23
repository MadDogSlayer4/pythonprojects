def strip_comments(strng, markers):
    pass
    fstring = ""
    read = True
    for rd in strng:
        if rd in markers: 
            read = False
            if fstring != '': 
                if fstring[-1] == ' ': fstring = fstring.rstrip()
        elif '\n' in rd or '\\' in rd:
            if fstring != '':
                if fstring[-1] != '\n': fstring = fstring.rstrip()
            read = True
        if read: fstring += rd
    return fstring
