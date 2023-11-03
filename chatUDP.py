import socket
import threading
# Endereço IP e porta para o servidor
host = '10.113.60.218' # Endereço IP do servidor
porta = 12345 # Porta do servidor
# Cria um objeto socket UDP
socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Liga o socket ao endereço e porta especificados
socket_server.bind((host, porta))
print(f&quot;Servidor UDP aguardando mensagens em {host}:{porta}&quot;)
# Função para receber mensagens
def receber_mensagens():
while True:
try:
# Recebe os dados e o endereço do remetente
dados, endereco = socket_server.recvfrom(1024) # Tamanho do buffer é
1024 bytes
mensagem = dados.decode(&#39;utf-8&#39;)
print(f&quot;Recebido de {endereco[0]}:{endereco[1]}: {mensagem}&quot;)
except UnicodeDecodeError:
print(f&quot;Recebido de {endereco[0]}:{endereco[1]}: Erro de decodificação
(não UTF-8)&quot;)
# Inicializa uma thread para receber mensagens
thread_recebimento = threading.Thread(target=receber_mensagens)
thread_recebimento.daemon = True
thread_recebimento.start()
# Função para enviar mensagens
def enviar_mensagens():
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
destino_ip = input(&quot;Digite o endereço IP de destino: &quot;)
mensagem = input(&quot;Digite a mensagem a ser enviada: &quot;)
if mensagem == &quot;/sair&quot;:
print(&quot;Encerrando o programa...&quot;)
print(&quot;Fechando portas de escuta:&quot;)
thread_recebimento.join()
break
else:
cliente_socket.sendto(mensagem.encode(&#39;utf-8&#39;), (destino_ip, porta))
# Inicializa uma thread para enviar mensagens
thread_envio = threading.Thread(target=enviar_mensagens)
thread_envio.start()
# Aguarda as threads finalizarem

thread_envio.join()
print(&quot;Threads encerradas.&quot;)
# Feche o socket (isso nunca será executado no loop acima)
socket_server.close()
print(&quot;Socket encerrado. Bye Bye&quot;)
