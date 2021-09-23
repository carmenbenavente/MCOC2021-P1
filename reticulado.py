<<<<<<< HEAD
from scipy.linalg import solve
from barra import Barra
import numpy as np
from scipy.linalg import solve
from barra import Barra
#bar = Barra()
class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        
        


    def agregar_nodo(self, x, y, z=0):
        
        

        print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        
        corn = self.xyz[n,:]
        
        
        #print(f"la posicion del nodo {n} es en las cordenadas =  {corn}")
        return corn
    def calcular_peso_total(self):
        pesototalbarras = 0
        for barra in self.barras:
            w_barra= barra.calcular_peso(self)
            pesototalbarras+= w_barra
        
        return pesototalbarras

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        print(f"Quiero agregar una restriccion en: ({nodo} {gdl} {valor})")
        
        if self.restricciones[nodo].index(nodo) == ValueError: #Si el nodo no está en las restricciones, se agrega
            
            self.restricciones[nodo] = []
            self.restricciones[nodo].append(gdl, valor)
            return 0
        else :
            self.restricciones[nodo].append(gdl, valor)
            return 0
        
       # print (restricciones)
        

        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        print(f"Quiero agregar una fuerza en: ({nodo} {gdl} {valor})")

        if self.cargas.index(nodo) == ValueError : #Si no existe el nodo, se agrega.
            
            self.cargas[nodo] = []
            self.cargas[nodo].append(gdl, valor)
            return 0
        else:
                    
            self.cargas[nodo].append(gdl, valor)
            return 0
        
            #print (cargas)
        
        
       


    def ensamblar_sistema(self):
        
        for e in self.barras: #recore las barras #barras tiene [N°barra | ni | nj]
            ni = self.barras[1] 
            nj = self.barras[2]
            
            ke = e.obtener_rigidez()
            fe = e.obtener_vector_de_carga()
            
            d = [3*ni,3*ni+1, 3*ni+2,3*nj,3*nj+1,3*nj+2]
            
            for i in range(6):
                p = d[i]
                for j in range(6):
                    q = d[j]
                    K[p,q] += k_e[i,j]
                f[p] += f_e[i]
            
            #agregar cargas puntuales
            
            for nodo in cargas:
                    print(nodo)
                    Ncargas = len(cargas[nodo])
                    print(Ncargas)
                    
                    for carga in range :
                        
                        gdl = cargas[nodo][0]
                        f = cargas[nodo][1]
                        print(f"Agregando carga de {f} en GDL {gdl}")
                        
                        gdl_global = 3*node + gdl
                        F[gdl_global] += f
           # 
           #
           #
           
           #self.K #matriz rigidez
           #self.u # grados de libertad
        return 0

    def resolver_sistema(self):

        grados_totales = np.arange(self.Nnodos * 3)
        gdl_c = []
        for i in self.restricciones:
            for j in self.restricciones[i]:
                gdl, valor = j[0], j[1]
                gdl_global = gdl + i * 3
                self.u[gdl_global] += valor
                gdl_c.append(gdl_global)

        np.array(gdl_c)
        gdl_f = np.setdiff1d(grados_totales, gdl_c)

        for i in self.cargas:
            for j in self.cargas[i]:
                gdl, valor = j[0], j[1]
                gdl_global = gdl + i * 3
                self.f[gdl_global] += valor

        self.Ff = self.F[gdl_f]
        self.Fc = self.F[gdl_c]
        self.Kcc = self.K[np.ix_(gdl_c, gdl_c)]
        self.Kff = self.K[np.ix_(gdl_f, gdl_f)]
        self.Kfc = self.K[np.ix_(gdl_f, gdl_c)]
        self.Kcf = self.K[np.ix_(gdl_c, gdl_f)]

        self.uf = self.u[gdl_f]
        self.uc = self.u[gdl_c]

        self.R = solve(self.Kff, self.Ff - self.Kfc @ self.uc)

        self.u[gdl_f] = self.R

        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""	
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0







    def __str__(self):

        s = "Soy un reticulado :) \n"

        s += "Nodos: \n"

        for i in range(self.Nnodos):
            s += f"{i} : ({self.xyz[i][0]}, {self.xyz[i][1]}, {self.xyz[i][2]})\n"
            i += 1

        s += "Barras: \n"

        h = 0
        for i in self.barras:
            s += f"{h} : [{self.barras[h].ni} {self.barras[h].nj}]\n"
            h += 1

        return s

=======
import numpy as np
from scipy.linalg import solve
from barra import Barra
import numpy as np
from scipy.linalg import solve
from barra import Barra
#bar = Barra()
class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        
        


    def agregar_nodo(self, x, y, z=0):
        
        

        print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos

        self.xyz[numero_de_nodo_actual,:] = [x, y, z]

        self.Nnodos += 1
        
        return 0

    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        
        corn = self.xyz[n,:]
        
        
        print(f"la posicion del nodo {n} es en las cordenadas =  {corn}")
        return corn
    def calcular_peso_total(self):
        pesototalbarras = 0
        for barra in self.barras:
            w_barra= barra.calcular_peso()
            pesototalbarras+= w_barra
        
        return pesototalbarras

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        
        """Implementar"""	
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        """Implementar"""	
        
        return 0


    def ensamblar_sistema(self):
        
        """Implementar"""	
        
        return 0



    def resolver_sistema(self):
        
        """Implementar"""	
        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""	
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""	
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""	
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""	
        
        return 0







    def __str__(self):

        s = "Soy un reticulado :) \n"

        s += "Nodos: \n"

        for i in range(self.Nnodos):
            s += f"{i} : ({self.xyz[i][0]}, {self.xyz[i][1]}, {self.xyz[i][2]})\n"
            i += 1

        s += "Barras: \n"

        h = 0
        for i in self.barras:
            s += f"{h} : [{self.barras[h].ni} {self.barras[h].nj}]\n"
            h += 1

        return s


