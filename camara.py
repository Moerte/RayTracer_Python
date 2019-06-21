from matriz import Matriz
from vetor import Vetor3D
from ponto import Ponto3D


class Camara:
    
    def __init__(self, posicao, olhar_para, 
                 vertical, distancia_olho_plano_projecao, 
                 largura_retangulo_projecao, altura_retangulo_projecao, 
                 resolucao_horizontal, resolucao_vertical):
        
        self.posicao = posicao
        self.olhar_para = olhar_para
        self.vertical = vertical
        self.distancia_olho_plano_projecao = distancia_olho_plano_projecao
        self.largura_retangulo_projecao = largura_retangulo_projecao
        self.altura_retangulo_projecao = altura_retangulo_projecao
        self.resolucao_horizontal = resolucao_horizontal
        self.resolucao_vertical = resolucao_vertical
        
        # eixo_z É o eixo dos z’s do sistema de coordenadas da câmara. É o
        # vetor com comprimento 1 que aponta do olho para olhar_para. É
        # dado por:
        eixo_z = (olhar_para - posicao).versor()
        
        # eixo_y é o eixo dos y’s do sistema de coordenadas da câmara. é a
        # componente com comprimento 1 do vetor vertical ortogonal ao eixo
        # dos z’s. é dado pelo vetor vertical subtraído da sua projeção sobre o
        # eixo dos z’s, isto é:
        eixo_y = (vertical + eixo_z * (-1.0 * vertical.interno(eixo_z))).versor() 
        
        # eixo_x É o eixo dos x’s do sistema de coordenadas da câmara. É
        # ortogonal a eixo_y e eixo_z. Quando estamos na posição da câmara,
        # a olhar segundo o eixo dos z’s usando como vertical o eixo dos y’s, o
        # eixo dos x’s aponta para a direita. Segundo a regra da mão direita, é
        # dado por
        eixo_x = eixo_z.externo(eixo_y)
        
        self.eixo_x = eixo_x
        self.eixo_y = eixo_y
        self.eixo_z = eixo_z
        
        # incremento_horizontal É a distância horizontal entre pixels. É dado por
        incremento_horizontal = largura_retangulo_projecao / resolucao_horizontal
        
        # incremento_vertical É a distância vertical entre pixels. É dado por
        incremento_vertical = altura_retangulo_projecao / resolucao_vertical
        
        self.incremento_horizontal = incremento_horizontal
        self.incremento_vertical = incremento_vertical
        
        # canto_superior_esquerdo_x Usando a mesma orientação que foi descrita
        # no eixo dos x’s, é a coordenada x do pixel do canto superior
        # esquerdo, do plano de projeção. É dado por
        canto_superior_esquerdo_x = (-largura_retangulo_projecao / 2.0) + (incremento_horizontal / 2.0)
        
        # canto_superior_esquerdo_y Usando a mesma orientação que foi descrita
        # no eixo dos x’s, é a coordenada y do pixel do canto superior
        # esquerdo, do plano de projeção. É dado por
        canto_superior_esquerdo_y = (altura_retangulo_projecao / 2.0) - (incremento_vertical / 2.0)
        
        # canto_superior_esquerdo_z Usando a mesma orientação que foi descrita
        # no eixo dos x’s, é a coordenada z do pixel do canto superior
        # esquerdo, do plano de projeção. É dado por
        canto_superior_esquerdo_z = distancia_olho_plano_projecao
        
        self.canto_superior_esquerdo_x = canto_superior_esquerdo_x
        self.canto_superior_esquerdo_y = canto_superior_esquerdo_y
        self.canto_superior_esquerdo_z = canto_superior_esquerdo_z
        
        matriz = Matriz(4, 4)
        matriz.set_coluna(1, [eixo_x.get_x(), eixo_x.get_y(), eixo_x.get_z(), 0.0])
        matriz.set_coluna(2, [eixo_y.get_x(), eixo_y.get_y(), eixo_y.get_z(), 0.0])
        matriz.set_coluna(3, [eixo_z.get_x(), eixo_z.get_y(), eixo_z.get_z(), 0.0])
        matriz.set_coluna(4, [posicao.get_x(), posicao.get_y(), posicao.get_z(), 1.0])
        
        self.matriz = matriz
        
    def __repr__(self):
        
        return "Camara:\nposicao(" \
        + str(self.posicao) + "), olhar_para(" \
        + str(self.olhar_para) + "), vertical(" \
        + str(self.vertical) + "), dist_olho_plano_proj(" \
        + str(self.distancia_olho_plano_projecao) + "), largura_rect_proj(" \
        + str(self.largura_retangulo_projecao) + "), altura_rect_proj(" \
        + str(self.altura_retangulo_projecao) + "), res_h(" \
        + str(self.resolucao_horizontal) + "), res_v(" \
        + str(self.resolucao_vertical) + "), eixo_x(" \
        + str(self.eixo_x) + "), eixo_y(" \
        + str(self.eixo_y) + "), eixo_z(" \
        + str(self.eixo_z) + "), canto_superior_esquerdo(" \
        + str(self.canto_superior_esquerdo_x) + ", " \
        + str(self.canto_superior_esquerdo_y) + ", " \
        + str(self.canto_superior_esquerdo_z) + "), incremento_horizontal(" \
        + str(self.incremento_horizontal) + "), incremento_vertical(" \
        + str(self.incremento_vertical) + "), " + "\n" + "\n" \
        + str(self.matriz)
         
    def get_posicao(self):
        
        return self.posicao
    
    def get_resolucao_horizontal(self):
        
        return self.resolucao_horizontal
    
    def get_resolucao_vertical(self):
        
        return self.resolucao_vertical
    
    def get_pixel_local(self, linha, coluna):
        
        x = self.canto_superior_esquerdo_x + (coluna - 1) * self.incremento_horizontal
        y = self.canto_superior_esquerdo_y - (linha - 1) * self.incremento_vertical
        z = self.canto_superior_esquerdo_z
        
        return Ponto3D(x, y, z)
    
    def local_para_global(self, ponto):
        
        mcoluna = Matriz(4,1)
        mcoluna.set_entrada(1, 1, ponto.get_x())
        mcoluna.set_entrada(2, 1, ponto.get_y())
        mcoluna.set_entrada(3, 1, ponto.get_z())
        mcoluna.set_entrada(4, 1, 1.0)
        
        mresultado = self.matriz * mcoluna
        
        x = mresultado.get_entrada(1, 1)
        y = mresultado.get_entrada(2, 1)
        z = mresultado.get_entrada(3, 1)
        
        return Ponto3D(x, y, z)
    
    def get_pixel_global(self, linha, coluna):
        
        pixel_local = self.get_pixel_local(linha, coluna)
        pixel_global = self.local_para_global(pixel_local)
        return pixel_global
    
        
