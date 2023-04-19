import time
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


origem = '/Users/marianabelloube/Downloads/origem'
destino = '/Users/marianabelloube/Downloads/destino'


dir_tree = {
    "Imagens": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Videos": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Documentos": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Executaveis": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        
        caminho_arquivo, extensao = os.path.splitext(event.src_path)

        for chave, valor in dir_tree.items():
            
            if extensao in valor:
                nome_arquivo = os.path.basename(event.src_path)

                arquivo_na_origem = origem + '/' + nome_arquivo
                pasta_destino = destino + '/' + chave
                arquivo_no_destino = destino + '/' + chave + '/' + nome_arquivo
                
                if os.path.exists(pasta_destino):
                    print('A pasta já existe')
                    print('Movendo ' + nome_arquivo)
                    shutil.move(arquivo_na_origem, arquivo_no_destino)
                    time.sleep(1)
                else:
                    print('Criando a pasta...')
                    os.makedirs(pasta_destino)
                    print('Movendo' + nome_arquivo)
                    shutil.move(arquivo_na_origem, arquivo_no_destino)
                    time.sleep(1)


event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, origem, recursive=True)

observer.start()


try:
    while True:
        time.sleep(2)
        print('Executando...')
except KeyboardInterrupt:
    print('Interrompido')
    observer.stop()