import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class Calculadora(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.resultado = toga.TextInput(readonly=True, style=Pack(flex=1))
        main_box.add(self.resultado)

        botoes = [
            ['C', '(', ')', '<'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+']
        ]

        for linha in botoes:
            h_box = toga.Box(style=Pack(direction=ROW, padding=5))
            for botao_texto in linha:
                botao = toga.Button(botao_texto, on_press=self.pressionar_botao, style=Pack(flex=1))
                h_box.add(botao)
            main_box.add(h_box)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def pressionar_botao(self, widget):
        texto_atual = self.resultado.value

        if widget.text == '=':
            try:
                resultado = str(eval(texto_atual))
                self.resultado.value = resultado
            except Exception as e:
                self.resultado.value = "Erro"
        elif widget.text == 'C':
            self.resultado.value = ''
        elif widget.text == '<':
            self.resultado.value = texto_atual[:-1]
        else:
            self.resultado.value += widget.text

def main():
    return Calculadora()
