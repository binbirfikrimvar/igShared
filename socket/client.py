import socket

# sunucunun IP adresi ve port numarası
IP = '127.0.0.1'
PORT = 12345

# IPv4 tabanlı, TCP protokolü üzerinden bir soket nesnesi oluşturuluyor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucu ile bağlantı kurma
client_socket.connect((IP, PORT))

# Sunucuya veri gönderme
message = "Merhaba, sunucu"
client_socket.send(message.encode())

# Sunucudan gelen cevabı alma
data = client_socket.recv(1024).decode()
print(f"Alınan veri: {data}")

# Bağlantıyı kapatma
client_socket.close()
