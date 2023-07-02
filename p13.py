#if we press on number 5
#http://www.pythonchallenge.com/pc/phonebook.php
# text: faultCode 105 faultString XML error 5: empty document
# after googling this failure related to phyton module xmlrpc
import xmlrpc.client
def pythonchallenge13(url):
    call = xmlrpc.client.ServerProxy(url)
    call.system.listMethods() #['phone', 'system.listMethods', 'system.methodHelp', 'system.methodSignature', 'system.multicall', 'system.getCapabilities']
    #phone looks like not a method from xmlrpc documents
    call.system.methodHelp('phone') #Returns the phone of a person
    call.system.methodSignature('phone') #[['string', 'string']]
    call.phone('phone') #He is not the evil
    #name before was bert
    return call.phone('Bert') #555-ITALY



result = pythonchallenge13("http://www.pythonchallenge.com/pc/phonebook.php")
print(result) #http://www.pythonchallenge.com/pc/return/italy.html