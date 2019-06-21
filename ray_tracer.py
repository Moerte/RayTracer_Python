from cor_rgb  import CorRGB
from imagem import Imagem
from matriz import Matriz
from vetor import Vetor3D
from ponto import Ponto3D
from luz import LuzPontual
from cor_phong import CorPhong
from reta import Reta
from plano import Plano
from face import FaceTriangular
from camara import Camara


class RayTracer:

    def __init__(self, lista_faces, lista_luzes, camara, cor_fundo):
        self.lista_faces = lista_faces
        self.lista_luzes = lista_luzes
        self.camara = camara
        self.cor_fundo = cor_fundo

    def __repr__(self):

        resultado = 'RayTracer('
        for face in self.lista_faces:
            resultado += str(face) + ',\n '
        for luz in self.lista_luzes:
            resultado += str(luz) + ',\n '
        resultado += str(self.camara) + ',\n ' + str(self.cor_fundo) + ')'

        return resultado

    def get_face_intercetada_mais_proxima(self, raio):

        intercecao = None
        indice = None
        for k in range(len(self.lista_faces)):
            face = self.lista_faces[k]
            resultado = face.interceta_triangulo(raio)
            if resultado[0]:
                if intercecao == None:
                    intercecao = resultado
                    indice = k
                else:
                    if resultado[2] < intercecao[2]:
                        intercecao = resultado
                        indice = k
        if intercecao == None:
            return [False, None, None, None]
        else:
            return [True, intercecao[1], intercecao[2], self.lista_faces[indice]]


    def get_cor_face(self, face, ponto_intercecao, direcao_olho):

        corPhong = face.get_cor_phong()
        #primeira luz
        luz = self.lista_luzes[0]
        posicao_luz = luz.get_posicao()
        raio = Reta(ponto_intercecao, posicao_luz)
        (interceta, ponto_intercecao2, t2, face2) = self.get_face_intercetada_mais_proxima(raio)
        if interceta:
            if t2 > (posicao_luz - ponto_intercecao).comprimento():
                interceta = False
        if interceta:
            cor = corPhong.get_cor_rgb(luz, None, None, None, True)
        else:
            direcao_luz = raio.vetor_diretor
            direcao_normal = face.normal
            cor = corPhong.get_cor_rgb(luz, direcao_luz, direcao_normal, direcao_olho, False)
        cor_resultado = cor
        #Outras Luzes
        for k in range(len(self.lista_luzes) - 1):
            luz = self.lista_luzes[k + 1]
            posicao_luz = luz.get_posicao()
            raio = Reta(ponto_intercecao, posicao_luz)
            (interceta, ponto_intercecao2, t2, face2) = self.get_face_intercetada_mais_proxima(raio)
            if interceta:
                if t2 > (posicao_luz - ponto_intercecao).comprimento():
                    interceta = False
            if interceta:
                cor = corPhong.get_cor_rgb(luz, None, None, None, True)
            else:
                direcao_luz = raio.vetor_diretor
                direcao_normal = face.normal
                cor = corPhong.get_cor_rgb(luz, direcao_luz, direcao_normal, direcao_olho, False)
            cor_resultado = cor_resultado + cor

        return cor_resultado



    def get_cor_vista_por_raio(self, raio):

        [interceta, ponto_intercecao, t, face] = self.get_face_intercetada_mais_proxima(raio)
        if interceta:
            direcao_olho = raio.vetor_diretor * (-1.0)
            cor = self.get_cor_face(face, ponto_intercecao, direcao_olho)
            return cor
        else:
            return self.cor_fundo

    def renderiza(self):
        camara = self.camara
        linha_max = camara.get_resolucao_vertical()
        coluna_max = camara.get_resolucao_horizontal()
        imagem = Imagem(linha_max, coluna_max)
        posicao_camara = camara.get_posicao()
        for i in range(linha_max):
            print('linha = ' +str(i + 1) + ' de ' + str(linha_max))
            for j in range(coluna_max):
                pixel = camara.get_pixel_global(i + 1, j + 1)
                recta = Reta(posicao_camara, pixel)
                cor = self.get_cor_vista_por_raio(recta)
                imagem.set_cor(i + 1, j + 1, cor)

        return imagem


