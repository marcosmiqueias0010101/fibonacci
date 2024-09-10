def fibonacci(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    if n in fib_sequence:
        return fib_sequence, True
    else:
        return fib_sequence, False

# Entrada do usuário
num = int(input("Informe um número: "))
sequence, exists = fibonacci(num)
print(f"Sequência de Fibonacci até {num}: {sequence}")
print(f"O número {num} {'pertence' if exists else 'não pertence'} à sequência.") 
cd caminho/para/seu/diretorio
git init
git commit -m "Adiciona código da sequência de Fibonacci"
git remote add origin https://github.com/https://github.com/marcosmiqueias0010101/fibonacci.git
git push -u origin master

