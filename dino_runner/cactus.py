import arcade
import random

class Cactus(arcade.Sprite):
    """
    Clase que representa un Cactus en el juego, actuando como un obstáculo para el Dinosaurio.

    Atributos:
    ----------
    center_x : float
        Establece la posición inicial del cactus en el eje X (generalmente al borde derecho de la pantalla).
    center_y : float
        Establece la posición inicial del cactus en el eje Y (en el suelo).

    Métodos:
    --------
    update() -> None:
        Actualiza la posición del cactus, moviéndolo hacia la izquierda para simular el avance del juego.
    reset_position(screen_width: float) -> None:
        Resetea la posición del cactus al borde derecho de la pantalla cuando sale del lado izquierdo.
    """

    def __init__(self, image_path, scale=0.5, speed=5):
        """
        Inicializa un objeto de la clase Cactus.

        Parámetros:
        -----------
        image_path : str
            Ruta a una imagen para el sprite del cactus.
        scale : float, opcional
            Factor de escala para el sprite del cactus.
        speed : float, opcional
            Velocidad horizontal con la que se mueve el cactus hacia la izquierda.
        """
        super().__init__(image_path, scale)
        self.center_x = 0  # Se actualizará cuando se añada al juego
        self.center_y = 0  # Se actualizará cuando se añada al juego
        self.change_x = -speed

    def update(self):
        """
        Actualiza la posición del cactus.
        
        Mueve el cactus hacia la izquierda para simular el avance del juego.
        Si el cactus sale del lado izquierdo de la pantalla, se resetea su posición.
        """
        super().update()
        if self.right < 0:
            screen_width = arcade.get_window().width
            self.reset_position(screen_width)

    def reset_position(self, screen_width):
        """
        Resetea la posición del cactus.

        Posiciona el cactus al borde derecho de la pantalla cuando sale del lado izquierdo.
        
        Parámetros:
        -----------
        screen_width : float
            Ancho de la pantalla del juego.
        """
        self.center_x = screen_width + random.randint(0, 50)
