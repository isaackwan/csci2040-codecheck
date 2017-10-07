from browser import document, alert
		
def echo(ev):
	alert(document["zone"].value)

document['mybutton'].bind('click',echo)

with open('workfile') as f:
	f.write('This is a test\n')

with open('workfile') as f:
	print(f.read())