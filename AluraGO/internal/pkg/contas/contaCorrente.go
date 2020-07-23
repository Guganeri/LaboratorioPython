package contas

import "github.com/Guganeri/Laboratorio/AluraGO/pkg/clientes"

type ContaCorrente struct {
	Titular       clientes.Titular
	NumeroAgencia int
	NumeroConta   int
	Saldo         float64
}

func (c *ContaCorrente) Sacar(valorDoSaque float64) string {
	podeSacar := valorDoSaque > 0 && valorDoSaque <= c.Saldo
	if podeSacar {
		c.Saldo -= valorDoSaque
		return "Saque realizado com sucessso"
	} else {
		return "Saldo insuficiente"
	}

}

func (c *ContaCorrente) Depositar(valorDoDeposito float64) (string, float64) {
	if valorDoDeposito > 0 {
		c.Saldo += valorDoDeposito
		return "Deposito realizado com sucesso", c.Saldo
	} else {
		return "O valor do deposito é inválido", c.Saldo
	}

}

func (c *ContaCorrente) Transferir(valorDaTransferencia float64, contaDesitno *ContaCorrente) bool {
	if valorDaTransferencia < c.Saldo && valorDaTransferencia > 0 {
		c.Saldo -= valorDaTransferencia
		contaDesitno.Depositar(valorDaTransferencia)
		return true
	} else {
		return false
	}
}