from random import randint

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'


class DataJSONView(BaseLineChartView):

    def get_labels(self):
        labels = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
            'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
        ]
        return labels

    def get_providers(self):
        datasets = [
            'Programação para Leigos',
            'Algoritimos e Lógica de Programação',
            'Programação em C',
            'Programação em Java',
            'Programação em Python',
            'Banco de Dados'
        ]
        return datasets

    def get_data(self):
        dados = []
        for  l in self.get_providers():
            for c in self.get_labels():
                dado = [
                    randint(1, 200), # jan
                    randint(1, 200), # fev
                    randint(1, 200), # mar
                    randint(1, 200), # abr
                    randint(1, 200), # mai
                    randint(1, 200), # jun
                    randint(1, 200), # jul
                    randint(1, 200), # ago
                    randint(1, 200), # set
                    randint(1, 200), # out
                    randint(1, 200), # nov
                    randint(1, 200), # dez
                ]
            dados.append(dado)
        return dados
