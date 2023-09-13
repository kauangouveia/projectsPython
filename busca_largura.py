from  classe_no import no

class busca:
    def executar(self, no_inicial:no):
        no_inicial.set_cor('azul')
        fila:list = [no_inicial]
        while len(fila)>0:
            no_atual:no = fila.pop(0)
            for no_filho in no_atual.get_adjacente():
                if no_filho.get_cor() == 'branco':
                    no_filho.set_cor('azul')
                    no_filho.set_custo(no_atual.get_custo() + 1)
                    no_filho.set_anterior(no_atual)
                    fila.append(no_filho)
            no_inicial.set_cor('vermelho')
    
    def percorrrer_caminho(self,alvo:no):
        caminho =  []
        while alvo:
            caminho.insert(0, alvo.get_nome())
            alvo = alvo.get_anterior()
        return caminho