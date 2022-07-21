import sys, pygame
from pygame.locals import *
import pongVersus
    
def PongMainMenu():    
    BACKGROUND_COLOR=(0,0,0)

    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    fpsClock=pygame.time.Clock()
    fpsClock_value=60
      
    #===== MENU =====        
    def menuInteraction():
        screenWidth, screenHeight = pygame.display.get_surface().get_size()   
        FontColor=(255,255,255)
        FontColorHovered=(200,200,200)
                
        PongFontLittleSize=((screenWidth+screenHeight)//2)//16
        PongFontLittle = pygame.font.Font('ressources/pong-font.ttf',PongFontLittleSize)
                
        GameTitle = pygame.image.load('sprites/PongTitle.png')
        GameTitle_Size=((screenWidth+screenHeight)//2)//40
        GameTitle = pygame.transform.scale(GameTitle, (GameTitle.get_width()*GameTitle_Size, GameTitle.get_height()*GameTitle_Size))
        GameTitle_Rect = GameTitle.get_rect()
        GameTitle_Rect.center=(screenWidth/2, screenHeight/4)
        screen.blit(GameTitle, GameTitle_Rect)
                
        buttonHeight=GameTitle_Rect.height*2.5
        
        Menu_ButtonText_1VS1="Jouer"
        Menu_ButtonText_Quit="Quitter"
                
        #Menu 1vs1
        Menu_1VS1Btn=PongFontLittle.render(Menu_ButtonText_1VS1, True , FontColor)
        Menu_1VS1Btn_Rect=Menu_1VS1Btn.get_rect()
        buttonHeight+=Menu_1VS1Btn_Rect.height*1.6
        Menu_1VS1Btn_Rect.center=(screenWidth/2, buttonHeight)
                
        #Menu quitter
        Menu_QuitBtn=PongFontLittle.render(Menu_ButtonText_Quit, True , FontColor)
        Menu_QuitBtn_Rect=Menu_QuitBtn.get_rect()
        buttonHeight+=Menu_QuitBtn_Rect.height*2.3
        Menu_QuitBtn_Rect.center=(screenWidth/2, buttonHeight)
                
                
        mouse = pygame.mouse.get_pos()
                
        #Bouton 1vs1 Hover
        if Menu_1VS1Btn_Rect.left<=mouse[0]<=Menu_1VS1Btn_Rect.right and Menu_1VS1Btn_Rect.top<=mouse[1]<=Menu_1VS1Btn_Rect.bottom:
            Menu_1VS1Btn=PongFontLittle.render(Menu_ButtonText_1VS1, True , FontColorHovered)
            screen.blit(Menu_1VS1Btn, Menu_1VS1Btn_Rect)
        else:
            screen.blit(Menu_1VS1Btn, Menu_1VS1Btn_Rect)
                    
        #Bouton Quitter Hover
        if Menu_QuitBtn_Rect.left<=mouse[0]<=Menu_QuitBtn_Rect.right and Menu_QuitBtn_Rect.top<=mouse[1]<=Menu_QuitBtn_Rect.bottom:
            Menu_QuitBtn=PongFontLittle.render(Menu_ButtonText_Quit, True , FontColorHovered)
            screen.blit(Menu_QuitBtn, Menu_QuitBtn_Rect)
        else:
            screen.blit(Menu_QuitBtn, Menu_QuitBtn_Rect)
                    
                    
                    
        return {"1vs1": Menu_1VS1Btn_Rect, "quit": Menu_QuitBtn_Rect}
    #==========
      
    pygame.mouse.set_visible(True)
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
      
    while True:
        screenWidth, screenHeight = pygame.display.get_surface().get_size()
        screen.fill(BACKGROUND_COLOR)
        
        Menu_BtnsRect = menuInteraction()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for Menu_Button in Menu_BtnsRect:
                    if Menu_BtnsRect[Menu_Button].left <= mouse[0] <= Menu_BtnsRect[Menu_Button].right and Menu_BtnsRect[Menu_Button].top <= mouse[1] <= Menu_BtnsRect[Menu_Button].bottom:
                        if Menu_Button=="1vs1":
                            return pongVersus.PongVersus()
                        if Menu_Button=="quit":
                            pygame.quit()
                            sys.exit()

        pygame.display.update()
        fpsClock.tick(fpsClock_value)
        
    pygame.quit()
    sys.exit()