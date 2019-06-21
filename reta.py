
from ponto import Ponto3D

ERRO_ARREND = 10.0**(-10)

class ErroPontosCoincidentes(Exception):
    """Classe exceção de erro """
    pass

class Reta:
    
    def __init__(self, origem, destino):
        
        self.origem = origem
        self.destino = destino
        vetor = destino - origem
        norma = vetor.comprimento()
        if norma < ERRO_ARREND:
            raise ErroPontosCoincidentes
        self.vetor_diretor = vetor.versor()
    
    def __repr__(self):
        
        return "Reta[ " + str(self.origem) + ", " \
                      + str(self.destino) + ", " \
                      + str(self.vetor_diretor) + " ]"
    
    def get_origem(self):
        
        return self.origem
    
    def get_destino(self):
        
        return self.destino
    
    def get_vetor_diretor(self):
        
        return self.vetor_diretor


if __name__== "__main__":
    
    # teste ao construtor
    p1 = Ponto3D(0.0, 0.0, 0.0)
    p2 = Ponto3D(1.0, 2.0, 3.0)
    r1 = Reta(p1, p2)
    print("Até aqui não foram lançadas exceções.")
    
    # teste à exceção ErroPontosCoincidentes
    try:
        r2 = Reta(p2, p2)
    except ErroPontosCoincidentes:
        print("Ao tentar definir-se a reta r2 = Reta(p2, p2)")
        print("foi lançada a exceção ErroPontosCoincidentes.")
        print("A execução foi interrompida. r2 não ficou definida.")
    
    #Erro propositado r3 = Reta(p1, p1)
    
#ALT + 3 ----------< COMENTAR
#ALT + 4 ----------< DESCOMENTAR

    # teste a __repr__
    print(r1)

    # teste a get_origem
    print(r1.get_origem())

    # teste a get_vetor_diretor
    print(r1.get_vetor_diretor())
