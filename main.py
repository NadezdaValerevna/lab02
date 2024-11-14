def sieve_of_eratosthenes(n):
    # Шаг 1: Инициализация
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 и 1 не простые числа

    # Шаг 2: Основной цикл
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            # Удалить все кратные числа p
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False

    # Шаг 3: Сбор простых чисел
    prime_numbers = [i for i in range(n + 1) if is_prime[i]]

    return prime_numbers


# Пример использования
n = int(input("Введите предел для поиска простых чисел: "))
primes = sieve_of_eratosthenes(n)
print(f"Простые числа до {n}: {primes}")