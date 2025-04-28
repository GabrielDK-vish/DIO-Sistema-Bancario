import tkinter as tk
from tkinter import simpledialog, messagebox


saldo = 500.0
operacoes = []
saque_count = 0

def registrar_operacao(operacoes, saldo_anterior, saldo_atual):
    operacao = saldo_atual - saldo_anterior
    operacoes.append(operacao)
    return operacoes

def func_depositar():
    global saldo, operacoes
    saldo_anterior = saldo
    valor = simpledialog.askfloat("Depósito:", "Confirme o valor depositado:")
    if valor is None or valor <= 0:
        messagebox.showwarning("Tente novamente.")
        return

    saldo += valor
    operacoes = registrar_operacao(operacoes, saldo_anterior, saldo)
    messagebox.showinfo("", f"R${valor:.2f} Depositado!")


def func_sacar():
    global saldo, saque_count, operacoes
    if saque_count >= 3:
        messagebox.showwarning("", "Limite saques atingido.")
        return

    saldo_anterior = saldo
    valor = simpledialog.askfloat("Saque:", "Confirme o valor sacado:")
    if valor is None or valor <= 0:
        messagebox.showwarning("", "Saque inválido.")
        return
    if valor > 500:
        messagebox.showwarning("", "Valor de saque maior que o permitido.")
        return
    if valor > saldo:
        messagebox.showwarning("", "Saldo insuficiente.")
        return

    saldo -= valor
    saque_count += 1
    operacoes = registrar_operacao(operacoes, saldo_anterior, saldo)
    messagebox.showinfo("", f"Saque de R${valor:.2f} realizado!")


def func_extrato():
    texto = f"Saldo atual: R${saldo:.2f}\n\n"
    if operacoes:
        for i, op in enumerate(operacoes, 1):
            if op == 0:
                break
            tipo = "Depósito" if op > 0 else "Saque"
            texto += f"{i}º {tipo}: R${abs(op):.2f}\n"
    else:
        texto += ""
    messagebox.showinfo("Extrato", texto)


def func_sair():
    root.destroy()

root = tk.Tk()
root.title("Sistema Bancário - DIO")

btn_depositar = tk.Button(root, text="Depositar", width=20, command=func_depositar)
btn_depositar.pack(pady=5)

btn_sacar = tk.Button(root, text="Sacar", width=20, command=func_sacar)
btn_sacar.pack(pady=5)

btn_extrato = tk.Button(root, text="Ver Extrato", width=20, command=func_extrato)
btn_extrato.pack(pady=5)

btn_sair = tk.Button(root, text="Sair", width=20, command=func_sair)
btn_sair.pack(pady=5)

root.mainloop()
