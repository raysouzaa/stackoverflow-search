# pip install requests
import sys
import requests

# O objetivo dessa aplicação é otimizar uma busca por informações no Stack
# Overflow. Isso é feito automatizando um busca via linha de comandos usando
# diretamente a API do StackExchange.
# Os resultados são visualizados diretamente no terminal e os links podem ser
# usados para acessar as respostas na página do https:// stackoverflow.com 

URL_BASE = "https://api.stackexchange.com/2.2"

# Parametros padrão, vão ser usados em todas as requisições 
query_params = {
        "order": "desc",
        "sort": "votes",
        "site": "stackoverflow",
        "pagesize": "10"
};

def main():
    api_endpoint = URL_BASE + "/search/advanced"

    # Verifica se a lista de argumentos está vazia
    if len(sys.argv) < 2:
        print('ERRO: Faltando o argumento: [Texto da busca]')
        exit(1)

    # Pega o primeiro argumento passado via linha de comandos
    arg = sys.argv[1]
    arg = str(arg)

    # Adiciona o argumento na requisição
    query_params['q'] = arg
    
    # Faz a requisição
    # r é o objeto com a resposta
    r = requests.get(api_endpoint, params=query_params)

    if r.status_code == 200:
        json = r.json()
        items = json['items']

        print('As', len(items), 'perguntas com melhor score\n')

        # Iteracao pelos objetos retornados
        for item in items:
            print(item['title'])
            print(item['link'])
            if item['is_answered']:
                print(f'Numero de respostas: {item["answer_count"]}')
            print(f"Score: {item['score']}\n")

    elif 400 <= r.status_code < 500:
        print(f'Erro. Status = {r.status_code}')


if __name__ == '__main__':
    main()