if __name__ == "__main__":
    # teste ao construtor

    vermelho = CorRGB(1.0, 0.0, 0.0)
    branco = CorRGB(1.0, 1.0, 1.0)
    preto = CorRGB(0.0, 0.0, 0.0)
    cinzento = CorRGB(0.25, 0.25, 0.25)
    brilho = 100.0
    cor_letras = CorPhong(vermelho * 0.1, vermelho * 0.75, vermelho * 0.5, brilho)
    cor_box = CorPhong(cinzento, cinzento, cinzento, brilho)
    # letra M - triângulo 1
    m1_v1 = Ponto3D(2.25, 0.0, 0.0)
    m1_v2 = Ponto3D(3.25, 0.0, 0.0)
    m1_v3 = Ponto3D(3.25, 3.0, 0.0)
    m1 = FaceTriangular(m1_v1, m1_v2, m1_v3, cor_letras)
    # letra M - triângulo 2
    m2_v1 = Ponto3D(3.75, 1.0, 0.0)
    m2_v2 = Ponto3D(4.25, 3.0, 0.0)
    m2_v3 = Ponto3D(3.25, 3.0, 0.0)
    m2 = FaceTriangular(m2_v1, m2_v2, m2_v3, cor_letras)
    # letra M - triângulo 3
    m3_v1 = Ponto3D(4.25, 0.0, 0.0)
    m3_v2 = Ponto3D(5.25, 0.0, 0.0)
    m3_v3 = Ponto3D(4.25, 3.0, 0.0)
    m3 = FaceTriangular(m3_v1, m3_v2, m3_v3, cor_letras)
    # caixa cubo
    lado = 20.0
    largura = 20.0
    altura = 20.0
    profundidade = 5.0
    box_fundo_cima_v1 = Ponto3D(-largura / 2, altura / 2, -profundidade / 2)
    box_fundo_cima_v2 = Ponto3D(-largura / 2, -altura / 2, -profundidade / 2)
    box_fundo_cima_v3 = Ponto3D(largura / 2, altura / 2, -profundidade / 2)
    box_fundo_cima = FaceTriangular(box_fundo_cima_v1,
                                    box_fundo_cima_v2,
                                    box_fundo_cima_v3, cor_box)
    box_fundo_baixo_v1 = Ponto3D(-largura / 2, -altura / 2, -profundidade / 2)
    box_fundo_baixo_v2 = Ponto3D(largura / 2, -altura / 2, -profundidade / 2)
    box_fundo_baixo_v3 = Ponto3D(largura / 2, altura / 2, -profundidade / 2)
    box_fundo_baixo = FaceTriangular(box_fundo_baixo_v1,
                                     box_fundo_baixo_v2,
                                     box_fundo_baixo_v3, cor_box)
    box_esquerda_cima_v1 = Ponto3D(-largura / 2, altura / 2, profundidade / 2)
    box_esquerda_cima_v2 = Ponto3D(-largura / 2, -altura / 2, profundidade / 2)
    box_esquerda_cima_v3 = Ponto3D(-largura / 2, altura / 2, -profundidade / 2)
    box_esquerda_cima = FaceTriangular(box_esquerda_cima_v1,
                                       box_esquerda_cima_v2,
                                       box_esquerda_cima_v3, cor_box)
    box_esquerda_baixo_v1 = Ponto3D(-largura / 2, -altura / 2, profundidade / 2)
    box_esquerda_baixo_v2 = Ponto3D(-largura / 2, -altura / 2, -profundidade / 2)
    box_esquerda_baixo_v3 = Ponto3D(-largura / 2, +altura / 2, -profundidade / 2)
    box_esquerda_baixo = FaceTriangular(box_esquerda_baixo_v1,
                                        box_esquerda_baixo_v2,
                                        box_esquerda_baixo_v3, cor_box)
    box_chao_esquerda_v1 = Ponto3D(-largura / 2, -altura / 2, profundidade / 2)
    box_chao_esquerda_v2 = Ponto3D(largura / 2, -altura / 2, -profundidade / 2)
    box_chao_esquerda_v3 = Ponto3D(-largura / 2, -altura / 2, -profundidade / 2)
    box_chao_esquerda = FaceTriangular(box_chao_esquerda_v1,
                                       box_chao_esquerda_v2,
                                       box_chao_esquerda_v3, cor_box)
    box_chao_direita_v1 = Ponto3D(-largura / 2, -altura / 2, profundidade / 2)
    box_chao_direita_v2 = Ponto3D(largura / 2, -altura / 2, profundidade / 2)
    box_chao_direita_v3 = Ponto3D(largura / 2, -altura / 2, -profundidade / 2)
    box_chao_direita = FaceTriangular(box_chao_direita_v1,
                                      box_chao_direita_v2,
                                      box_chao_direita_v3, cor_box)
    box_direita_cima_v1 = Ponto3D(largura / 2, altura / 2, profundidade / 2)
    box_direita_cima_v2 = Ponto3D(largura / 2, altura / 2, -profundidade / 2)
    box_direita_cima_v3 = Ponto3D(largura / 2, -altura / 2, -profundidade / 2)
    box_direita_cima = FaceTriangular(box_direita_cima_v1,
                                      box_direita_cima_v2,
                                      box_direita_cima_v3, cor_box)
    box_direita_baixo_v1 = Ponto3D(largura / 2, -altura / 2, profundidade / 2)
    box_direita_baixo_v2 = Ponto3D(largura / 2, altura / 2, profundidade / 2)
    box_direita_baixo_v3 = Ponto3D(largura / 2, -altura / 2, -profundidade / 2)
    box_direita_baixo = FaceTriangular(box_direita_baixo_v1,
                                       box_direita_baixo_v2,
                                       box_direita_baixo_v3, cor_box)
    lista_faces = [m1, m2, m3, box_fundo_cima, box_fundo_baixo, box_esquerda_cima,
                   box_esquerda_baixo, box_chao_esquerda, box_chao_direita,
                   box_direita_cima, box_direita_baixo]
    # lista de luzes
    luz1_posicao = Ponto3D(-8.0, 5.0, 5.0)
    luz2_posicao = Ponto3D(8.0, 5.0, 1.0)
    luz1 = LuzPontual(luz1_posicao, branco, branco, branco)
    luz2 = LuzPontual(luz2_posicao, branco, branco, branco)
    lista_luzes = [luz1, luz2]
    # a câmara
    camara_posicao = Ponto3D(0.0, 0.0, 10.0)
    camara_posicao = Ponto3D(0.0, 0.0, 5.0)
    camara_olhar_para = Ponto3D(0.0, 0.0, 0.0)
    camara_vertical = Vetor3D(0.0, 1.0, 0.0)
    camara_distancia_olho_plano_projecao = 5.0
    camara_largura_retangulo_projecao = 10.0
    camara_altura_retangulo_projecao = 8.0
    camara_largura_retangulo_projecao = 20.0
    camara_altura_retangulo_projecao = 16.0
    #camara_resolucao_horizontal = 320
    #camara_resolucao_vertical = 240
    camara_resolucao_horizontal = 100
    camara_resolucao_vertical = 80
    camara = Camara(camara_posicao,
                    camara_olhar_para,
                    camara_vertical,
                    camara_distancia_olho_plano_projecao,
                    camara_largura_retangulo_projecao,
                    camara_altura_retangulo_projecao,
                    camara_resolucao_horizontal,
                    camara_resolucao_vertical)
    cor_fundo = preto
    ray_tracer = RayTracer(lista_faces, lista_luzes, camara, cor_fundo)
    # teste a __repr__
    print(ray_tracer)

    # teste a renderiza
    imagem = ray_tracer.renderiza()
    imagem.guardar_como_ppm("teste_ao_RayTracer.ppm")