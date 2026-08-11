def ativacao_degrau(z):
    if z >= 0:
        return 1
    return 0

def prever(entradas, pesos, bias):
    # Cálculo linear ( z = (x1 * w2) + (x2 * w2) ... (x999 * w999) + bias)
    z = bias

    for i in range(len(entradas)):
        z += entradas[i] * pesos[i]

    decisao = ativacao_degrau(z)
    return decisao, z

if __name__ == "__main__":
    pesos_modelo = [0.8, 0.3]
    bias_modelo = -7.0

    # Cenários de teste
    cenarios = [
        { "nome": "Ana", "entradas": [8, 7] },
        { "nome": "Pedro", "entradas": [4, 3] },
    ]

    for c in cenarios:
        resultado, valor_z = prever(c["entradas"], pesos_modelo, bias_modelo)
        status = "Upgrade Concedido!" if resultado == 1 else "Upgrade Negado."
        print(f"Hóspede: {c['nome']} | Entradas: {c['entradas']} -> Z: {valor_z} | Decisão: {status}")