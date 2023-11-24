# Overview

This project was conducted to learn about networking and gain a basic understanding of networking through application of Python into creating a virtual chat in a terminal.

 The following is a chat room that can be opened in a terminal that connects a client to a server, allowing the client and server to communicate back-and-forth sending information primarily as a chat room. Users can go back-and-forth, sending information or send information simultaneously to each other.

I was able to create this program through trial and error, and watching a variety of tutorials on networking, as well as reviewing a variety of Python networking websites. After getting a basic understanding, I attempted to add threading, which would allow my messaging to be simultaneous rather than a game of back-and-forth one piece of information than another.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Chat room demo](https://youtu.be/COW6UAOjrCw)

# Network Communication

 The architecture I chose to use was client/server, this was done to allow for a variety of added clients later on down the road and seemed to match my wants the best. 

The chat is using TCP (Transmission Control Protocol) within the socket being socket being used. This server is bound to PORT-48295 and the Client is connected to PORT-48295.

Between the client and server information is encrypted from a string to bites then when Received by the client or server, is then unencrypted, and returned to being a string to be read.

# Development Environment

I used a variety of tutorial videos to gain understanding of server client systems. Going back-and-forth between Python, networking websites and tutorials to get a visual on how the programming should look and be conducted to run smoothly.

I used VS code, and the Python programming language to create the chat room. I imported the socket and threading modules to Connect and allow my chat to simultaneously run functions. 

# Useful Websites

* [python.org](https://docs.python.org/3.6/library/socketserver.html)
* [realpython](https://realpython.com/python-sockets/)
* [YouTube](https://www.youtube.com/watch?v=vsLBErLWBhA)
* [YouTube](https://www.youtube.com/watch?v=7gek0eCnbHs)

# Future Work

* I want to add more personalized version, allowing the clients to give them self a name and four messages to be saved and revisited as chats continue overtime.
* I had some difficulty understanding and applying encryption to secure messages back-and-forth and would like to dive deeper into it and add a secure end-to-end encryption to the chat.
* I want to increase the visuals of this chat by connecting it, or adding it to an application to give it an aesthetic and more usable look and platform.