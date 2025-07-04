import pygame
from typing import Optional
from src.utils.logger import Logger
from src.windows.screens.theme_selection import ThemeSelectionScreen

class Launcher:
    def __init__(self) -> None:
        pygame.init()
        pygame.freetype.init()
        
        self.running: bool = True
        Logger.info("Launcher", "Initializing game launcher...")
    
    def start(self) -> None:
        try:
            current_screen = ThemeSelectionScreen()
            
            while self.running:
                Logger.info("Launcher", "Running screen: " + current_screen.__class__.__name__)
                result = current_screen.run()
                
                if result is None:
                    Logger.info("Launcher", "No next screen, exiting")
                    self.running = False
                else:
                    current_screen = result
                    Logger.info("Launcher", "Moving to next screen: " + current_screen.__class__.__name__)
            
            Logger.info("Launcher", "Game launcher closed")
        except Exception as e:
            Logger.error("Launcher", f"Error in launcher: {e}")
        finally:
            pygame.quit()

if __name__ == "__main__":
    launcher = Launcher()
    launcher.start() 