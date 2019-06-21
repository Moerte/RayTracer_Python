
from cor_rgb    import CorRGB
from imagem     import Imagem
from matriz     import Matriz
from vetor      import Vetor3D
from ponto      import Ponto3D
from luz        import LuzPontual
from cor_phong  import CorPhong
from reta       import Reta
from plano      import Plano
from face       import FaceTriangular
from camara   import Camara
from ray_tracer import RayTracer
from tranformacao import Transformacao
# teste ao construtor

#translacao = Transformacao()
#translacao.translacao(Vetor3D(-2, -4, 0))
#escalamento = Transformacao()
#escalamento.escalamento(1, 2, 1)
#shearing = Transformacao()
#shearing.shearing( 2, 1.5, 0, 0, 0, 0)
rotX = Transformacao()
rotX.rotacao_x(-1)
#rotY = Transformacao()
#rotY.rotacao_y(-0.5)
#rotZ = Transformacao()
#rotZ.rotacao_z(2)

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

# transformações
#Translação
#m1 = translacao.transforma_face_triangular(m1)
#m2 = translacao.transforma_face_triangular(m2)
#m3 = translacao.transforma_face_triangular(m3)
#m1 = escalamento.transforma_face_triangular(m1)
#m2 = escalamento.transforma_face_triangular(m2)
#m3 = escalamento.transforma_face_triangular(m3)
#m1 = shearing.transforma_face_triangular(m1)
#m2 = shearing.transforma_face_triangular(m2)
#m3 = shearing.transforma_face_triangular(m3)
m1 = rotX.transforma_face_triangular(m1)
m2 = rotX.transforma_face_triangular(m2)
m3 = rotX.transforma_face_triangular(m3)
#m1 = rotY.transforma_face_triangular(m1)
#m2 = rotY.transforma_face_triangular(m2)
#m3 = rotY.transforma_face_triangular(m3)
#m1 = rotZ.transforma_face_triangular(m1)
#m2 = rotZ.transforma_face_triangular(m2)
#m3 = rotZ.transforma_face_triangular(m3)

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
camara_resolucao_horizontal = 320
camara_resolucao_vertical = 240
#camara_resolucao_horizontal = 120
#camara_resolucao_vertical = 80
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
imagem = ray_tracer.renderiza()
#imagem.guardar_como_ppm("projeto_imagem_1.ppm")
#imagem.guardar_como_ppm("projeto_imagem_2.ppm")
#imagem.guardar_como_ppm("projeto_imagem_3.ppm")
#imagem.guardar_como_ppm("projeto_imagem_4.ppm")
#imagem.guardar_como_ppm("projeto_imagem_5.ppm")
#imagem.guardar_como_ppm("projeto_imagem_6.ppm")
imagem.guardar_como_ppm("projeto_imagem_7.ppm")
