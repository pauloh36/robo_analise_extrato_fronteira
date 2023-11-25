# imports necessarios para instalar os pacotes automaticamente

import subprocess
import sys
import importlib.util

# variaveis com o nome dos pacotes utilizados



class instalador:

    def __init__(self):

        self.pacote1 = 'xlsxwriter'
        self.pacote2 = 'pyexcel'
        self.pacote3 = 'pyexcel-xls'
        self.pacote4 = 'pyexcel-xlsx'

    def metodo_instalador_pacote(self):

        inst = instalador()

        print('Instalando pacotes...')

        # instalação dos pacotes

        if importlib.util.find_spec(inst.pacote1) is None:
               # Se o pacote não estiver instalado, instale-o
                subprocess.check_call(['pip', 'install', inst.pacote1])
                print("Instalando "+inst.pacote1+" ...  ")
        else:

           print("Pacote "+inst.pacote1+" já está instalado")


        if importlib.util.find_spec(inst.pacote2) is None:
               # Se o pacote não estiver instalado, instale-o
                subprocess.check_call(['pip', 'install', inst.pacote2, inst.pacote3, inst.pacote4])
                print("Instalando "+inst.pacote2+" "+inst.pacote2+" "+inst.pacote3+" ...  ")

        else:

           print("Pacote "+inst.pacote2+" "+inst.pacote2+" "+inst.pacote3+" já está instalado")

