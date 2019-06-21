class Vetor3D:

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

        return "Vetor3D(" + str(self.x) + ", " \
                        + str(self.y) + ", " \
                        + str(self.z) + ")" \
    
    def adiciona(self, outro_vetor):

        novo_x=self.x + outro_vetor.x
        novo_y=self.y + outro_vetor.y
        novo_z=self.z + outro_vetor.z
        vetor_soma=Vetor3D(novo_x,novo_y,novo_z)
        return vetor_soma
    
    def __add__(self, outro_vetor):
        
        return self.adiciona(outro_vetor)
    
    def multiplica_escalar(self, escalar):

        novo_x=self.x * escalar
        novo_y=self.y * escalar
        novo_z=self.z * escalar
        resultado=Vetor3D(novo_x,novo_y,novo_z)
        return resultado
    
    def __mul__(self, escalar):

        return self. multiplica_escalar(escalar)
    
    def comprimento(self):

        x=self.x
        y=self.y
        z=self.z
        return (x*x + y*y + z*z)**(0.5)
    
    def versor(self):

        fator = 1.0 / self.comprimento()
        return self * fator
    
    def interno(self, outro_vetor):

        return self.x * outro_vetor.x \
                + self.y * outro_vetor.y \
                + self.z * outro_vetor.z
                
    def externo(self, outro_vetor):

        ux=self.x
        uy=self.y
        uz=self.z
        vx=outro_vetor.x
        vy=outro_vetor.y
        vz=outro_vetor.z
        x=uy*vz-vy*uz
        y=-(ux*vz-uz*vx)
        z=ux*vy-uy*vx
        resultado = Vetor3D(x,y,z)
        return resultado

if __name__ == "__main__":
    
    print("\n#teste ao construtor")

    v1 = Vetor3D(1.0, 2.0, 3.0)

    # teste a get_x
    print("coordenada x de v1 = ")
    print(v1.get_x())

    # teste a get_y
    print("coordenada y de v1 = ")
    print(v1.get_y())

    # teste a get_z
    print("coordenada z de v1 = ")
    print(v1.get_z())

    # teste a __repr__
    print("v1 = ")
    print(v1)
    
    # teste a adiciona
    v2 = Vetor3D(10.0, 20.0, 30.0)
    v3 = v1.adiciona(v2)
    print("v1 = ")
    print(v1)
    print("v2 = ")
    print(v2)
    print("v3 = ")
    print(v3)

    # teste a +
    v4 = v1 + v2
    print("v4 = ")
    print(v4)
    
    # teste a multiplica_escalar
    a = 2.0
    v5 = v1.multiplica_escalar(a)
    print("v5 = ")
    print(v5)
    
    # teste a *
    v6 = v1 * a
    print("v6 = ")
    print(v6)
    
    # teste a comprimento
    v7 = Vetor3D(3.0, 0.0, 4.0)
    cv7 = v7.comprimento()
    print("v7 = ")
    print(v7)
    print("comprimento de v7 = ")
    print(cv7)
    
    print("# teste a versor")
    vv7 = v7.versor()
    cvv7 = vv7.comprimento()
    print("vv7 = " + str(vv7))
    print("comprimento de vv7 = " + str(cvv7))
    
    # teste a interno
    print("v1 =")
    print(v1)
    print("v7 =")
    print(v7)
    iv1v7 = v1.interno(v7)
    print("v1 interno v7 = ")
    print(iv1v7)

    # teste a externo
    e = v1.externo(v7)
    print("e = v1 externo v7 = ")
    print(e)
    print("v1 interno e = ")
    print(v1.interno(e))
    print("v7 interno e = ")
    print(v7.interno(e))