import math

print(math.sqrt(81))

##########################

# importar uma ou mais funções especificas

from math import sqrt, sin

print(sqrt(81))

##########################

# importar o modulo mas não ficar escrevendo no nome do módulo sempre
# mas não muito recomendado pois pode dar conflito com outros modúlos importados

from math import *

print(sqrt(81))

###########################

# importar mas usar outro nomes para os módulos 

import math as m

print(m.sqrt(144))