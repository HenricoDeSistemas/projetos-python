#Exemplo de Uso da variavel sentinela

while True:
    comando = input("Digite um comando-para parar digite 'sair'")

if comando == "sair":
    break
print(F"Executando:{comando}")