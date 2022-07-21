import requests

def buscar_avatar(usuario):
   """
   Busca um avatar dentro do ghuithub
   :param usuario: str com nome de usuario no guithub
   :return: str com o link do avatar
   
   """
   url = f'https://api.github.com/users/{usuario}'
   resp = requests.get(url)
   return resp.json()['avatar_url']

if __name__ == '__main__':
    print(buscar_avatar('CleitonTyukrs'))