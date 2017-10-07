from browser import document, alert, window

def echo(ev):
	alert(document["zone"].value)

document['mybutton'].bind('click',echo)