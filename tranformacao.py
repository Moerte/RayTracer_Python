import math
from matriz     import Matriz
from ponto      import Ponto3D
from face       import FaceTriangular
from vetor import Vetor3D # Para Testes



class Transformacao:

    def __init__(self):

        matriz = Matriz(4, 4)
        matriz.set_entrada(1, 1, 1.0)
        matriz.set_entrada(2, 2, 1.0)
        matriz.set_entrada(3, 3, 1.0)
        matriz.set_entrada(4, 4, 1.0)
        self.matriz = matriz


    def __repr__(self):

        return "Transformação( " + str(self.matriz) + ")"

    def ponto(self, ponto):

        coluna = Matriz(4,1)
        coluna.set_coluna(1, [ponto.x, ponto.y, ponto.z, 1.0])
        res = self.matriz * coluna
        x = res.get_entrada(1, 1)
        y = res.get_entrada(2, 1)
        z = res.get_entrada(3, 1)
        w = res.get_entrada(4, 1)

        return Ponto3D(x, y, z)

    def transforma_face_triangular(self, uma_face_triangular):

        ponto1 = self.ponto(uma_face_triangular.ponto1)
        ponto2 = self.ponto(uma_face_triangular.ponto2)
        ponto3 = self.ponto(uma_face_triangular.ponto3)
        cor = uma_face_triangular.cor_phong
        nova_face = FaceTriangular(ponto1, ponto2, ponto3, cor)

        return nova_face

    def translacao(self, um_vector):

        matriz = Matriz(4,4)
        matriz.set_entrada(1, 1, 1.0)
        matriz.set_entrada(2, 2, 1.0)
        matriz.set_entrada(3, 3, 1.0)
        matriz.set_entrada(1, 4, um_vector.x)
        matriz.set_entrada(2, 4, um_vector.y)
        matriz.set_entrada(3, 4, um_vector.z)
        matriz.set_entrada(4, 4, 1.0)
        self.matriz = self.matriz * matriz

    def escalamento(self, sx, sy, sz):

        matriz = Matriz(4,4)
        matriz.set_entrada(1, 1, sz)
        matriz.set_entrada(2, 2, sy)
        matriz.set_entrada(3, 3, sx)
        matriz.set_entrada(4, 4, 1.0)
        self.matriz = self.matriz * matriz


    def shearing(self, sxy, sxz, syx, syz, szx, szy):

        matriz = Matriz(4,4)
        matriz.set_entrada(1, 1, 1.0)
        matriz.set_entrada(1, 2, sxy)
        matriz.set_entrada(1, 3, sxz)
        matriz.set_entrada(2, 1, syx)
        matriz.set_entrada(2, 2, 1.0)
        matriz.set_entrada(2, 3, syz)
        matriz.set_entrada(3, 1, szx)
        matriz.set_entrada(3, 2, szy)
        matriz.set_entrada(3, 3, 1.0)
        matriz.set_entrada(4, 4, 1.0)
        self.matriz = self.matriz * matriz

    def rotacao_z(self, angulo):

        matriz = Matriz(4, 4)
        matriz.set_entrada(1, 1, math.cos(angulo))
        matriz.set_entrada(1, 2, -math.sin(angulo))
        matriz.set_entrada(2, 1, math.sin(angulo))
        matriz.set_entrada(2, 2, math.cos(angulo))
        matriz.set_entrada(3, 3, 1.0)
        matriz.set_entrada(4, 4, 1.0)
        self.matriz = self.matriz * matriz


    def rotacao_y(self, angulo):

        matriz = Matriz(4,4)
        matriz.set_entrada(1, 1, math.cos(angulo))
        matriz.set_entrada(1, 3, math.sin(angulo))
        matriz.set_entrada(3, 1, -math.sin(angulo))
        matriz.set_entrada(3, 3, math.cos(angulo))
        matriz.set_entrada(2, 2, 1.0)
        matriz.set_entrada(4, 4, 1.0)
        self.matriz = self.matriz * matriz

    def rotacao_x(self, angulo):

        matriz = Matriz(4,4)
        matriz.set_entrada(1, 1, 1.0)
        matriz.set_entrada(2, 2, math.cos(angulo))
        matriz.set_entrada(2, 3, -math.sin(angulo))
        matriz.set_entrada(3, 2, math.sin(angulo))
        matriz.set_entrada(3, 3, math.cos(angulo))
        matriz.set_entrada(4, 4, 1.0)
        self.matriz = self.matriz * matriz

    def projecao_paralela(self, um_vetor, um_plano):

        return None

    def projecao_perespectiva(self,um_ponto, um_plano):

        return None




# Testes:
if __name__ == "__main__":
        #teste ao contrutor e ao repr

        x = Transformacao()
        print("Matriz Original: "+str(x))

        #teste à translação
        x = Transformacao()
        x.translacao(Vetor3D(1, 2, 3))
        print("Matriz Com translação: " + str(x))

        #teste ao escalonamento
        x = Transformacao()
        x.escalamento(2,3,4)
        print("Matriz Com Escalamento: " + str(x))

        #teste ao shearing
        x = Transformacao()
        x.shearing(1,2,3,4,5,6)
        print("Matriz Com Shearing: " + str(x))

        #teste à rotacao_x
        x = Transformacao()
        x.rotacao_x(1.0)
        print("Matriz Com Rotação X: " + str(x))

        # teste à rotacao_y
        x = Transformacao()
        x.rotacao_y(1.0)
        print("Matriz Com Rotação Y: " + str(x))

        # teste à rotacao_z
        x = Transformacao()
        x.rotacao_z(1.0)
        print("Matriz Com Rotação Z: " + str(x))





