from arquivo05 import Produto

produto1 = Produto("Playstation 2", 350.00)
print(f"Produto: {produto1.nome_get()} | Preço: R$ {produto1.preco_get():.2f}")

produto1.nome_set("Xbox 360")
produto1.preco_set(600.00)
print(f"Produto: {produto1.nome_get()} | Preço: R$ {produto1.preco_get():.2f}")

produto1.nome_set("")
produto1.preco_set(-100)