import socket

# esli file zapuwen samostoyatelno s konsoli ,my rabotaem opredelennym obrazom vypolnyaetsya main()
def run():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('localhost', 5000))
	server_socket.listen()

	while True:
		client_socket, addr = server_socket.accept()
		server_socket.sets
		request = client_socket.recv(1024)
		print(request.decode('utf-8'))
		print()
		print(addr)

		response = generate_response(request.decode('utf-8'))

		client_socket.sendall('hello world'.encode())
		client_socket.close()

if __name__ == '__main__': 
	run()