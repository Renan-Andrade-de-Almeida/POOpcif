class pessoa:
    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura

    def Envelhece(self, anos):
        self.idade += anos

    def Engordar(self, gordura):
        self.peso += gordura

    def Emagrecer(self, gordura):
        self.peso -= gordura
    
    def Crescer(self, tamanho):
        if self.idade < 21:
            self.altura += tamanho

p1 = pessoa("kenya", 15, 42, 150)


