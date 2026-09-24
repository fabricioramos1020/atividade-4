def saque_bancario():
    try:
        # Solicita o saldo e o valor do saque ao utilizador
        saldo = float(input("Informe o saldo da conta: "))
        saque = float(input("Informe o valor do saque: "))
        
        # Lança uma exceção se o valor do saque for menor ou igual a zero
        if saque <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
            
        # Lança uma exceção se o valor do saque for maior que o saldo disponível
        if saque > saldo:
            raise Exception("Saldo insuficiente para realizar a operação.")
            
    except ValueError as e:
        # Captura entradas inválidas (ex: texto) ou o erro de valor de saque <= 0
        if str(e).startswith("could not convert"):
            print("Erro: Por favor, informe um valor numérico válido.")
        else:
            print(f"Erro: {e}")
            
    except Exception as e:
        # Captura a exceção de saldo insuficiente lançada pelo 'raise'
        print(f"Erro: {e}")
        
    else:
        # Executa quando o saque é válido: calcula e mostra o saldo restante
        saldo_restante = saldo - saque
        print("Saque realizado com sucesso!")
        print(f"Saldo restante: R$ {saldo_restante:.2f}")
        
    finally:
        # Exibido sempre no término da operação
        print("Operação bancária finalizada.")

if __name__ == "__main__":
    saque_bancario()