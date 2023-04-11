import socket

# sunucunun dinleyeceği IP adresi ve port numarası
IP = '0.0.0.0'
PORT = 12345

# IPv4 tabanlı, TCP protokolü üzerinden bir soket nesnesi oluşturuluyor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soket bağlantısının yapılacağı IP ve port numarası belirleniyor
server_socket.bind((IP, PORT))

# Soket bağlantısını dinleme moduna alınması
server_socket.listen(1)

print('Sunucu dinlemede...')

# Bağlantıyı kabul etme
client_socket, client_address = server_socket.accept()
print(f"{client_address} bağlandı.")

# İstemciden veri alma
data = client_socket.recv(1024).decode()
print(f"Alınan veri: {data}")

# İstemciye cevap gönderme
message = "Merhaba, istemci"
client_socket.send(message.encode())

# Bağlantıyı kapatma
client_socket.close()
server_socket.close()
