from dino_runner.main import DinoRunner
import arcade

if __name__ == '__main__':
    game = DinoRunner(800, 600, "Dino Runner")
    game.setup()
    arcade.run()