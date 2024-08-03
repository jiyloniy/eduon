def factorial_qoshish_optimal(n):
    if n == 0 or n == 1:
        return 1
    
    natijalar = [1, 1]  # 0! va 1! uchun natijalar
    
    for i in range(2, n + 1):
        yangi_natija = 0
        for _ in range(i):
            yangi_natija += natijalar[-1]
        natijalar.append(yangi_natija)
    
    return natijalar[-1]

# Dasturni sinab ko'rish
print(factorial_qoshish_optimal(5))  # 5! = 120 ni chiqarishi kerak
print(factorial_qoshish_optimal(7))  # 7! = 5040 ni chiqarishi kerak
print(factorial_qoshish_optimal(1000))  # 7! = 5040 ni chiqarishi kerak
