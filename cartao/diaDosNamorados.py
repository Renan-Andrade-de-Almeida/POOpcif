from cartao_mensagem import CartaoMensagem

class MensagemDiaDosNamorados(CartaoMensagem):
    def __init__(self, remetente, nome):
        super().__init__(remetente)
        self.nome = nome
        
    def __str__(self):
        return (
            f"{self.data}\
                \n\nTe amo muito {self.nome},\
                \n\n{self.remetente}"
        )