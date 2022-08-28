from televisores.tv import TV
from televisores.control import Control
from televisores.marca import Marca

if __name__ == "__main__":
    marca = Marca("Xiomi")

    tv1 = TV(marca, True)

    ok = False
    if(tv1.getPrecio() == 500 and tv1.getCanal() == 1 and tv1.getVolumen() == 1):
        ok = True
    
    print(ok)

