print("n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?")
n=int(input("Введите кол-во школьников:"))
print("Кол-во школьников: ", n)
k=int(input("Введите кол-во яблок:"))
print("Кол-во яблок: ", k)
f=k/n
print("Каждому школьнику достанется яблок: ", f)
g=k%n
print("В корзине останется яблок: ", g)
