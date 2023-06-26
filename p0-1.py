#task 0
def pythonchallenge0(x,y):
    return x**y
result = pythonchallenge0(2,38)
print(result) #www.pythonchallenge.com/pc/def/274877906944.html

#task 1
# hints: k==m , o==q, e==g
#test(1)
print(ord('k')-ord('m'),ord('o')-ord('q'),ord('e')-ord('g'))
#result 2 is the difference
import string
def pythonchallenge1(text):
    a = string.ascii_lowercase
    mytable = str.maketrans(a,a[2:]+a[:2])
    text = text.translate(mytable)
    return text

result = pythonchallenge1('''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. map''')
print(result) #http://www.pythonchallenge.com/pc/def/ocr.html



