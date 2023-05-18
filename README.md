# Converter um texto digitado para letra cursiva.

Este script converte texto digitado em uma imagem de escrita à mão usando a biblioteca PySimpleGUI e PyWhatKit. O usuário pode escolher a cor do texto e onde salvar a imagem.

## Requisitos

- Python 3
- PySimpleGUI
- PyWhatKit

Instale as dependências usando:

```
pip install PySimpleGUI pywhatkit
```

## Uso

1. Execute o script.
2. Escolha a cor do texto na opção "Cor do texto".
3. Clique em "Salvar" para selecionar o diretório onde a imagem será salva.
4. Digite o texto quedeseja converter na caixa de texto.
5. Clique em "Converter" para gerar a imagem de escrita à mão.

## Personalizar a cor do texto

Se você deseja usar uma cor personalizada:

1. Escolha a opção "Personalizado" no menu "Cor do texto".
2. Clique em "Converter".
3. Insira a cor desejada no formato RGB, separado por vírgulas (por exemplo, 255, 255, 255) na janela "Personalizar cor".
4. Clique em "OK".

Se a conversão for bem-sucedida, você verá uma janela de pop-up informando que a imagem foi salva com sucesso no diretório selecionado.

## Limitações

- A conversão pode ser lenta para textos longos.
- A qualidade da escrita à mão pode não ser perfeita.
