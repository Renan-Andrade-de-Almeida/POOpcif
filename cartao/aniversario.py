from cartao_mensagem import CartaoMensagem

class MensagemAniversario(CartaoMensagem):
    def __init__(self, remetente, nome):
        super().__init__(remetente)
        self.nome = nome

    def __str__(self):
        return (
            f"{self.data}\
                \n\nFeliz aniveersario, {self.nome},\
                \n\nGrandes abraços!\
                \n\n{self.remetente}"
        )