# Testes:   
if __name__ == "__main__":
    
    # teste ao construtor
    posicao = Ponto3D(0.0, 0.0, 3.0)
    olhar_para = Ponto3D(0.0, 0.0, 0.0)
    vertical = Vetor3D(0.0, 1.0, 0.0)
    distancia_olho_plano_projecao = 2.0
    largura_retangulo_projecao = 2.0
    altura_retangulo_projecao = 2.0
    resolucao_horizontal = 5
    resolucao_vertical = 5
    camara = Camara(posicao, olhar_para, vertical, distancia_olho_plano_projecao,
    largura_retangulo_projecao, altura_retangulo_projecao,
    resolucao_horizontal, resolucao_vertical)
    
    print("# teste a __repr__")
    print(camara)
    print()
    
    print("# teste a get_posicao")
    print(camara.get_posicao())
    print()
    
    print("# teste a get_resolucao_horizontal")
    print(camara.get_resolucao_horizontal())
    print()
    
    print("# teste a get_resolucao_vertical")
    print(camara.get_resolucao_vertical())
    print()
    
    print("# teste a get_pixel_local")
    print("sistema de coordenadas LOCAL")
    print("canto superior esquerdo (-x,y)= ")
    p1 = camara.get_pixel_local(1, 1)
    print(p1)
    print("canto superior direito (x,y)= ")
    p2 = camara.get_pixel_local(1, 5)
    print(p2)
    print("canto inferior esquerdo (-x,-y)= ")
    p3 = camara.get_pixel_local(5, 1)
    print(p3)
    print("canto inferior direito (x,-y)= ")
    p4 = camara.get_pixel_local(5, 5)
    print(p4)
    print()
    
    print("# teste a local_para_global")
    print("sistema de coordenadas GLOBAL")
    print("canto superior esquerdo = ")
    p1_global = camara.local_para_global(p1)
    print(p1)
    print(p1_global)
    print("canto superior direito = ")
    p2_global = camara.local_para_global(p2)
    print(p2_global)
    print("canto inferior esquerdo = ")
    p3_global = camara.local_para_global(p3)
    print(p3_global)
    print("canto inferioror direito = ")
    p4_global = camara.local_para_global(p4)
    print(p4_global)
    print()
    
    print("# teste a get_pixel_global")
    print("sistema de coordenadas GLOBAL")
    print("canto superior esquerdo = ")
    p5 = camara.get_pixel_global(1, 1)
    print(p5)
    print("canto superior direito = ")
    p6 = camara.get_pixel_global(1, 5)
    print(p6)
    print("canto inferior esquerdo = ")
    p7 = camara.get_pixel_global(5, 1)
    print(p7)
    print("canto inferioror direito = ")
    p8 = camara.get_pixel_global(5, 5)
    print(p8)