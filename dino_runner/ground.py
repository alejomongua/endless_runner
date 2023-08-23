import arcade

class Suelo(arcade.Sprite):
    """
    Clase que representa el suelo del juego.

    Atributos:
    ----------
    center_x : float
        Posición central del sprite en el eje X.
    center_y : float
        Posición central del sprite en el eje Y.

    Métodos:
    --------
    update() -> None:
        Actualiza la posición del suelo, moviéndolo hacia la izquierda para simular el avance del juego.
    """

    def __init__(self, image_path, scale=1.0, speed=5):
        """
        Inicializa un objeto de la clase Suelo.

        Parámetros:
        -----------
        image_path : str
            Ruta a una imagen para el sprite del suelo.
        scale : float, opcional
            Factor de escala para el sprite del suelo.
        speed : float, opcional
            Velocidad horizontal con la que se mueve el suelo hacia la izquierda.
        """
        super().__init__(image_path, scale)
        self.change_x = -speed

    def update(self):
        """
        Actualiza la posición del suelo.
        
        Mueve el suelo hacia la izquierda para simular el avance del juego.
        Si una parte del suelo sale completamente del lado izquierdo de la pantalla, 
        se ajusta su posición para crear la ilusión de un suelo infinito.
        """
        super().update()
        if self.right < 0:
            self.center_x += self.width
