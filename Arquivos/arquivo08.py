from arquivo07 import ContaBancaria

conta1 = ContaBancaria("Renato", 2000.00)

print(f"Titular: {conta1.get_titular()} | Saldo: {conta1.get_saldo():.2f}")

conta1.set_titular("Renato Silva")
conta1.set_saldo(2500.00)
print(f"Titular:{conta1.get_titular()} | Saldo:{conta1.get_saldo():.2f}")

conta1.set_titular("")
conta1.set_saldo(-180)
