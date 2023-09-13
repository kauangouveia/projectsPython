from future.types import no

class no:
    def __init__(self, nome:str):
        self.__nome__:str = nome
        self.__cor__:str = "branco"
        self.__custo__:float = 0
        self.__anterior__:no =  None
        self.__adjacente__:list =None
        
    def get_nome(self):
        return self.__nome__
        
    def get_cor(self):
        return self.__cor__
        
    def get_custo(self):
        return self.__custo__
        
    def get_anterior(self):
        return self.__anterior__
        
    def get_adjacente(self):
        return self.__adjacente__
        
        
    def set_nome(self, nome:str):
        self.__nome__ = nome

    def set_cor(self, cor:str):
        self.__cor__ = cor
        
    def set_custo(self, custo:float):
        self.__custo__ = custo
        
    def set_anterior(self, anterior:str):
        self.__anterior__ = anterior
        
    def set_adjacente(self, adjacente:str):
        self.__adjacente__ = adjacente
        
        