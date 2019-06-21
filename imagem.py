from cor_rgb import CorRGB
from io import StringIO

class Imagem:

    def __init__(self, numero_linhas, numero_colunas):

        self.numero_linhas = numero_linhas
        self.numero_colunas = numero_colunas
        self.linhas = []
        
        for n in range(numero_linhas):
            nova_linha = []
            for m in range(numero_colunas):
                nova_cor = CorRGB(0.0,0.0,0.0)
                nova_linha.append(nova_cor)
            self.linhas.append(nova_linha)
    
    def __repr__(self):

        resultado = StringIO()
        resultado.write("P3\n")
        resultado.write("#Imagem criada por MCG\n")
        resultado.write(str(self.numero_colunas))
        resultado.write(" ")
        resultado.write(str(self.numero_linhas) + "\n")
        resultado.write("255\n")
        
        for n in range(self.numero_linhas):

            for m in range(self.numero_colunas):
                resultado.write(str(self.linhas[n][m]) + " ")
            resultado.write("\n")
   
        return resultado.getvalue()
    
    def set_cor(self,linha,coluna,cor_rgb):

        self.linhas[linha-1][coluna-1] = cor_rgb
        return self
   
    def get_cor(self,linha,coluna):

        return self.linhas[linha-1][coluna-1]
    
    def guardar_como_ppm(self, nome_ficheiro):
        
        ficheiro = open(nome_ficheiro, "w")
        ficheiro.write(str(self))
        ficheiro.close()

if __name__ == "__main__":    
    print()
    print("teste ao construtor") 
    imagem1 = Imagem(5, 5)
    
    print()
    print("# teste a __repr__")
    imagem2 = Imagem(5, 5)
    print(imagem2)
    
    # teste a set_cor 
    imagem3 = Imagem(5, 5) 
    branco = CorRGB(1.0, 1.0, 1.0) 
    imagem3.set_cor(3, 3, branco) 
    print(imagem3)
    
    # testes a get_cor 
    imagem4 = Imagem(5, 5) 
    branco = CorRGB(1.0, 1.0, 1.0) 
    imagem4.set_cor(3, 3, branco) 
    print(imagem4.get_cor(3, 3)) 
    print(imagem4.get_cor(5, 5))
    
    # teste a guardar_como_ppm 
    imagem5 = Imagem(3, 5) 
    red = CorRGB(1.0, 0.0, 0.0) 
    green = CorRGB(0.0, 1.0, 0.0)
    blue = CorRGB(0.0, 0.0, 1.0)
    imagem5.set_cor(2, 2, red) 
    imagem5.set_cor(2, 3, green) 
    imagem5.set_cor(2, 4, blue) 
    imagem5.guardar_como_ppm("imagem5.ppm")
    
    imagem6 = Imagem(100, 100) 
    print(imagem6)