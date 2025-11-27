from banco import ContaBancaria

conta = ContaBancaria("L.Phillipe", 1000)
conta.depositar(50)
conta.sacar(30)
conta.mostrar_saldo()