import arcade
from arcade import PhysicsEngineSimple

from dino_runner.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Dinosaurio(arcade.Sprite):
    """
    Clase que representa al Dinosaurio en el juego.

    Atributos:
    ----------
    center_x, center_y : float
        Establecen la posición inicial del dinosaurio en la pantalla.
    change_y : float
        Representa la velocidad vertical del dinosaurio, controlando el movimiento en el eje Y.
    gravity : float
        Define la gravedad que afecta al dinosaurio, haciendo que caiga hacia abajo.
    jump_speed : float
        Define la velocidad inicial en el eje Y cuando el dinosaurio salta.
    can_jump : bool
        Indica si el dinosaurio puede saltar o no (por ejemplo, si está en el suelo).
    physics_engine : PhysicsEngineSimple
        Instancia del motor de física de Arcade que maneja el movimiento y las colisiones del dinosaurio.

    Métodos:
    --------
    setup_physics(ground: arcade.Sprite) -> None:
        Configura el motor de física para el dinosaurio.
    update() -> None:
        Actualiza el estado del dinosaurio (se llama automáticamente por Arcade).
    saltar() -> None:
        Hace que el dinosaurio salte, cambiando su velocidad en el eje Y si puede saltar.
    """
    def __init__(self, image_path: str, scale: float = 0.5):
        """
        Inicializa un objeto de la clase Dinosaurio.

        Parámetros:
        -----------
        image_path : str
            Ruta a una imagen para el sprite del dinosaurio.
        scale : float, opcional
            Factor de escala para el sprite del dinosaurio.
        """
        super().__init__(image_path, scale=0.5)
        self.center_x = SCREEN_WIDTH // 8
        self.center_y = SCREEN_HEIGHT // 4
        self.change_y = 0

        # Gravedad y velocidad de salto para controlar el movimiento en el eje Y
        self.gravity = -1
        self.jump_speed = 15
        
        self.can_jump = True  # Para verificar si el dinosaurio está en el suelo y puede saltar
        
        # Usamos un simple motor de física para manejar el movimiento y las colisiones
        self.physics_engine = None

    def setup_physics(self, ground):
        """
        Configura el motor de física para el dinosaurio.

        Parámetros:
        -----------
        ground : arcade.Sprite
            Objeto que representaría el suelo para gestionar las colisiones.
        """
        self.physics_engine = PhysicsEngineSimple(self, ground)

    def update(self):
        """
        Actualiza el estado del dinosaurio.
        
        Aplica la gravedad, actualiza la posición del dinosaurio y verifica si está en el suelo.
        Se llama automáticamente por Arcade.
        """
        # Aplica gravedad
        if not self.can_jump:
            self.change_y += self.gravity

        # Llama al motor de física para actualizar la posición
        if self.physics_engine:
            self.physics_engine.update()

        # Verifica si el dinosaurio está en el suelo
        if self.change_y == 0:
            self.can_jump = True
            self.change_y = 0
        else:
            self.can_jump = False

    def saltar(self):
        """
        Hace que el dinosaurio salte.

        Cambia la velocidad en el eje Y del dinosaurio si puede saltar.
        """
        if self.can_jump:
            self.change_y = self.jump_speed
            self.can_jump = False