from vetor import Vetor3D

class Ponto3D:
    
    def __init__(self, x, y, z):
        
        self.x=x
        self.y=y
        self.z=z
    
    def get_x(self):
        
        return self.x
    
    def get_y(self):
        
        return self.y
    
    def get_z(self):
        
        return self.z
    
    def __repr__(self):
        
        return "Ponto3D(" + str(self.x) + "," \
                        + str(self.y) + "," \
                        + str(self.z) + ")"
        
    def adiciona_vetor(self, um_vetor):
        
        novo_x = self.x + um_vetor.x
        novo_y = self.y + um_vetor.y
        novo_z = self.z + um_vetor.z
        novo_ponto = Ponto3D(novo_x,novo_y,novo_z)
        return novo_ponto
    
    def __add__(self, um_vetor):
        
        return self.adiciona_vetor(um_vetor)
    
    #>AB = B - A
    #self.subtrai_ponto(ponto_inicial)
    
    def subtrai_ponto(self, ponto_inicial):
        
        novo_x = self.x - ponto_inicial.x
        novo_y = self.y - ponto_inicial.y
        novo_z = self.z - ponto_inicial.z
        novo_vetor = Vetor3D(novo_x,novo_y,novo_z)
        
        return novo_vetor
    
    def __sub__(self, ponto_inicial):
        
        return self.subtrai_ponto(ponto_inicial)
    
if __name__ == "__main__":

    print("\n# teste ao construtor")
    p1 = Ponto3D(1.0, 2.0, 3.0)
    
    print("\n# teste a get_x")
    print("coordenada x de p1 = ")
    print(p1.get_x())

    print("\n# teste a get_y")
    print("coordenada y de p1 = ")
    print(p1.get_y())
    
    print("\n# teste a get_z")
    print("coordenada z de p1 = ")
    print(p1.get_z())
    
    print("\n# teste a __repr__")
    print("p1 = ")
    print(p1)

    print("\n# teste a adiciona_vetor")
    v1 = Vetor3D(10.0, 20.0, 30.0)
    p2 = p1.adiciona_vetor(v1)
    print("v1 = ")
    print(v1)
    print("p2 = ")
    print(p2)
    
    #Vetor mais ponto não se define. Tem de ser ponto mais vetor.
    
    print("\n# teste a +")
    p3 = p1 + v1
    print("p3 = p1 + v1 = ")
    print(p3)

    print("\n# teste a subtrai_ponto")
    v2 = p2.subtrai_ponto(p1)
    print(p1)
    print(p2)
    print("v2 = ")
    print(v2)
    
    print("\n# teste a -")
    v3 = p2 - p1
    print("v3 = ")
    print(v3)