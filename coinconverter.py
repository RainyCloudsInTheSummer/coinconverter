import requests

def converter_moeda(valor, de_moeda, para_moeda):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de_moeda.upper()}&to={para_moeda.upper()}"
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print("Erro ao acessar a API.")
        return None

    dados = resposta.json()
    return dados['rates'][para_moeda.upper()]

if __name__ == "__main__":
    print("=== Conversor de Moedas ===")
    valor = float(input("Digite o valor: "))
    de_moeda = input("Converter de (ex: USD): ")
    para_moeda = input("Para (ex: BRL): ")

    resultado = converter_moeda(valor, de_moeda, para_moeda)
    if resultado:
        print(f"{valor:.2f} {de_moeda.upper()} = {resultado:.2f} {para_moeda.upper()}")
