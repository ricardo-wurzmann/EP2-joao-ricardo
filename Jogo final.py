#normalizando base países
import Funcoes
import Base_países
dados=Funcoes.normaliza(Base_países.DADOS)
print(dados)

print(" ============================")
print("|                            |")
print("| Bem-vindo ao Insper Países |")
print("|                            |")
print(" ==== Design de Software ==== ")
print(" Comandos:")
print("    dica       - entra no mercado de dicas")
print("    desisto    - desiste da rodada")
print("    inventario - exibe sua posição")
print("Um país foi escolhido, tente adivinhar!")
print("Você tem tentativa(s)")
print("Qual seu palpite?")