from plano import Plano
from plano import ErroPontosColineares
from ponto import Ponto3D
from cor_rgb import CorRGB
from cor_phong import CorPhong

class FaceTriangular(Plano):
    
    def __init__ (self, ponto1, ponto2, ponto3, cor_phong): #por default este parametro é falso
        
        #Plano.__init__(self, ponto1, ...) 
        super().__init__(ponto1, ponto2, ponto3)
        
        self.cor_phong = cor_phong
       # self.espelhado = espelhado
    
    def __repr__(self):
        
        resultado = "FaceTriangular(" + super().__repr__() + ", " + str(self.cor_phong) + ")" + "\n"
        return resultado

    def get_cor_phong(self):
        
        return self.cor_phong
        
       
# Testes:   
if __name__ == "__main__":
        
    print("# teste ao construtor")
    a = Ponto3D(0.0, 0.0, 0.0)
    b = Ponto3D(1.0, 0.0, 0.0)
    c = Ponto3D(0.0, 1.0, 0.0)
    k_ambiente = CorRGB(0.0, 0.0, 0.1)
    k_difusa = CorRGB(0.0, 0.0, 0.75)
    k_especular = CorRGB(1.0, 1.0, 1.0)
    brilho = 100.0
    cor = CorPhong(k_ambiente, k_difusa, k_especular, brilho)
    face1 = FaceTriangular(a, b, c, cor)
    print("Até aqui não foram lançadas exceções.")
    
    print()
    print("# teste à exceção ErroPontosColineares")
    try:
        face2 = FaceTriangular(a, a, c, cor)
    except ErroPontosColineares:
        print("Ao tentar definir-se a face face2 = FaceTriangular(a, a, c, cor)")
        print("foi lançada a exceção ErroPontosColineares.")
        print("É o comportamento herdado da classe Plano.")
    
    print()
    print("# teste a __repr__")
    print(face1)
    print()
    
    print("# teste a get_cor_phong")
    print(face1.get_cor_phong())