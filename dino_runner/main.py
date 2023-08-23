import arcade
from dino_runner.dino import Dinosaurio
from dino_runner.cactus import Cactus
from dino_runner.ground import Suelo

from dino_runner.settings import SCREEN_WIDTH, SCREEN_HEIGHT

SCREEN_TITLE = "Dino Runner"
SPEED = 5

class DinoRunner(arcade.Window):
    """
    Clase principal del juego Dino Runner.

    Atributos:
    ----------
    dinosaurio : Dinosaurio
        Representa al personaje principal del juego.
    cacti : arcade.SpriteList
        Lista que contiene todos los cactus (obstáculos) en el juego.
    ground_list : arcade.SpriteList
        Lista que contiene las instancias del suelo.

    Métodos:
    --------
    setup() -> None:
        Inicializa el juego y crea los objetos iniciales.
    on_draw() -> None:
        Dibuja todos los elementos del juego en la pantalla.
    update(delta_time: float) -> None:
        Actualiza el estado del juego.
    on_key_press(key: int, modifiers: int) -> None:
        Maneja los eventos de teclado.
    """

    def __init__(self, width, height, title):
        """
        Inicializa la ventana del juego.

        Parámetros:
        -----------
        width : int
            Ancho de la ventana.
        height : int
            Alto de la ventana.
        title : str
            Título de la ventana.
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        # Inicializa los atributos
        self.dinosaurio = None
        self.cacti = None
        self.ground_list = None

    def setup(self):
        """Inicializa el juego y crea los objetos iniciales."""
        self.dinosaurio = Dinosaurio("assets/images/dino.png")
        self.cacti = arcade.SpriteList()
        self.ground_list = arcade.SpriteList()

        # Añade cactus al juego
        for _ in range(3):
            cactus = Cactus("assets/images/cactus.png", speed=SPEED)
            cactus.center_x = SCREEN_WIDTH + 100 * _
            cactus.center_y = 50
            self.cacti.append(cactus)

        # Añade las piezas de suelo
        for _ in range(2):
            ground = Suelo("assets/images/ground.png", speed=SPEED)
            ground.center_x = SCREEN_WIDTH / 2 + SCREEN_WIDTH * _
            ground.center_y = 50
            self.ground_list.append(ground)

        self.dinosaurio.setup_physics(self.ground_list)

    def on_draw(self):
        """Dibuja todos los elementos del juego en la pantalla."""
        arcade.start_render()
        self.dinosaurio.draw()
        self.cacti.draw()
        self.ground_list.draw()

    def update(self, delta_time):
        """Actualiza el estado del juego."""
        self.dinosaurio.update()
        self.cacti.update()
        self.ground_list.update()

        # Comprobar colisiones entre el dinosaurio y los cactus
        if arcade.check_for_collision_with_list(self.dinosaurio, self.cacti):
            arcade.close_window()  # Termina el juego si hay colisión

    def on_key_press(self, key, modifiers):
        """Maneja los eventos de teclado."""
        if key == arcade.key.UP or key == arcade.key.SPACE:
            self.dinosaurio.saltar()

if __name__ == "__main__":
    game = DinoRunner(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()
