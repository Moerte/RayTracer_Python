from ponto import Ponto3D
from matriz import Matriz
from reta import Reta

TOLERANCIA_ZERO = 10.0 ** (-10)


class ErroPontosColineares(Exception):
    """ Exceção """


class Plano:

    def __init__(self, ponto1, ponto2, ponto3):

        self.ponto1 = ponto1
        self.ponto2 = ponto2
        self.ponto3 = ponto3
        v12 = ponto2 - ponto1
        v13 = ponto3 - ponto1
        normal = v12.externo(v13)
        if normal.comprimento() < TOLERANCIA_ZERO:
            raise ErroPontosColineares
        self.normal = normal.versor()

    def __repr__(self):

        p1 = str(self.ponto1)
        p2 = str(self.ponto2)
        p3 = str(self.ponto3)
        n = str(self.normal)
        resultado = "Plano(" + p1+ ", " + p2 + ", " + p3 + ", " + n + ")"
        return resultado

    def interceta_triangulo(self, reta):

        #plano
        ax = self.ponto1.x
        ay = self.ponto1.y
        az = self.ponto1.z

        bx = self.ponto2.x
        by = self.ponto2.y
        bz = self.ponto2.z

        cx = self.ponto3.x
        cy = self.ponto3.y
        cz = self.ponto3.z

        #reta
        vx = reta.get_vetor_diretor().x
        vy = reta.get_vetor_diretor().y
        vz = reta.get_vetor_diretor().z

        px = reta.get_origem().x
        py = reta.get_origem().y
        pz = reta.get_origem().z


        M = Matriz(3, 3)
        M.set_linha(1, [ax - bx, ax - cx, vx])
        M.set_linha(2, [ay - by, ay - cy, vy])
        M.set_linha(3, [az - bz, az - cz, vz])

        detM = M.det()

        if abs(detM) < TOLERANCIA_ZERO:  # em torno de zero ~0

            return [False, None, None]

        M3 = Matriz(3, 3)
        M3.set_linha(1, [ax - bx, ax - cx, ax - px])
        M3.set_linha(2, [ay - by, ay - cy, ay - py])
        M3.set_linha(3, [az - bz, az - cz, az - pz])

        t = M3.det() / detM

        if t < TOLERANCIA_ZERO:
            return [False, None, None]

        M1 = Matriz(3, 3)
        M1.set_linha(1, [ax - px, ax - cx, vx])
        M1.set_linha(2, [ay - py, ay - cy, vy])
        M1.set_linha(3, [az - pz, az - cz, vz])

        tB = M1.det() / detM

        if tB < 0.0 or tB > 1.0:  # maior ou menor nao depende do arrendondamento

            return [False, None, None]

        M2 = Matriz(3, 3)
        M2.set_linha(1, [ax - bx, ax - px, vx])
        M2.set_linha(2, [ay - by, ay - py, vy])
        M2.set_linha(3, [az - bz, az - pz, vz])

        tC = M2.det() / detM

        if tC < 0.0 or tC > 1.0:  # maior ou menor nao depende do arrendondamento

            return [False, None, None]

        # tA = 1.0 - tB - tC

        tA = 1.0 - tB - tC

        if tA < 0.0 or tA > 1.0:  # maior ou menor nao depende do arrendondamento

            return [False, None, None]

        # A interseção é dentro do triângulo

        A = self.ponto1
        B = self.ponto2
        C = self.ponto3

        # multiplicar o escalar à direita

        ponto_intercecao = self.ponto1 + ((B - A) * tB) + ((C - A) * tC)

        return [True, ponto_intercecao, t]


if __name__ == "__main__":

    # teste ao construtor
    a = Ponto3D(0.0, 0.0, 0.0)
    b = Ponto3D(2.0, 0.0, 0.0)
    c = Ponto3D(0.0, 2.0, 0.0)
    plano1 = Plano(a, b, c)
    print("Até aqui não foram lançadas exceções.")
    # teste a TOLERANCIA_ZERO
    print("TOLERANCIA_ZERO = " + str(TOLERANCIA_ZERO))
    # teste à exceção ErroPontosColineares
    try:
        plano2 = Plano(a, b, b)
    except ErroPontosColineares:
        print("Ao tentar definir-se o plano plano2 = Plano(a, b, b)")
        print("foi lançada a exceção ErroPontosColineares.")
        print("A execução foi interrompida. plano2 não ficou definida.")

    # teste a __repr__
    # a normal tem que apontar no sentido do eixo dos z’s
    # e tem que ter comprimento 1
    print(plano1)

    # testes a interceta_triangulo
    p1 = Ponto3D(1.0, 1.0, 10.0)
    p2 = Ponto3D(1.0, 1.0, 5.0)
    r1 = Reta(p1, p2)
    trio = plano1.interceta_triangulo(r1)
    if trio[0] == True:
        print("r1 interceta plano1.")
        print("interceção = " + str(trio[1]))
        print("parâmetro t = " + str(trio[2]))
        print("interceção calculada com a equação da reta e t.")
        print("(tem que dar o mesmo que trio[1])")
        t = trio[2]
        # pi = r1.get_origem() + (r1.get_vetor_diretor() * t)
        pi = r1.origem + (r1.vetor_diretor * t)
        print(pi)
    else:
        print("r1 NÃO interceta plano1.")
    p3 = Ponto3D(2.0, 2.0, 10.0)
    r2 = Reta(p1, p3)
    trio = plano1.interceta_triangulo(r2)
    if trio[0] == True:
        print("r2 interceta plano1.")
        print("interceção = " + str(trio[1]))
        print("parâmetro t = " + str(trio[2]))
    else:
        print("r2 NÃO interceta plano1.")
