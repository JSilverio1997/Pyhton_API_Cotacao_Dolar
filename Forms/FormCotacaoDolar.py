from tkinter import *
from tkcalendar import *
from Action.Cotacao_Dolar import CotacaoDolar


class FormCotacaoDolar:

    def __init__(self, master):
        self.master = master
        self.master.title("Cotação do Dólar")
        self.componentes(master)

    @staticmethod
    def componentes(janela):

        def obter_data_selecionada():
            cotacao = CotacaoDolar()
            data_formatada = cotacao.formatar_data(date_entrada.get_date())
            cotacao.obter_cotacao_dolar(data_formatada)

        Label(janela, text="Selecione a Data", font="Arial, 14", background="light green").pack(padx=10, pady=10)
        date_entrada = DateEntry(janela, width=25, background="dark green", foreground="black",
                                 borderwith=3, date_pattern="dd/mm/y", locale="pt")
        date_entrada.pack(padx=10, pady=10)

        btn_consulta = Button(janela)
        btn_consulta['text'] = "Consultar Valor do Dólar"
        btn_consulta['font'] = "Arial,14,bold"
        btn_consulta['width'] = 20
        btn_consulta['command'] = obter_data_selecionada
        btn_consulta.pack(padx=40, pady=10)


def instanciar():
    form_cotacao_dolar = Tk()
    FormCotacaoDolar(form_cotacao_dolar)
    form_cotacao_dolar.iconbitmap(r'Imagens/dollar.ico')
    form_cotacao_dolar.configure(relief="ridge", bg="light green", border="4")
    form_cotacao_dolar.geometry("520x450+500+200")
    form_cotacao_dolar.resizable(0, 0)
    form_cotacao_dolar.maxsize(450, 200)
    form_cotacao_dolar.mainloop()


instanciar()

