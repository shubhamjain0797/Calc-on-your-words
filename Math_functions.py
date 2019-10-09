responses =["Welcome to smart calculator","I am cal on your words","Sorry, this is beyond my limit "]

def extracr_numbers_from_text(text):
    l=[]
    for t in text.split(''):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)

