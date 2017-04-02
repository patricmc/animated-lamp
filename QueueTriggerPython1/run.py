import os

# read the queue message and write to stdout
inputMessage = open(os.environ['inputMessage']).read()
msgCnt = len(inputMessage)
message = "Hello world!  Processed queue message '{0}'".format(inputMessage)
print(message)
print("Message length '{0}'".format(str(msgCnt)))