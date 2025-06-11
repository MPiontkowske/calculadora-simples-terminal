import os
from colorama import init, Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    clear_screen()
    print(f"{Fore.CYAN}=== Calculadora Simples ==={Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}Operações disponíveis:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} Adição (+)")
    print(f"{Fore.GREEN}[2]{Style.RESET_ALL} Subtração (-)")
    print(f"{Fore.GREEN}[3]{Style.RESET_ALL} Multiplicação (*)")
    print(f"{Fore.GREEN}[4]{Style.RESET_ALL} Divisão (/)")
    print(f"{Fore.GREEN}[5]{Style.RESET_ALL} Potenciação (^)")
    print(f"{Fore.GREEN}[6]{Style.RESET_ALL} Raiz quadrada (√)")
    print(f"{Fore.RED}[0]{Style.RESET_ALL} Sair")
    print("\n" + "="*30 + "\n")

def calculator():
    init()  # Inicializa o Colorama
    while True:
        print_menu()
        
        try:
            operacao = input(f"{Fore.YELLOW}Escolha uma operação (0-6): {Style.RESET_ALL}")
            
            if operacao == '0':
                print(f"\n{Fore.GREEN}Obrigado por usar a calculadora!{Style.RESET_ALL}")
                break
            
            if operacao not in ['1', '2', '3', '4', '5', '6']:
                print(f"\n{Fore.RED}Operação inválida! Por favor, escolha uma opção válida.{Style.RESET_ALL}")
                input("\nPressione Enter para continuar...")
                continue

            if operacao == '6':
                num = float(input(f"\n{Fore.CYAN}Digite o número para calcular a raiz quadrada: {Style.RESET_ALL}"))
                if num < 0:
                    print(f"{Fore.RED}Não é possível calcular a raiz quadrada de um número negativo!{Style.RESET_ALL}")
                    input("\nPressione Enter para continuar...")
                    continue
                resultado = num ** 0.5
                print(f"\n{Fore.GREEN}√{num} = {resultado}{Style.RESET_ALL}")
            else:
                num1 = float(input(f"\n{Fore.CYAN}Digite o primeiro número: {Style.RESET_ALL}"))
                num2 = float(input(f"{Fore.CYAN}Digite o segundo número: {Style.RESET_ALL}"))

                if operacao == '1':
                    resultado = num1 + num2
                    print(f"\n{Fore.GREEN}{num1} + {num2} = {resultado}{Style.RESET_ALL}")
                elif operacao == '2':
                    resultado = num1 - num2
                    print(f"\n{Fore.GREEN}{num1} - {num2} = {resultado}{Style.RESET_ALL}")
                elif operacao == '3':
                    resultado = num1 * num2
                    print(f"\n{Fore.GREEN}{num1} * {num2} = {resultado}{Style.RESET_ALL}")
                elif operacao == '4':
                    if num2 == 0:
                        print(f"{Fore.RED}Erro: Divisão por zero não é permitida!{Style.RESET_ALL}")
                        input("\nPressione Enter para continuar...")
                        continue
                    resultado = num1 / num2
                    print(f"\n{Fore.GREEN}{num1} / {num2} = {resultado}{Style.RESET_ALL}")
                elif operacao == '5':
                    resultado = num1 ** num2
                    print(f"\n{Fore.GREEN}{num1} ^ {num2} = {resultado}{Style.RESET_ALL}")

            input("\nPressione Enter para continuar...")

        except ValueError:
            print(f"\n{Fore.RED}Erro: Por favor, digite apenas números válidos!{Style.RESET_ALL}")
            input("\nPressione Enter para continuar...")
        except Exception as e:
            print(f"\n{Fore.RED}Ocorreu um erro: {e}{Style.RESET_ALL}")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    calculator() 
