import sys
from browser import document

# setup stderr
def write(data):
    document['result'].innerText += str(data)

sys.stderr.write = write

def handleUpload(event):
	lab.upload(event.detail.name, event.detail.body)

def handleFinishedUpload(event):
	lab.finishedUpload()
	document['drop_zone'].innerText = 'Retry? Please refresh this page before proceeding'

document['drop_zone'].bind('upload', handleUpload)
document['drop_zone'].bind('finishedUpload', handleFinishedUpload)
document['drop_zone'].innerText = 'Ready, please drop your Python3 (.py) files here'