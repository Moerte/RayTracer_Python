from cor_rgb import CorRGB
from ponto import Ponto3D
from vetor import Vetor3D
from imagem import Imagem
from luz import LuzPontual

class CorPhong:
    
    def __init__(self, k_ambiente, k_difusa, k_especular, brilho):
        self.k_ambiente   = k_ambiente
        self.k_difusa     = k_difusa
        self.k_especular  = k_especular
        self.brilho       = brilho
        
    def __repr__(self):
        return "CorPhong(" + str(self.k_ambiente) + ", " \
                           + str(self.k_difusa) + ", " \
                           + str(self.k_difusa) + ", " \
                           + str(self.brilho) + ")"   
        
    def get_cor_rgb(self, luz, direcao_luz, normal, direcao_olho, sombra):

        cor_ambiente = luz.intensidade_ambiente * self.k_ambiente

        if(sombra):
            return cor_ambiente
        n_interno_l = normal.interno(direcao_luz)
        r = direcao_luz * (-1) + normal * 2 * n_interno_l
        if(n_interno_l < 0):
            return cor_ambiente
        cor_difusa = luz.intensidade_difusa * self.k_difusa * n_interno_l
        cor_especular = luz.intensidade_especular * self.k_especular * (direcao_olho.interno(r)) ** self.brilho

        return cor_ambiente + cor_difusa + cor_especular

        #componente ambiente
        
        # cor_ambiente = luz.get_intensidade_ambiente() \
        #             * self.k_ambiente
        #
        # if sombra == True:
        #     return cor_ambiente
        #
        # interno_N_L = normal.interno(direcao_luz)
        #
        # if interno_N_L < 0:
        #     return cor_ambiente
        #
        #  #component difusa
        #
        # cor_difusa = (luz.get_intensidade_difusa() \
        #             * self.k_difusa) * interno_N_L
        #
        # if sombra == True:
        #     return cor_ambiente
        #
        # interno_N_L = normal.interno(direcao_luz)
        #
        # if interno_N_L < 0:
        #     return cor_ambiente
        #
        # #componente especular
        #
        # r = direcao_luz * (-1.0) + (normal * (2.0 * interno_N_L))
        #
        # cor_especular = (luz.get_intensidade_especular() \
        #             * (self.k_especular) * (direcao_olho.interno(r))**self.brilho)
        #
        # cor = cor_ambiente + cor_difusa + cor_especular
        #
        # return cor
                         
if __name__ == "__main__":
   
    # teste ao construtor
    material_k_ambiente = CorRGB(0.0, 0.0, 0.1)
    material_k_difusa = CorRGB(0.0, 0.0, 0.9)
    material_k_especular = CorRGB(1.0, 1.0, 1.0)
    material_brilho = 100.0
    material_cor = CorPhong(material_k_ambiente,
                            material_k_difusa,
                            material_k_especular,
                            material_brilho)

    # teste a __repr__
    print(material_cor)
    
    # teste a get_cor_rgb
    luz_posicao = Ponto3D(1.0, 0.0, 1.0)
    luz_intensidade_ambiente = CorRGB(1.0, 1.0, 1.0)
    luz_intensidade_difusa = CorRGB(1.0, 1.0, 1.0)
    luz_intensidade_especular = CorRGB(1.0, 1.0, 1.0)
    luz = LuzPontual(luz_posicao, luz_intensidade_ambiente, luz_intensidade_difusa, luz_intensidade_especular)
    olho = Ponto3D(-1.0, 0.0, 1.0)
    n_pontos = 100
    imagem = Imagem(100, 100)
    incremento = 0.02 # 2.0/100.0
    normal = Vetor3D(0.0, 0.0, 1.0)
    sombra = False
    for m in range(100): # índice de linhas
        for n in range(100): # índice de colunas
                ponto = Ponto3D(-1.0 + n*incremento, 1.0 - m*incremento, 0)
                direcao_luz = (luz.get_posicao() - ponto).versor()
                direcao_olho = (olho - ponto).versor()
                cor = material_cor.get_cor_rgb(luz, direcao_luz, normal, direcao_olho, sombra)
                imagem.set_cor(m+1, n+1, cor)
   
    imagem.guardar_como_ppm("cor_phong.ppm")
    
    # teste adicional - parâmetros
    h = 60.0
    n_pontos = 120
    # teste adicional
    luz_posicao = Ponto3D(1.0, 0.0, 1.0)
    luz_i_ambiente = CorRGB(1.0, 1.0, 1.0)
    luz_i_difusa = CorRGB(1.0, 1.0, 1.0)
    luz_i_especular = CorRGB(1.0, 1.0, 1.0)
    luz = LuzPontual(luz_posicao, luz_i_ambiente, luz_i_difusa, luz_i_especular)
    olho = Ponto3D(-1.0, 0.0, 1.0)
    k_ambiente = CorRGB(0.0, 0.0, 0.0)
    k_difusa = CorRGB(0.0, 0.0, 0.0)
    k_especular = CorRGB(0.9, 0.9, 0.9)
    brilho = 100.0
    k_ambiente.set_hsv(h, 1.0, 0.1)
    k_difusa.set_hsv(h, 1.0, 0.8)
    cor_phong = CorPhong(k_ambiente,
                         k_difusa,
                         k_especular,
                         brilho)
    imagem = Imagem(n_pontos, n_pontos)
    incremento = 2.0 / n_pontos
    normal = Vetor3D(0.0, 0.0, 1.0)
    sombra = False
    for m in range(n_pontos): # índice de linhas
        for n in range(n_pontos): # índice de colunas
            ponto = Ponto3D(-1.0 + n*incremento, 1.0 - m*incremento, 0)
            direcao_luz = (luz.get_posicao() - ponto).versor()
            direcao_olho = (olho - ponto).versor()
            cor = cor_phong.get_cor_rgb(luz, direcao_luz, normal, direcao_olho, sombra)
            imagem.set_cor(m+1, n, cor)
    imagem.guardar_como_ppm("cor_phong_adicional.ppm")

