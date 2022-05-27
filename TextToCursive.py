from tkinter.font import BOLD
import PySimpleGUI as sg
import pywhatkit as kit


def janela_escrever():
    sg.theme('DarkPurple1')

    layout = [
        [sg.Text('⚙️ Configurações', justification='center',
                 font=('Arial', 14, BOLD))],
        [sg.Text('Cor do texto'), sg.OptionMenu(['Preto', 'Azul', 'Vermelho', 'Rosa', 'Cinza', 'Verde',
                                                 'Roxo', 'Dourado', 'Laranja', 'Personalizado'], default_value='Preto', key='-COR-FONTE-')],
        [sg.FolderBrowse('Salvar', key='-SALVAR-IMAGEM-', button_color=('White', 'Gray')),
         sg.Input(default_text='⬅️ Escolha onde salvar', size=(29, 0))],
        [sg.HSep()],
        [sg.Text('Digite o texto que deseja converter'),
         sg.Button('Converter', key='-CONVERTER-')],
        [sg.Multiline(size=(35, 20), key='-TEXTO-')],
    ]
    return sg.Window("Botega - Escrita",  font=("Arial", 12), layout=layout, finalize=True)


escrever_janela = janela_escrever()

while True:
    window, event, values = sg.read_all_windows()
    if window == escrever_janela and event == sg.WIN_CLOSED:
        break

    if values['-COR-FONTE-'] == 'Preto':
        cor = [0, 0, 0]

    if values['-COR-FONTE-'] == 'Azul':
        cor = [41, 35, 219]

    if values['-COR-FONTE-'] == 'Vermelho':
        cor = [235, 38, 38]

    if values['-COR-FONTE-'] == 'Rosa':
        cor = [235, 14, 231]

    if values['-COR-FONTE-'] == 'Cinza':
        cor = [96, 96, 96]

    if values['-COR-FONTE-'] == 'Verde':
        cor = [3, 82, 22]

    if values['-COR-FONTE-'] == 'Roxo':
        cor = [108, 5, 153]

    if values['-COR-FONTE-'] == 'Dourado':
        cor = [218, 165, 32]

    if values['-COR-FONTE-'] == 'Laranja':
        cor = [247, 133, 2]

    if event == '-CONVERTER-':
        if values['-SALVAR-IMAGEM-'] == '':
            sg.Popup(
                'Opa, parece que esqueceu de escolher onde a imagem será salva.', title='Atenção')
        elif values['-COR-FONTE-'] == 'Personalizado':
            cor = sg.popup_get_text(
                'Coloque a cor em formato RGB, separado por vírgula.\nExemplo: 255, 255, 255', title='Personalizar cor')
            if cor == '':
                sg.Popup('Opa, parece que esqueceu de escolher a cor.',
                         title='Atenção')
            else:
                kit.text_to_handwriting(values['-TEXTO-'], values['-SALVAR-IMAGEM-']+'\imagem.png', [
                                        int(cor.split(',')[0]), int(cor.split(',')[1]), int(cor.split(',')[2])])
                sg.Popup('Imagem salva com sucesso em ' +
                         values['-SALVAR-IMAGEM-'], title='Sucesso')
        else:
            kit.text_to_handwriting(
                values['-TEXTO-'], values['-SALVAR-IMAGEM-']+'\imagem.png', cor)
            sg.Popup('Imagem salva com sucesso em '+'"' +
                     values['-SALVAR-IMAGEM-']+'"', title='Sucesso')
