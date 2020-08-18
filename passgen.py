"""
[✓] Armazenar a senha site/software, usuário/email.
[✓] Armazenar Site/Software.
[✓] Armazenar Usuário/Email.
[✓] Configurar o tamanho da senha.
[✓] Tocar música de fundo quando o programa for iniciado.

"""
import random
import PySimpleGUI as sg
from playsound import playsound


class PassGen:
    def __init__(self):
        sg.theme('DarkBlack')
        # Escolhendo a música que será tocada
        playsound('Bit_Coin.mp3', block=False)

        # Criando layout
        layout = [
            [sg.Text('Gerador de senhas fortes...')],
            [sg.Text('Site/Software:', size=(10, 1)), sg.Input(key='site', size=(20, 1))],
            [sg.Text('Usuário/Email:', size=(10, 1)), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres:'),
             sg.Combo(values=list(range(31)), key='chars_tot', default_value=1, size=(3, 1))],
            [sg.Output(size=(31, 5))],
            [sg.Button('Gerar Senha', size=(29, 1))]
        ]

        # Criando a janela
        self.janela = sg.Window('Ebony Sys', layout, resizable=True)

    def Iniciar(self):
        # Criando eventos
        while True:
            evento, valores = self.janela.read()

            # Fechar a janela
            if evento == sg.WINDOW_CLOSED:
                break

            # Clicar no botão
            if evento == 'Gerar Senha':
                nova_senha = self.Gerar_Senha(valores)
                print(nova_senha)
                self.Salvar(nova_senha, valores)

    def Gerar_Senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*&%$#@!'
        chars = random.choices(char_list, k=int(valores['chars_tot']))
        join_pass = ''.join(chars)
        return join_pass

    def Salvar(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"{valores['site']}, usuario: {valores['usuario']}, "
                          f"nova senha: {nova_senha}\n")
        print('Arquivo salvo com sucesso!')


gen = PassGen()
gen.Iniciar()
