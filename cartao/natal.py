from cartao_mensagem import CartaoMensagem

class MensagemNatal(CartaoMensagem):
    def __init__(self, remetente, nome):
        super().__init__(remetente)
        self.nome = nome
        
    def __str__(self):
        return (
            f"{self.data}\
                \n\nFeliz natal! {self.nome},\
                \n\nAbraços!\
                \n\n{self.remetente}"
        )