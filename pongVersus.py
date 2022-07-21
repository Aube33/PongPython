import sys, pygame, time, random
from pygame.locals import *
import pongChoice, pongMenu

def PongVersus(player1Color=(255,255,255), player2Color=(255,255,255)):
    player1Color, player2Color=pongChoice.PongChoice()
    BACKGROUND_COLOR=(0,0,0)
    TERRAIN_COLOR=(0,0,0)
    BUTS_COLOR=(255,255,255)
    BUTS_WIDTH=10
    DEFAULT_PLAYER_COLOR=(255,255,255)
    BALL_COLOR=[(219,11,1),(226,58,9),(230,90,13),(237,126,19),(241,159,23),(246,194,30),(249,220,32),(255,255,140),(255,255,255)]
    BALL_SPEED=3

    class Player:
        def __init__(self):
            screenWidth, screenHeight = pygame.display.get_surface().get_size()

            self.image = pygame.Surface([10,screenHeight//8])

            self.image.fill(DEFAULT_PLAYER_COLOR)
            self.rect = self.image.get_rect()

            self.score=0
            self.vitesse=9

        def display(self,screen,rect, playerColor):
            screenWidth, screenHeight = pygame.display.get_surface().get_size()

            self.image = pygame.Surface([10,screenHeight//8])
            self.image.fill(playerColor)
            self.rect = self.image.get_rect()

            screen.blit(self.image, rect)

        def controls(self, rect, playerNumber="1"):
            screenWidth, screenHeight = pygame.display.get_surface().get_size()

            if playerNumber=="1":
                key = pygame.key.get_pressed()
                if key[pygame.K_z]:
                    if 0<=rect.y:
                        rect=rect.move(0, -self.vitesse)
                if key[pygame.K_s]:
                    if rect.y<screenHeight-self.rect.height:
                        rect=rect.move(0, self.vitesse)
                '''
                if y1>=512:
                    if 0<=rect.y:
                        rect=rect.move(0, -self.vitesse)
                if y1<512:
                    if rect.y<screenHeight-self.rect.height:
                        rect=rect.move(0, self.vitesse)
                '''
                try:
                    rect.y=y1
                except:
                    pass
                return rect

            elif playerNumber=="2":
                key = pygame.key.get_pressed()
                if key[pygame.K_UP]:
                    if 0<=rect.y:
                        rect=rect.move(0, -self.vitesse)
                if key[pygame.K_DOWN]:
                    if rect.y<screenHeight-self.rect.height:
                        rect=rect.move(0, self.vitesse)
                '''
                if y2>=512:
                    if 0<=rect.y:
                        rect=rect.move(0, -self.vitesse)
                if y2<512:
                    if rect.y<screenHeight-self.rect.height:
                        rect=rect.move(0, self.vitesse)
                '''
                try:
                    rect.y=y2
                except:
                    pass
                return rect


    #===== BALLE =====
    class Ball:
        screenWidth, screenHeight = pygame.display.get_surface().get_size()

        image = pygame.Surface([2,2])

        image.fill((255,255,255))
        rect = image.get_rect()

        reflets=[]

        vitesse=BALL_SPEED
        x_speed=-1
        y_speed=0

        colorIndex=0

        sender="player1"
        '''
        def particule(self, quantity, rect):
            if self.vitesse>0:
                screenWidth, screenHeight = pygame.display.get_surface().get_size()

                particle = pygame.Surface([13,13])
                particle.fill((255,255,255))
                particle_Rect = particle.get_rect()
                particle_Rect.center=(rect.centerx+particle_Rect.width, rect.centery+particle_Rect.height)

                particle_Rect.x+=self.x_speed*self.vitesse
                particle_Rect.y+=self.y_speed*self.vitesse

                screen.blit(particle, particle_Rect)
           '''

        def reset(self, rect, lastPlayer="1"):
            screenWidth, screenHeight = pygame.display.get_surface().get_size()

            self.vitesse=BALL_SPEED
            self.colorIndex=0
            if lastPlayer=="2":
                self.x_speed=1
            elif lastPlayer=="1":
                self.x_speed=-1
            self.y_speed=0

            rect.center=(screenWidth/2,screenHeight/2)

            return rect

        def display(self,screen,rect):
            screenWidth, screenHeight = pygame.display.get_surface().get_size()

            self.image = pygame.Surface([2,2])
            self.image.fill(BALL_COLOR[self.colorIndex])
            self.rect = self.image.get_rect()
            self.imageResize=((screenWidth+screenHeight)/2)//100
            self.image = pygame.transform.scale(self.image, (2*self.imageResize, 2*self.imageResize))

            screen.blit(self.image, rect)

            #self.particule(1, rect)

        def upgradeSpeed(self, speed):
            if self.vitesse<=7:
                if self.vitesse==3:
                    self.colorIndex=0
                elif 3<self.vitesse<=3.5:
                    self.colorIndex=1
                elif 3.5<self.vitesse<=4:
                    self.colorIndex=2
                elif 4<self.vitesse<=4.5:
                    self.colorIndex=3
                elif 4.5<self.vitesse<=5:
                    self.colorIndex=4
                elif 5<self.vitesse<=5.5:
                    self.colorIndex=5
                elif 5.5<self.vitesse<=6:
                    self.colorIndex=6
                elif 6<self.vitesse<=6.5:
                    self.colorIndex=7
                elif 6.5<self.vitesse<=7:
                    self.colorIndex=8

                self.vitesse+=speed

        def movement(self, rect, player1:list, player2:list, buts1Rect, buts2Rect):
            screenWidth, screenHeight = pygame.display.get_surface().get_size()

            player1Rect=player1[1]
            player2Rect=player2[1]

            player1=player1[0]
            player2=player2[0]

            rect.x+=self.x_speed*self.vitesse
            rect.y+=self.y_speed*self.vitesse

            if abs(rect.x)>screenWidth+500:
                return rect
            if abs(rect.y)>screenHeight+500:
                return rect
            if rect.bottom>=screenHeight-30 or rect.top<=0:
                self.y_speed*=-1

            #JOUEUR 1
            if self.x_speed<0:
                if abs(rect.left - player1Rect.right) < 5 and player1Rect.bottom-(player1Rect.height*1.2) <= rect.centery <= player1Rect.top+player1Rect.height:

                    #Redirection lors de l'engagement de la balle
                    if self.y_speed==0:
                        self.y_speed=1

                    #Direction de la balle en fonction du point touché sur le pad 1
                    if player1Rect.bottom-(player1Rect.height*1.2)/3 <= rect.centery <= player1Rect.top+player1Rect.height:
                        self.x_speed*=-1
                        self.y_speed*=1
                        self.upgradeSpeed(0.25)
                    elif player1Rect.bottom-(player1Rect.height*1.2) <= rect.centery <= player1Rect.top+player1Rect.height/3:
                        self.x_speed*=-1
                        self.y_speed*=-1
                        self.upgradeSpeed(0.25)
                    else:
                        self.x_speed*=-1
                        self.upgradeSpeed(1)

                    self.sender="player1"



            #JOUEUR 2
            if self.x_speed>0:
                if abs(rect.right - player2Rect.left) < 30 and player2Rect.bottom-(player2Rect.height*1.2) <= rect.centery <= player2Rect.top+player2Rect.height:

                    #Redirection lors de l'engagement de la balle
                    if self.y_speed==0:
                        self.y_speed=-1

                    #Direction de la balle en fonction du point touché sur le pad 2
                    if player2Rect.bottom-(player2Rect.height*1.2)/3 <= rect.centery <= player2Rect.top+player2Rect.height:
                        self.x_speed*=-1
                        self.y_speed*=-1
                        self.upgradeSpeed(0.25)
                    elif player2Rect.bottom-(player2Rect.height*1.2) <= rect.centery <= player2Rect.top+player2Rect.height/3:
                        self.x_speed*=-1
                        self.y_speed*=1
                        self.upgradeSpeed(0.25)
                    else:
                        self.x_speed*=-1
                        self.upgradeSpeed(1)


                    self.sender="player2"



            #Buts joeurs 1
            if self.x_speed<0:
                if rect.x<buts1Rect.x:
                    player2.score+=1
                    rect=self.reset(rect, "1")

            #Buts joeurs 2
            elif self.x_speed>0:
                if rect.x+23>buts2Rect.x:
                    player1.score+=1
                    rect=self.reset(rect, "2")

            return rect

    #==========



    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screenWidth, screenHeight = pygame.display.get_surface().get_size()

    fpsClock=pygame.time.Clock()
    fpsClock_value=120

    player1 = Player()
    player2 = Player()
    ball = Ball()

    player1Rect=player1.rect
    player1Rect.center=(screenWidth/2, screenHeight/2)

    player2Rect=player2.rect
    player2Rect.center=(screenWidth/2, screenHeight/2)

    ballRect=ball.rect
    ballRect.center=(screenWidth/2, screenHeight/2)




    #===== TERRAIN =====
    def updateTerrain():
        screenWidth, screenHeight = pygame.display.get_surface().get_size()

        terrainWidth=screenHeight+(screenHeight//4)
        terrainHeight=screenHeight

        terrain = pygame.Surface([terrainWidth,terrainHeight])
        terrain.fill(TERRAIN_COLOR)
        terrainRect = terrain.get_rect()
        terrainRect.center=(screenWidth/2, screenHeight/2)


        buts1 = pygame.Surface([BUTS_WIDTH,screenHeight])
        buts1.fill(player1Color)
        buts1Rect = buts1.get_rect()
        buts1Rect.center=(screenWidth/2-(terrainWidth/2), screenHeight/2)
        screen.blit(buts1, buts1Rect)

        buts2 = pygame.Surface([BUTS_WIDTH,screenHeight])
        buts2.fill(player2Color)
        buts2Rect = buts2.get_rect()
        buts2Rect.center=(screenWidth/2+(terrainWidth/2), screenHeight/2)
        screen.blit(buts2, buts2Rect)

        padBut_space=15
        player1Rect.x=buts1Rect.x+padBut_space
        player2Rect.x=buts2Rect.x-player2Rect.width+buts2Rect.width-padBut_space
        screen.blit(terrain, terrainRect)

        pygame.draw.line(screen, (150,150,150), (screenWidth//2, 30), (screenWidth//2, screenHeight-30), 2)

        return (buts1Rect, buts2Rect)
    #==========


    #===== MENU FIN =====
    IsEnded=False
    IsEndeded=False
    playerWinner="Joueur -1"

    def menuWin(IsEnded, IsEndeded, playerWinner="Joueur 0"):
        if IsEnded:
            screenWidth, screenHeight = pygame.display.get_surface().get_size()
            FontColor=(255,255,255)
            FontColorHovered=(200,200,200)

            PongFontSize=((screenWidth+screenHeight)//2)//8
            PongFont = pygame.font.Font('ressources/pong-font.ttf',PongFontSize)

            PongFontMiddleSize=((screenWidth+screenHeight)//2)//15
            PongFontMiddle = pygame.font.Font('ressources/pong-font.ttf',PongFontMiddleSize)

            PongFontLittleSize=((screenWidth+screenHeight)//2)//22
            PongFontLittle = pygame.font.Font('ressources/pong-font.ttf',PongFontLittleSize)

            key = pygame.key.get_pressed()

            if not IsEndeded:
                pauseBackground = pygame.Surface([screenWidth, screenHeight])
                pauseBackground = pauseBackground.convert_alpha()
                pauseBackground.fill((0,0,0,150))
                screen.blit(pauseBackground, (0,0))
                IsEndeded=True

            pygame.mouse.set_visible(True)
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

            #Title du menu
            Menu_Title=PongFont.render("Winner", True , FontColor)
            Menu_Title_Rect=Menu_Title.get_rect()
            Menu_Title_Rect.center=(screenWidth/2, Menu_Title_Rect.height*2)
            screen.blit(Menu_Title, Menu_Title_Rect)

            buttonHeight=Menu_Title_Rect.height*2.8

            #Title du Gagant
            if playerWinner=="Joueur 1":
                Menu_Title_Winner=PongFontMiddle.render(playerWinner, True , player1Color)
            elif playerWinner=="Joueur 2":
                Menu_Title_Winner=PongFontMiddle.render(playerWinner, True , player2Color)
            else:
                Menu_Title_Winner=PongFontMiddle.render(playerWinner, True , FontColor)

            Menu_Title_Winner_Rect=Menu_Title_Winner.get_rect()
            Menu_Title_Winner_Rect.center=(screenWidth/2, buttonHeight)
            screen.blit(Menu_Title_Winner, Menu_Title_Winner_Rect)

            buttonHeight=Menu_Title_Rect.height*3.2

            #Menu rejouer
            Menu_ReplayBtn=PongFontLittle.render("Rejouer", True , FontColor)
            Menu_ReplayBtn_Rect=Menu_ReplayBtn.get_rect()
            buttonHeight+=Menu_ReplayBtn_Rect.height*1.6
            Menu_ReplayBtn_Rect.center=(screenWidth/2, buttonHeight)

            #Menu menu principal
            Menu_MainMenuBtn=PongFontLittle.render("Menu Principal", True , FontColor)
            Menu_MainMenuBtn_Rect=Menu_MainMenuBtn.get_rect()
            buttonHeight+=Menu_MainMenuBtn_Rect.height*1.6
            Menu_MainMenuBtn_Rect.center=(screenWidth/2, buttonHeight)


            #Menu quitter
            Menu_QuitBtn=PongFontLittle.render("Quitter", True , FontColor)
            Menu_QuitBtn_Rect=Menu_QuitBtn.get_rect()
            buttonHeight+=Menu_QuitBtn_Rect.height*1.6
            Menu_QuitBtn_Rect.center=(screenWidth/2, buttonHeight)


            mouse = pygame.mouse.get_pos()

            #Bouton Rejouer Hover
            if Menu_ReplayBtn_Rect.left<=mouse[0]<=Menu_ReplayBtn_Rect.right and Menu_ReplayBtn_Rect.top<=mouse[1]<=Menu_ReplayBtn_Rect.bottom:
                Menu_ReplayBtn=PongFontLittle.render("Rejouer", True , FontColorHovered)
                screen.blit(Menu_ReplayBtn, Menu_ReplayBtn_Rect)
            else:
                screen.blit(Menu_ReplayBtn, Menu_ReplayBtn_Rect)

            #Bouton MenuPrincipal Hover
            if Menu_MainMenuBtn_Rect.left<=mouse[0]<=Menu_MainMenuBtn_Rect.right and Menu_MainMenuBtn_Rect.top<=mouse[1]<=Menu_MainMenuBtn_Rect.bottom:
                Menu_MainMenuBtn=PongFontLittle.render("Menu Principal", True , FontColorHovered)
                screen.blit(Menu_MainMenuBtn, Menu_MainMenuBtn_Rect)
            else:
                screen.blit(Menu_MainMenuBtn, Menu_MainMenuBtn_Rect)

            #Bouton Quitter Hover
            if Menu_QuitBtn_Rect.left<=mouse[0]<=Menu_QuitBtn_Rect.right and Menu_QuitBtn_Rect.top<=mouse[1]<=Menu_QuitBtn_Rect.bottom:
                Menu_QuitBtn=PongFontLittle.render("Quitter", True , FontColorHovered)
                screen.blit(Menu_QuitBtn, Menu_QuitBtn_Rect)
            else:
                screen.blit(Menu_QuitBtn, Menu_QuitBtn_Rect)

            return IsEnded, IsEndeded, {"replay": Menu_ReplayBtn_Rect, "mainmenu": Menu_MainMenuBtn_Rect, "quit": Menu_QuitBtn_Rect}
        else:
            return IsEnded, IsEndeded, {}
    #==========


    #===== SCORE =====
    def updateScore(IsEnded):
        screenWidth, screenHeight = pygame.display.get_surface().get_size()
        PongFontSize=((screenWidth+screenHeight)//2)//8
        PongFont = pygame.font.Font('ressources/pong-font.ttf',PongFontSize)

        playerWinner="Joueur 0"

        player1Score=player1.score
        if player1Score>=5:
            ScorePlayer1 = PongFont.render("5", True , (40,180,75))
            IsEnded=True
            playerWinner="Joueur 1"
        else:
            ScorePlayer1 = PongFont.render(str(player1Score), True , (255,255,255))

        player2Score=player2.score
        if player2Score>=5:
            ScorePlayer2 = PongFont.render("5", True , (40,180,75))
            IsEnded=True
            playerWinner="Joueur 2"
        else:
            ScorePlayer2 = PongFont.render(str(player2Score), True , (255,255,255))

        screen.blit(ScorePlayer1, ((screenWidth/2-37)-170, 30))
        screen.blit(ScorePlayer2, ((screenWidth/2-37)+170, 30))

        return IsEnded, playerWinner
    #==========



    #===== MENU PAUSE =====
    IsPaused=False
    menuIntervale=200
    lastMenuPressed=0

    def menuPause(IsPaused, lastMenuPressed, IsEnded):
        screenWidth, screenHeight = pygame.display.get_surface().get_size()
        FontColor=(255,255,255)
        FontColorHovered=(200,200,200)

        PongFontSize=((screenWidth+screenHeight)//2)//8
        PongFont = pygame.font.Font('ressources/pong-font.ttf',PongFontSize)

        PongFontLittleSize=((screenWidth+screenHeight)//2)//22
        PongFontLittle = pygame.font.Font('ressources/pong-font.ttf',PongFontLittleSize)

        key = pygame.key.get_pressed()

        if key[pygame.K_ESCAPE] and time.time()*1000>lastMenuPressed+menuIntervale and not IsEnded:
            lastMenuPressed=time.time()*1000

            pauseBackground = pygame.Surface([screenWidth, screenHeight])
            pauseBackground = pauseBackground.convert_alpha()
            pauseBackground.fill((0,0,0,150))
            screen.blit(pauseBackground, (0,0))

            IsPaused = not IsPaused

        if IsPaused:
            pygame.mouse.set_visible(True)
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

            #Title du menu
            Menu_Title=PongFont.render("Pause", True , FontColor)
            Menu_Title_Rect=Menu_Title.get_rect()
            Menu_Title_Rect.center=(screenWidth/2, Menu_Title_Rect.height*2)
            screen.blit(Menu_Title, Menu_Title_Rect)

            buttonHeight=Menu_Title_Rect.height*2.8

            #Menu continuer
            Menu_ContinueBtn=PongFontLittle.render("Continuer", True , FontColor)
            Menu_ContinueBtn_Rect=Menu_ContinueBtn.get_rect()
            buttonHeight+=Menu_ContinueBtn_Rect.height*1.6
            Menu_ContinueBtn_Rect.center=(screenWidth/2, buttonHeight)

            #Menu rejouer
            Menu_ReplayBtn=PongFontLittle.render("Rejouer", True , FontColor)
            Menu_ReplayBtn_Rect=Menu_ReplayBtn.get_rect()
            buttonHeight+=Menu_ReplayBtn_Rect.height*1.6
            Menu_ReplayBtn_Rect.center=(screenWidth/2, buttonHeight)

            #Menu menu principal
            Menu_MainMenuBtn=PongFontLittle.render("Menu Principal", True , FontColor)
            Menu_MainMenuBtn_Rect=Menu_MainMenuBtn.get_rect()
            buttonHeight+=Menu_MainMenuBtn_Rect.height*1.6
            Menu_MainMenuBtn_Rect.center=(screenWidth/2, buttonHeight)


            #Menu quitter
            Menu_QuitBtn=PongFontLittle.render("Quitter", True , FontColor)
            Menu_QuitBtn_Rect=Menu_QuitBtn.get_rect()
            buttonHeight+=Menu_QuitBtn_Rect.height*1.6
            Menu_QuitBtn_Rect.center=(screenWidth/2, buttonHeight)


            mouse = pygame.mouse.get_pos()

            #Bouton Continuer Hover
            if Menu_ContinueBtn_Rect.left<=mouse[0]<=Menu_ContinueBtn_Rect.right and Menu_ContinueBtn_Rect.top<=mouse[1]<=Menu_ContinueBtn_Rect.bottom:
                Menu_ContinueBtn=PongFontLittle.render("Continuer", True , FontColorHovered)
                screen.blit(Menu_ContinueBtn, Menu_ContinueBtn_Rect)
            else:
                screen.blit(Menu_ContinueBtn, Menu_ContinueBtn_Rect)

            #Bouton Rejouer Hover
            if Menu_ReplayBtn_Rect.left<=mouse[0]<=Menu_ReplayBtn_Rect.right and Menu_ReplayBtn_Rect.top<=mouse[1]<=Menu_ReplayBtn_Rect.bottom:
                Menu_ReplayBtn=PongFontLittle.render("Rejouer", True , FontColorHovered)
                screen.blit(Menu_ReplayBtn, Menu_ReplayBtn_Rect)
            else:
                screen.blit(Menu_ReplayBtn, Menu_ReplayBtn_Rect)

            #Bouton MenuPrincipal Hover
            if Menu_MainMenuBtn_Rect.left<=mouse[0]<=Menu_MainMenuBtn_Rect.right and Menu_MainMenuBtn_Rect.top<=mouse[1]<=Menu_MainMenuBtn_Rect.bottom:
                Menu_MainMenuBtn=PongFontLittle.render("Menu Principal", True , FontColorHovered)
                screen.blit(Menu_MainMenuBtn, Menu_MainMenuBtn_Rect)
            else:
                screen.blit(Menu_MainMenuBtn, Menu_MainMenuBtn_Rect)

            #Bouton Quitter Hover
            if Menu_QuitBtn_Rect.left<=mouse[0]<=Menu_QuitBtn_Rect.right and Menu_QuitBtn_Rect.top<=mouse[1]<=Menu_QuitBtn_Rect.bottom:
                Menu_QuitBtn=PongFontLittle.render("Quitter", True , FontColorHovered)
                screen.blit(Menu_QuitBtn, Menu_QuitBtn_Rect)
            else:
                screen.blit(Menu_QuitBtn, Menu_QuitBtn_Rect)



            return IsPaused, lastMenuPressed, {"continue": Menu_ContinueBtn_Rect, "replay": Menu_ReplayBtn_Rect, "mainmenu": Menu_MainMenuBtn_Rect, "quit": Menu_QuitBtn_Rect}

        else:
            if not IsEnded:
                pygame.mouse.set_visible(False)
            return IsPaused, lastMenuPressed, {}
    #==========



    while True:
        IsEnded, IsEndeded, MenuWin_BtnsRect = menuWin(IsEnded, IsEndeded, playerWinner)
        IsPaused, lastMenuPressed, MenuPause_BtnsRect = menuPause(IsPaused, lastMenuPressed, IsEnded)

        if not IsEnded and not IsPaused:
            screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == QUIT:
                main = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    fpsClock_value=5

            if event.type == pygame.MOUSEBUTTONDOWN:
                if IsPaused:
                    mouse = pygame.mouse.get_pos()
                    for Menu_Button in MenuPause_BtnsRect:
                        if MenuPause_BtnsRect[Menu_Button].left <= mouse[0] <= MenuPause_BtnsRect[Menu_Button].right and MenuPause_BtnsRect[Menu_Button].top <= mouse[1] <= MenuPause_BtnsRect[Menu_Button].bottom:
                            if Menu_Button=="continue":
                                IsPaused=False
                            if Menu_Button=="replay":
                                return PongVersus(player1Color, player2Color)
                            if Menu_Button=="mainmenu":
                                return pongMenu.PongMainMenu()
                            if Menu_Button=="quit":
                                pygame.quit()
                                sys.exit()
                elif IsEnded:
                    mouse = pygame.mouse.get_pos()
                    for Menu_Button in MenuWin_BtnsRect:
                        if MenuWin_BtnsRect[Menu_Button].left <= mouse[0] <= MenuWin_BtnsRect[Menu_Button].right and MenuWin_BtnsRect[Menu_Button].top <= mouse[1] <= MenuWin_BtnsRect[Menu_Button].bottom:
                            if Menu_Button=="replay":
                                return PongVersus(player1Color, player2Color)
                            if Menu_Button=="mainmenu":
                                return pongMenu.PongMainMenu()
                            if Menu_Button=="quit":
                                pygame.quit()
                                sys.exit()


        if not IsEnded and not IsPaused:
            buts1Rect, buts2Rect=updateTerrain()

            player1Rect=player1.controls(player1Rect, "1")
            player1.display(screen, player1Rect, player1Color)

            player2Rect=player2.controls(player2Rect, "2")
            player2.display(screen, player2Rect, player2Color)

            IsEnded, playerWinner=updateScore(IsEnded)

            ball.display(screen, ballRect)
            ballRect=ball.movement(ballRect, [player1, player1Rect], [player2, player2Rect], buts1Rect, buts2Rect)

        pygame.display.update()
        fpsClock.tick(fpsClock_value)

    pygame.quit()
    sys.exit()
