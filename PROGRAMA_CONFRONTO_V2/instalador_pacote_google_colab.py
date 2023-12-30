# imports necessarios para instalar os pacotes automaticamente

import subprocess
import importlib.util

# variaveis com o nome dos pacotes utilizados

pacote1 = 'xlsxwriter'
pacote2 = 'pyexcel'
pacote3 = 'pyexcel-xls'
pacote4 = 'pyexcel-xlsx'


print('Instalando pacotes...')

# instalação dos pacotes

if importlib.util.find_spec(pacote1) is None:
       # Se o pacote não estiver instalado, instale-o
        subprocess.check_call(['pip', 'install', pacote1])
        print("Instalando "+pacote1+" ...  ")
else:

   print("Pacote "+pacote1+" já está instalado")


if importlib.util.find_spec(pacote2) is None:
       # Se o pacote não estiver instalado, instale-o
        subprocess.check_call(['pip', 'install', pacote2, pacote3, pacote4])
        print("Instalando "+pacote2+" "+pacote2+" "+pacote3+" ...  ")

else:

   print("Pacote "+pacote2+" "+pacote2+" "+pacote3+" já está instalado")

