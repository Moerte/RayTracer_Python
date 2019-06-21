from colorsys import hsv_to_rgb

class CorRGB:

    def __init__ (self, red, green, blue):
        
        #if red > 1.0: 
            #self.r = 1.0 etc
            
        self.r = max(0.0, min(1.0, red))
        self.g = max(0.0, min(1.0, green))
        self.b = max(0.0, min(1.0, blue))        
    
    def __repr__ (self):
        
        rint = int(self.r * 255.0)
        gint = int(self.g * 255.0)
        bint = int(self.b * 255.0)
        
        return str(rint) + " " + str(gint) + " " + str(bint)
        
    def soma (self, outra_cor):
        
        novo_r = self.r + outra_cor.r
        novo_g = self.g + outra_cor.g
        novo_b = self.b + outra_cor.b
        
        nova_cor = CorRGB(novo_r, novo_g, novo_b)
        
        return nova_cor
        
    def __add__ (self, outra_cor):
         
         return self.soma(outra_cor)
         
    def set_hsv(self, hue, saturation, value):
        
        (r, g, b) = hsv_to_rgb(hue/360.0, saturation, value)
        
        self.r = r
        self.g = g
        self.b = b
        
        return self
        
    def multiplica (self, outra_cor):
        
        novo_r = self.r * outra_cor.r
        novo_g = self.g * outra_cor.g
        novo_b = self.b * outra_cor.b
        
        nova_cor = CorRGB(novo_r, novo_g, novo_b)
        
        return nova_cor 
    
    def multiplica_escalar (self, escalar):
        
        novo_r = self.r * escalar
        novo_g = self.g * escalar
        novo_b = self.b * escalar
        
        nova_cor = CorRGB(novo_r, novo_g, novo_b)
        
        return nova_cor 
        
    def __mul__ (self, valor):
         
         if isinstance(valor, float):
             return self.multiplica_escalar(valor)
         else:
             return self.multiplica(valor)
  
if __name__ == "__main__":   
    
    #Testes ao construtor
    c1 = CorRGB(1.0, 0.0, 0.0) #RED
    c2 = CorRGB(0.0, 1.0, 0.0) #GREEN
    c3 = CorRGB(0.0, 0.0, 1.0) #BLUE
    c4 = CorRGB(1.0, 1.0, 1.0) #BLACK
    c5 = CorRGB(0.0, 0.0, 0.0) #WHITE     
    
    print("Com a função soma:")
    c6 = c1.soma(c2)
    c7 = c1.soma(c4) # = CorRGB.soma(c1, c3)
    print(c6)
    print(c7)
    print(" ")
    
    print("Com o operador + :")
    c6 = c1 + c2
    c7 = c1 + c4
    print(c6)
    print(c7)
    print(" ")
    
    print("Transformação hsv:")
    c1.set_hsv(360.0, 1.0, 1.0)
    print(c1)
    print(" ")
    
    print("Com o operador * :")
    c1 = CorRGB(1.0, 1.0, 1.0)
    c2 = CorRGB(0.0, 0.5, 1.0)
    e1 = 0.5
    c3 = c1 * c2
    c4 = c1 * e1
    print(c3)
    print(c4)

