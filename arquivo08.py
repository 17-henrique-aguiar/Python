from arquivo07 import ContaBancaria

conta1 = ContaBancaria("Renato", 2000.00)

print(f"Titular: {conta1.get_titu()} | Saldo: {conta1.get_saldo():.2f}")

conta1.set_titu("Renato Silva")
conta1.set_saldo(2500.00)
print(f"Titular:{conta1.get_titu()} | Saldo:{conta1.get_saldo():.2f}")

conta1.set_titu("")
conta1.se1_saldo(-180)