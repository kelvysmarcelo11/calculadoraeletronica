import math

class Calculator:
    def __init__(self):
        self.resultado = 0
        self.modo_angulo = 'rad'

    def adicionar(self, x, y):
        self.resultado = x + y
        return self.resultado

    def subtrair(self, x, y):
        self.resultado = x - y
        return self.resultado

    def multiplicar(self, x, y):
        self.resultado = x * y
        return self.resultado

    def dividir(self, x, y):
        if y == 0:
            raise ValueError("Divisão por zero não é permitida")
        self.resultado = x / y
        return self.resultado

    def potencia(self, x, y):
        self.resultado = x ** y
        return self.resultado

    def raiz_quadrada(self, x):
        if x < 0:
            raise ValueError("Raiz quadrada de um número negativo não é permitida")
        self.resultado = math.sqrt(x)
        return self.resultado

    def exponencia(self, x, y):
        self.resultado = math.exp(y * math.log(x))
        return self.resultado

    def seno(self, x):
        if self.modo_angulo == 'deg':
            x = math.radians(x)
        self.resultado = math.sin(x)
        return self.resultado

    def cosseno(self, x):
        if self.modo_angulo == 'deg':
            x = math.radians(x)
        self.resultado = math.cos(x)
        return self.resultado

    def tangente(self, x):
        if self.modo_angulo == 'deg':
            x = math.radians(x)
        self.resultado = math.tan(x)
        return self.resultado

    def alterar_modo(self):
        if self.modo_angulo == 'rad':
            self.modo_angulo = 'deg'
        else:
            self.modo_angulo = 'rad'

def mostrar_menu(calculadora):
    print("Calculadora Científica")
    print("-------------------")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potencia")
    print("6. Raiz Quadrada")
    print("7. Exponencia")
    print("8. Seno (em radianos)")
    print("9. Cosseno (em radianos)")
    print("10. Tangente (em radianos)")
    print("11. Seno (em graus)")
    print("12. Cosseno (em graus)")
    print("13. Tangente (em graus)")
    print("14. Alterar modo de ângulo (atualmente em " + calculadora.modo_angulo + ")")
    print("15. Sair")

def main():
    calculadora = Calculator()

    while True:
        try:
            mostrar_menu(calculadora)
            operacao = int(input("Digite o número da operação desejada: "))

            if operacao == 1:
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                print(f"O resultado da adição é: {calculadora.adicionar(x, y)}")

            elif operacao == 2:
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                print(f"O resultado da subtração é: {calculadora.subtrair(x, y)}")

            elif operacao == 3:
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                print(f"O resultado da multiplicação é: {calculadora.multiplicar(x, y)}")

            elif operacao == 4:
                x = float(input("Digite o primeiro número: "))
                y = float(input("Digite o segundo número: "))
                try:
                    print(f"O resultado da divisão é: {calculadora.dividir(x, y)}")
                except ValueError as e:
                    print(e)

            elif operacao == 5:
                x = float(input("Digite o número base: "))
                y = float(input("Digite o expoente: "))
                print(f"O resultado da potenciação é: {calculadora.potencia(x, y)}")

            elif operacao == 6:
                x = float(input("Digite o número: "))
                print(f"A raiz quadrada de {x} é: {calculadora.raiz_quadrada(x)}")

            elif operacao == 7:
                x = float(input("Digite o número base: "))
                y = float(input("Digite o expoente: "))
                print(f"O resultado da exponenciação é: {calculadora.exponencia(x, y)}")

            elif operacao == 8:
                x = float(input("Digite o ângulo em radianos: "))
                print(f"O seno de {x} radianos é: {calculadora.seno(x)}")

            elif operacao == 9:
                x = float(input("Digite o ângulo em radianos: "))
                print(f"O cosseno de {x} radianos é: {calculadora.cosseno(x)}")

            elif operacao == 10:
                x = float(input("Digite o ângulo em radianos: "))
                print(f"A tangente de {x} radianos é: {calculadora.tangente(x)}")

            elif operacao == 11:
                x = float(input("Digite o ângulo em graus: "))
                print(f"O seno de {x} graus é: {calculadora.seno(x):.2f}")

            elif operacao == 12:
                x = float(input("Digite o ângulo em graus: "))
                print(f"O cosseno de {x} graus é: {calculadora.cosseno(x):.2f}")

            elif operacao == 13:
                x = float(input("Digite o ângulo em graus: "))
                print(f"A tangente de {x} graus é: {calculadora.tangente(x):.2f}")

            elif operacao == 14:
                calculadora.alterar_modo()
                print(f"O modo de ângulo foi alterado para {calculadora.modo_angulo}.")

            elif operacao == 15:
                print("Até a próxima!")
                break

            else:
                print("Opção inválida. Digite um número entre 1 e 15.")

        except ValueError:
            print("Digite um número válido.")

if __name__ == "__main__":
    main()