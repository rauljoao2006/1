class Gato:
    def __init__(self, cor, peso, nome, idade, raca):
        self.cor = cor
        self.peso = peso
        self.nome = nome
        self.idade = idade
        self.raca = raca

    def andar(self):
        print(f"{self.nome}, um gato {self.raca}, está a andar pela casa.")

    def correr(self):
        print(f"{self.nome}, o {self.raca}, está a correr atrás do rato.")

meu_gato = Gato("preto", 7, "Lua", 5, "Bombaim")

print(f"O gato chama-se {meu_gato.nome}, tem {meu_gato.idade} anos, é da raça {meu_gato.raca}, cor {meu_gato.cor} e pesa {meu_gato.peso} kg.")

meu_gato.andar()
meu_gato.correr()


                         
