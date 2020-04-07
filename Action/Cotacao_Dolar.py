import json
import requests
import tkinter.messagebox
from datetime import datetime


class CotacaoDolar:
    @staticmethod
    def formatar_data(data):
        date_atual = data
        data_formatada = datetime.strftime(date_atual, '%m-%d-%Y')
        return data_formatada

    @staticmethod
    def obter_cotacao_dolar(data):
        requisicao = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia"
                                  + "(dataCotacao=@dataCotacao)"
                                  + f"?@dataCotacao=%27{data}%27&$top=100&$format=json&$select=cotacaoCompra,"
                                  + "cotacaoVenda,dataHoraCotacao")
        try:
            if requisicao.status_code == 200:
                json_file = json.loads(requisicao.text)
                dados_cotacao_dolar = json_file
                dict_cotacao_dolar = dict(dados_cotacao_dolar['value'][0])

                dolar_compra = dict_cotacao_dolar['cotacaoCompra']
                dolar_venda = dict_cotacao_dolar['cotacaoVenda']
                data_hora_cotacao = dict_cotacao_dolar['dataHoraCotacao']

                tkinter.messagebox.showinfo("Dólar", f" Valor do Dólar de Compra: {dolar_compra}\n Valor do Dólar de "
                                                     f"Venda: {dolar_venda}"
                                                     f"\n Data/ Hora da Cotação: {data_hora_cotacao[:19]}")
            else:
                tkinter.messagebox.showwarning("Atenção", "Erro ao tentar consumir a API. ", requisicao.status_code)
        except():
            tkinter.messagebox.showerror("Erro", "Erro ao tentar consumir a API de Cotação")
        except IndexError:
            tkinter.messagebox.showwarning("Atenção", "Atenção: provavelmente você tentou obter o valor de uma cotação"
                                                      " com a Data de um Feriado Nacional ou de um final de "
                                           "semana.")


"""cotacao_atual = CotacaoDolar()
cotacao_atual.obter_cotacao_dolar('04-03-2020')  # formato de data MM-DD-RRRR
print(cotacao_atual.formatar_data(datetime.today()))"""
