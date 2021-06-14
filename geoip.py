import subprocess
import sys
from multiprocessing import Pool

pool = Pool()
posicion = 1

if len(sys.argv) > 1:
    comando = "%s" % (sys.argv[posicion])

    if comando.endswith('.txt'):
        with open(comando) as f:
            for line in f:
                pool.apply_async(subprocess.call(["geoiplookup",line.strip()]))
    else:
        parametros = len(sys.argv) - 1
        while (parametros >= posicion):
            pool.apply_async(subprocess.call(["geoiplookup", comando]))
            posicion = posicion + 1
else:
    print("No empty parameters!")