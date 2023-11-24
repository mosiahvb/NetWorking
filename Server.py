# Creating a chat
# ---SERVER---
import socket
import threading

# Initiating objects for used throughout program.
# Fines and inputs your IP address
HOST_IP = socket.gethostbyname(socket.gethostname())
# Your designated port of Connection
HOST_PORT = 48295
# Encodes bits to strings
ENCODER = "utf-8"
# The Maximum size size of information to be sent.
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
            print(f"\nClient: {message}")

# send a message function
def send_messages(client_socket):
    while True:
        # Input becomes message
        message = input("Server: ")
        # Message is encoded and sent to client 
        client_socket.send(message.encode(ENCODER))
        # If statement looks for the word "quit" and ends chat if found.
        if message.lower() == "quit":
            print("\n Chat is Ending...bye bye!")
            break

# A socket is created to allow the messaging to go back-and-forth.
# The type of socket is identified
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# The socket, then uses the IP and port numbers
server_socket.bind((HOST_IP, HOST_PORT))
# The socket begins to listen for incoming data packets.
server_socket.listen()

try:
    # opening up socket to allow for acceptance and sending of information.
    print("Server is running...\n")
    client_socket, client_address = server_socket.accept()
    client_socket.send("You are connected...\n".encode())

    # Threads are created and connected to both sending and receiving messages to
    # allow them to be conducted simultaneously rather than a back-and-forth
    receiving_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    sending_thread = threading.Thread(target=send_messages, args=(client_socket,))
    # starts the threads
    receiving_thread.start()
    sending_thread.start()
    # Weights for the thread to finish before starting another one.
    receiving_thread.join()
    sending_thread.join()

finally:
    # closes the socket ending the chat closes the socket ending the chat
    server_socket.close()
