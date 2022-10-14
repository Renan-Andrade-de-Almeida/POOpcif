class pessoa:
    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso 
        self.altura = altura

    def Envelhece(self, anos):
        for i in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.Crescer(0.5)
            

    def Engordar(self, gordura):
        self.peso += gordura

    def Emagrecer(self, gordura):
        self.peso -= gordura
    
    def Crescer(self, tamanho):
        self.altura += tamanho

p1 = pessoa("kenya", 15, 42, 150)

p1.Engordar(10)
p1.Emagrecer(20)

p1.Envelhece(7)


print(p1.idade, p1.altura)