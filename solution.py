
#import socket module
from socket import *
import sys # In order to terminate the program

def webServer(port=13331):
    #hostIP = "127.0.0.1"
    serverSocket = socket(AF_INET, SOCK_STREAM)

    #Prepare a sever socket
    serverSocket.bind(("", port))
    #Fill in start
    serverSocket.listen(3)
    #Fill in end

    while True:
        #Establish the connection
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() #Fill in start      #Fill in end
        try:
            #print(connectionSocket)
            #print(addr)
            #print('Connection received by', addr)
            message = connectionSocket.recv(1024) #Fill in start    #Fill in end
            #print(message)
            filename = message.split()[1]
            #print(filename)
            f = open(filename[1:])
            #print(f)
            outputdata = f.read() #Fill in start     #Fill in end
            #print (outputdata)

            #Send one HTTP header line into socket
            #Fill in start
            connectionSocket.send(("\nHTTP/1.1 200 OK\r\n\r\n".encode()))

            #Fill in end

            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            #Send response message for file not found (404)
            #Fill in start
            connectionSocket.send("\nHTTP/1.1 404 Not Found\r\n\r\n".decode())
            #Fill in end

            #Close client socket
            #Fill in start
            connectionSocket.close()
            #Fill in end
        except (ConnectionResetError, BrokenPipeError):
            pass

        serverSocket.close()
        sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
    
    webServer(13331)



