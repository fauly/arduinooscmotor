from OSC import OSCClient, OSCMessage

client = OSCClient()
client.connect(('localhost', 8000))

go = OSCMessage('/lmcp/motor')
go.append('1')
back = OSCMessage('/lmcp/motor')
back.append('2')
stop = OSCMessage('/lmcp/motor',)
stop.append('0')

while True:
    choice = raw_input('Choice: ')
    if choice == 'go':
        client.send(go)
    elif choice == 'back':
        client.send(back)
    elif choice == 'stop':
       client.send(stop)
    else:
        client.send(stop)
