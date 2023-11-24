# Guest on chat
# ---CLIENT---
import socket
import threading

# Initiating objects for used throughout program.
# Fines and inputs your IP address
DEST_IP = socket.gethostbyname(socket.gethostname())
# The designated port to connect to
DEST_PORT = 48295
# Encodes bits to strings
ENCODER = "utf-8"
# The Maximum size size of information to be sent
BUF_SIZE = 1024

# Receiving messages function.
def receive_messages(client_socket):
    while True:
        # Message received and decoded as a string
        message = client_socket.recv(BUF_SIZE).decode(ENCODER)
        # The word "quit" is looked for
        if message.lower() == "quit":
            # if the word quit is found, Goodbye is sent, and the chat ends.
            print("\n Chat is Ending...bye bye!")
            break
        else:
            # If quit is not found a new message is Print it out
            print(f"\nServer: {message}")

# send a message function
def send_messages(client_socket):
    while True:
        # Input becomes message
        message = input("Client: ")
        # Message is encoded and sent to client
        client_socket.send(message.encode(ENCODER))
        # If statement looks for the word "quit" and ends chat if found.
        if message.lower() == "quit":
            print("\n Chat is Ending...bye bye!")
            break

# Client socket which connects to the server.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connects to the server
    client_socket.connect((DEST_IP, DEST_PORT))

    # Threads are created and connected to both sending and receiving messages to
    # allow them to be conducted simultaneously rather than a back-and-forth
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    # starts the threads
    receive_thread.start()
    send_thread.start()
    # Weights for the thread to finish before starting another one.
    receive_thread.join()
    send_thread.join()

finally:
    # closes the socket ending the chat closes the socket ending the chat.
    client_socket.close()
