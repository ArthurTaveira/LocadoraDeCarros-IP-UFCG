
import funcoes_locadora as locadora

def menu():
    print("Bem-vindo à Locadora de Veículos!")
    print("Digite:")
    print("1 - Para locar um veículo")
    print("2 - Para se cadastrar como cliente")
    print("3 - Para devolver um veículo")
    print("4 - Para ver o veículo mais locado")
    print("5 - Para ver o total de dinheiro ganho")
    print("6 - Para ver a lista de clientes")
    print("7 - Para ver a lista total de carros")
    print("8 - Para ver a lista de carros locados")
    print("9 - Para adicionar um novo carro")
    print("0 - Para sair")

def main():
    while True:
        menu()
        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            locar_veiculo()
        elif escolha == "2":
            cadastrar_cliente()
        elif escolha == "3":
            devolver_veiculo()
        elif escolha == "4":
            veiculo_mais_locado()
        elif escolha == "5":
            dinheiro_ganho()
        elif escolha == "6":
            listar_clientes()
        elif escolha == "7":
            listar_carros()
        elif escolha == "8":
            listar_carros_locados()
        elif escolha == "9":
            adicionar_novo_carro()
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida!")
            
#Função para Locar Veículos
def locar_veiculo():
    carros = locadora.ler_carros_disponiveis()
    print("Carros disponíveis para locação:")
    for carro in carros:
        print(f"{carro['carro']} - Placa: {carro['placa']} - Número do Veículo: {carro['numero_veiculo']} - Preço de Locação: R$ {carro['preco_locacao']:.2f}")
    placa = input("Digite a placa do carro que deseja locar: ")
    cpf = input("Digite seu CPF: ")
    if locadora.verificar_cliente(cpf):
        if locadora.verificar_locacao(placa, cpf):
            print("Você já tem um veículo locado.")
        else:
            carro_locado = next((carro for carro in carros if carro['placa'] == placa), None)
            if carro_locado:
                locadora.adicionar_carro_locado(carro_locado['placa'], cpf)
                dinheiro_ganho = locadora.ler_dinheiro_ganho()
                locadora.atualizar_dinheiro_ganho(dinheiro_ganho + carro_locado['preco_locacao'])
                print(f"Carro {carro_locado['carro']} locado com sucesso! Preço da locação: R$ {carro_locado['preco_locacao']:.2f}")
            else:
                print("Placa inválida ou carro não disponível.")
    else:
        print("CPF não registrado na locadora.")

# Função para cadastrar um novo cliente
def cadastrar_cliente():
    print("Por favor, insira seus dados:")
    nome = input("Nome: ")
    email = input("Email: ")
    cpf = input("CPF: ")

    locadora.cadastrar_cliente(nome, email, cpf)

#funcao para devolver o veiculo
def devolver_veiculo():
    placa = input("Digite seu CPF: ")
    cpf = input("Digite a placa do carro a ser devolvido: ")

    if locadora.verificar_locacao(placa, cpf):
        locadora.remover_carro_locado(placa)
        print(f"Veículo com placa {placa} devolvido com sucesso!")
    else:
        print("Placa ou CPF inválidos ou veículo não locado por este cliente.")

# Função para mostrar o veículo mais locado
def veiculo_mais_locado():
    carro, quantidade = locadora.veiculo_mais_locado()
    if carro:
        print(f"O veículo mais locado é '{carro}' com {quantidade} locações.")
    else:
        print("Nenhum veículo foi locado ainda.")
  
#Função que mostra a quantidade de dinheiro ganhada com a Locadora      
def dinheiro_ganho():
    locadora.dinheiro_ganho()
   
#Função para listar o total de clientes 
def listar_clientes():
    locadora.listar_clientes()
    
# Função para listar os carros atualmente locados
def listar_carros_locados():
    print("Lista de carros atualmente locados:")
    carros_locados = locadora.ler_carros_locados()
    if carros_locados:
        for carro in carros_locados:
            print(carro)
    else:
        print("Nenhum carro atualmente locado.")

# Função para listar todos os carros disponíveis para locação
def listar_carros():
    print("Lista de todos os carros disponíveis para locação:")
    carros = locadora.ler_carros_disponiveis()
    if carros:
        for carro in carros:
            print(f"{carro['carro']} - Placa: {carro['placa']} - Número do Veículo: {carro['numero_veiculo']} - Preço de Locação: R$ {carro['preco_locacao']:.2f}")
    else:
        print("Nenhum carro disponível para locação.")
   
#Função para adicionar um novo carro a locadora     
def adicionar_novo_carro():
    print("Adicionar novo carro:")
    carro = input("Digite o nome do carro: ")
    placa = input("Digite a placa do carro: ")
    numero_veiculo = input("Digite o número do veículo: ")
    preco_locacao = float(input("Digite o preço de locação do carro: "))
    
    locadora.adicionar_carro(carro, placa, numero_veiculo, preco_locacao)
    print("Carro adicionado com sucesso!")

main()
