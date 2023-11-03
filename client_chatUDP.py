import socket
import threading

# Endereço IP e porta do servidor
host = '192.168.10.116'  # Endereço IP do servidor
porta = 12345  # Porta do servidor

# Tamanho máximo de dados a serem recebidos de uma vez
tamanho_maximo = 1024

# Lista de contatos simulada (nome, endereço IP)
contatos = []

# Função para receber mensagens do servidor
def receber_mensagens(socket_cliente):
    while True:
        try:
            dados, _ = socket_cliente.recvfrom(tamanho_maximo)
            mensagem = dados.decode('utf-8')
            print(f"Recebido do servidor: {mensagem}")
        except UnicodeDecodeError:
            print("Erro de decodificação (não UTF-8)")

# Função para enviar mensagens para o servidor
def enviar_mensagens(socket_cliente):
    while True:
        mensagem = input("Digite a mensagem: ")
        if mensagem == ".contatos":
            # Comando para solicitar a lista de contatos
            socket_cliente.sendto(mensagem.encode('utf-8'), (host, porta))
        elif mensagem.startswith("."):
            # Comando para enviar mensagem para um contato específico
            socket_cliente.sendto(mensagem.encode('utf-8'), (host, porta))
        else:
            # Enviar mensagem normal
            socket_cliente.sendto(mensagem.encode('utf-8'), (host, porta))

# Função para exibir a lista de contatos
def exibir_lista_contatos():
    print("Lista de Contatos:")
    for nome, endereco in contatos:
        print(f"{nome}: {endereco}")

# Configuração do cliente UDP
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_cliente.bind((host, porta))  # Associa o cliente a uma porta

# Inicializa threads para receber e enviar mensagens
thread_recebimento = threading.Thread(target=receber_mensagens, args=(socket_cliente,))
thread_envio = threading.Thread(target=enviar_mensagens, args=(socket_cliente,))

# Laço principal do cliente
while True:
    print("\nComandos disponíveis:")
    print(".contatos - Exibir lista de contatos")
    print(".<nome_do_contato>_<mensagem> - Enviar mensagem para um contato")
    print(".parar - Encerrar o cliente")
    
    comando = input("Digite um comando ou mensagem: ")
    
    if comando == ".contatos":
        exibir_lista_contatos()
    elif comando == ".parar":
        print("Encerrando o cliente...")
        socket_cliente.close()
        break
    elif comando.startswith("."):
        # Tratar o comando .<nome_do_contato>_<mensagem>
        # Divida o comando para extrair o nome do contato e a mensagem
        partes = comando.split("_", 1)
        if len(partes) == 2:
            nome_contato = partes[0][1:]  # Remove o ponto no início
            mensagem = partes[1]
            # Aqui você pode enviar a mensagem para o servidor, informando o nome do contato e a mensagem
            print(f"Enviando mensagem para {nome_contato}: {mensagem}")
            # Substitua a linha acima com a lógica de envio real
    else:
        # Tratar mensagens normais
        # Aqui você pode enviar a mensagem para o servidor como antes
        # Substitua a linha abaixo com a lógica de envio real
        print(f"Enviando mensagem para o servidor: {comando}")
        


