class Matriz:

    def __init__(self,numero_linhas,numero_colunas):

        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        self.linhas = []

        for n in range(numero_linhas):
            nova_linha = []
            for m in range(numero_colunas):
                nova_linha.append(0.0)
            self.linhas.append(nova_linha)

    def __repr__(self):

        #impressão de matrizes com sinal e floating point até <10
        resultado = "Matriz(" + str(self.numero_linhas) + ", " \
                    + str(self.numero_colunas) + ")\n"

        for n in range(self.numero_linhas):
            for m in range(self.numero_colunas):
                resultado = resultado + "| " + '{:^5}'.format(self.linhas[n][m]) + " "
            resultado = resultado + "|" + "\n"
        return resultado

    def set_entrada(self, n, m, valor):

        self.linhas[n-1][m-1] = valor

    def get_entrada(self, n, m):

        return self.linhas[n-1][m-1]

    def adiciona(self, outra_matriz):

        #falta dar erro em caso de dimensões diferentes
        matrizResultado = Matriz(self.numero_linhas, self.numero_colunas)
        for n in range(self.numero_linhas):
            for m in range(self.numero_colunas):
                matrizResultado.linhas[n][m] = self.linhas[n][m] + outra_matriz.linhas[n][m]
        return matrizResultado

    def __add__(self, outra_matriz):

        return self.adiciona(outra_matriz)

    def multiplica(self, outra_matriz):

        nlinhas = self.numero_linhas
        ncolunas = outra_matriz.numero_colunas
        resultado = Matriz(self.numero_linhas, outra_matriz.numero_colunas)
        for linha in range(nlinhas):
            for coluna in range(ncolunas):
                soma=0.0
                for k in range(self.numero_colunas):
                    soma = soma + self.linhas[linha][k] \
                           * outra_matriz.linhas[k][coluna]
                resultado.linhas[linha][coluna] = soma
        return resultado

    def multiplica_escalar(self, escalar):

        nlinhas = self.numero_linhas
        ncolunas = self.numero_colunas
        resultado = Matriz(nlinhas, ncolunas)
        for linha in range(nlinhas):
            for coluna in range(ncolunas):
                aux = self.linhas[linha][coluna] * escalar
                resultado.linhas[linha][coluna] = aux
        return resultado

    def __mul__(self, valor):

        if isinstance(valor, Matriz):
            return self.multiplica(valor)
        else:
            return self.multiplica_escalar(valor)

    def det_2x2(self):

        a = self.linhas[0][0]
        b = self.linhas[0][1]
        c = self.linhas[1][0]
        d = self.linhas[1][1]

        return a*d - b*c

    def det_3x3(self):

        a = self.linhas[0][0]
        b = self.linhas[0][1]
        c = self.linhas[0][2]
        d = self.linhas[1][0]
        e = self.linhas[1][1]
        f = self.linhas[1][2]
        g = self.linhas[2][0]
        h = self.linhas[2][1]
        i = self.linhas[2][2]

        return a*e*i + b*f*g + c*d*h - g*e*c - h*f*a - i*d*b

    def sub_matriz(self, linha_a_remover, coluna_a_remover):

        nlinhas = self.numero_linhas-1
        ncolunas = self.numero_colunas-1
        resultado = Matriz(nlinhas, ncolunas)
        for linha in range(nlinhas):
            for coluna in range(ncolunas):
                linha_self = linha
                coluna_self = coluna
                if linha >= linha_a_remover - 1 :
                    linha_self = linha_self + 1
                if coluna >= coluna_a_remover -1 :
                    coluna_self = coluna_self + 1
                resultado.linhas[linha][coluna] = self.linhas[linha_self][coluna_self]

        return resultado

    def det(self):

        if self.numero_linhas == 1:
            return self.linhas[0][0]
        elif self.numero_linhas == 2:
            return self.det_2x2()
        elif self.numero_linhas == 3:
            return self.det_3x3()
        else:
            soma = 0.0
            for j in range(self.numero_linhas):
                soma = soma + (-1.0)**(1+j+1) \
                       * self.linhas[0][j] \
                       * self.sub_matriz(1,j+1).det()
        return soma

    def transposta(self):

        nova_matriz = Matriz(self.numero_colunas, self.numero_linhas)
        for i in range(nova_matriz.numero_linhas):
            for j in range(nova_matriz.numero_colunas):
                nova_matriz.linhas[j][i] = self.linhas[i][j]

    def copia(self):

        nova_matriz = Matriz(self.numero_linhas, self.numero_colunas)
        for i in range(nova_matriz.numero_linhas):
            for j in range(nova_matriz.numero_colunas):
                nova_matriz.linhas[j][i] = self.linhas[j][i]

    def set_linha(self, nlinhas, uma_lista):

        for n in range(self.numero_linhas):
            self.linhas[nlinhas-1][n] = uma_lista[n]


    def set_coluna(self, ncolunas, uma_lista):

        for n in range(self.numero_linhas):
            self.linhas[n][ncolunas-1] = uma_lista[n]


if __name__ == "__main__":

    # teste ao construtor 
    print("#Teste ao construtor")
    m1 = Matriz(3, 4)

    # teste a __repr__ 
    print(m1)

    # teste a set_entrada 
    m1.set_entrada(1, 2, 1.0)
    m1.set_entrada(2, 2, 2.0)
    m1.set_entrada(3, 2, 3.0)
    m1.set_entrada(3, 4, 10.0)
    print(m1)

    # teste a get_entrada 
    print("m1 entrada 3,1 = ")
    print(m1.get_entrada(3, 1))
    print("m1 entrada 3,2 = ")
    print(m1.get_entrada(3, 2))
    print("m1 entrada 3,4 = ")
    print(m1.get_entrada(3, 4))

    # teste a adiciona 
    m2 = m1.adiciona(m1)
    print(m2)

    # teste a + 
    m3 = m1 + m1
    print(m3)

    # teste a multiplica
    m4 = Matriz(4, 3)
    m4.set_entrada(2, 1, 1.0)
    m4.set_entrada(2, 2, 2.0)
    m4.set_entrada(2, 3, 3.0)
    print(m4)
    m5 = m1.multiplica(m4)
    print(m5)

    # teste a multiplica_escalar
    m5a = m5.multiplica_escalar(-1.0)
    print(m5a)

    # teste a *
    m6 = m1 * m4
    print(m6)
    m6a = m1 * 2.0
    print(m6a)

    # teste a det_2x2
    m7 = Matriz(2, 2)
    m7.set_entrada(1, 1, 1.0)
    m7.set_entrada(1, 2, 2.0)
    m7.set_entrada(2, 1, 3.0)
    m7.set_entrada(2, 2, 4.0)
    print(m7)
    print("det(m7) = " + str(m7.det_2x2()))

    # teste a det_3x3
    print(m6)
    print("det(m6) = " + str(m6.det_3x3()))

    dir(m6)

    # teste a sub_matriz 
    m8 = m6.sub_matriz(2, 2)
    print(m8)

    # testes a det 
    print(m7.det())
    print(m6.det())
    m9 = Matriz(5, 5)
    m9.set_entrada(1, 1, 2.0)
    m9.set_entrada(2, 2, 2.0)
    m9.set_entrada(3, 3, 2.0)
    m9.set_entrada(4, 4, 2.0)
    m9.set_entrada(5, 5, 2.0)
    print(m9)
    print(m9.det())
