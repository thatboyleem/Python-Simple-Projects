def send_messages(messages, sent_messages):
    while messages:
        current_msg = messages.pop()
        print(f"sending: {current_msg}")
        sent_messages.append(current_msg)

def show_messages(text_messages):
    """this function prints messages in a text"""
    for message in text_messages:
        print(message)

messages = ['hello', 'can you get it for me', 'please refrain from dodging too much', 'nice hair cut']
sent_messages =[]

for message in messages:
    print(message)
send_messages(messages[:], sent_messages)
show_messages(sent_messages)