def divisao_segura():
    try:
        # Solicita os dois números ao utilizador
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Realiza a divisão
        resultado = num1 / num2
        
    except ValueError:
        # Trata o erro caso o utilizador digite letras ou caracteres inválidos
        print("Erro: Por favor, digite apenas números válidos.")
        
    except ZeroDivisionError:
        # Trata o erro de tentativa de divisão por zero
        print("Erro: não é possível dividir por zero.")
        
    else:
        # Executado apenas quando a divisão ocorre sem erros
        print(f"Resultado: {resultado}")
        
    finally:
        # Executado SEMPRE, independentemente de ocorrer erro ou não
        print("Operação finalizada.")

if __name__ == "__main__":
    divisao_segura()