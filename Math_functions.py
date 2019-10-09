responses =["Welcome to smart calculator","I am cal on your words","Sorry, this is beyond my limit "]

def extracr_numbers_from_text(text):
    l=[]
    for t in text.split(''):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)

def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
