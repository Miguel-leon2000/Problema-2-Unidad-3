# Pruebas unitarias
"""
>>> Area = AreaTriangulo(3, 3, 60)
>>> Area.Convertir_Angulo_Radianes()
>>> Area.Calcular_Area()
>>> Area.getArea()
3.8971143170299736
"""

#Libreria math para calcular el valor exacto de pi y obtener el seno de un angulo en radianes.
import math

#Nombre de la clase
class AreaTriangulo:

    # Atributos de entrada y salida
    __lado1 = int(0)
    __lado2 = int(0)
    __angulo = int(0)
    __angulo_radianes = float(0)
    __area = float(0)

    # Metodo constructor para recibir los atributos de entrada.
    def __init__(self, lado1, lado2, angulo):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__angulo = angulo

    """
    Metodo para convertir el angulo a radianes mediante la formula 
    (Se utliza la libreria math para obtener el valor exacto de pi)
    """
    def Convertir_Angulo_Radianes(self):

        self.__angulo_radianes = (self.__angulo * math.pi)/180

    """
    Metodo para calcular el area del triangulo mediante la ley del seno
    Se hace uso de la libreria math para calcular el seno del angulo convertido en radianes
    """
    def Calcular_Area(self):

        self.__area = (1/2) * self.__lado1 * self.__lado2 * math.sin(self.__angulo_radianes)

    # Metodo get para obtener el valor del atributo "area"
    def getArea(self):
        return self.__area

#Manda ejecutar las pruebas automatizadas(Pruebas unitarias)
if __name__ == "__main__":
    import doctest
    doctest.testmod()
