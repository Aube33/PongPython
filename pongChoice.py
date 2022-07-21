import sys, pygame, time
from pygame.locals import *

def PongChoice():
    BACKGROUND_COLOR=(0,0,0)
    SELECTOR_COLOR=(240,240,240)
    MIDDLELINE_COLOR=(150,150,150)

    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screenWidth, screenHeight = pygame.display.get_surface().get_size()

    fpsClock=pygame.time.Clock()
    fpsClock_value=60

    pygame.mouse.set_visible(False)

    class Selector:
        screenWidth, screenHeight = pygame.display.get_surface().get_size()

        image = pygame.Surface([0,0])
        rect = image.get_rect()

        lastKeyPressed=0
        intervale=150
        ready=False


        def display(self,screen,rect):
            screenWidth, screenHeight = pygame.display.get_surface().get_size()

            pygame.draw.rect(screen, SELECTOR_COLOR, rect, 5)


        def controls(self, player, rect, movement, posDict):
            key = pygame.key.get_pressed()

            if player=="1":
                # == Déplacements ==
                if not(self.ready):
                    if key[pygame.K_z] and time.time()*1000>self.lastKeyPressed+self.intervale:
                        rect.y-=movement
                        for i in posDict:
                            if rect.center == posDict[i][1] or rect.center == posDict[i][2]:
                                pygame.draw.rect(screen, (240,240,240), rect, 5)
                                self.lastKeyPressed=time.time()*1000
                                return rect
                        rect.y+=movement

                    elif key[pygame.K_s] and time.time()*1000>self.lastKeyPressed+self.intervale:
                        rect.y+=movement
                        for i in posDict:
                            if rect.center == posDict[i][1] or rect.center == posDict[i][2]:
                                pygame.draw.rect(screen, (240,240,240), rect, 5)
                                self.lastKeyPressed=time.time()*1000
                                return rect
                        rect.y-=movement

                    elif key[pygame.K_q] and time.time()*1000>self.lastKeyPressed+self.intervale:
                        rect.x-=movement
                        for i in posDict:
                            if rect.center == posDict[i][1] or rect.center == posDict[i][2]:
                                pygame.draw.rect(screen, (240,240,240), rect, 5)
                                self.lastKeyPressed=time.time()*1000
                                return rect
                        rect.x+=movement

                    elif key[pygame.K_d] and time.time()*1000>self.lastKeyPressed+self.intervale:
                        rect.x+=movement
                        for i in posDict:
                            if rect.center == posDict[i][1] or rect.center == posDict[i][2]:
                                pygame.draw.rect(screen, (240,240,240), rect, 5)
                                self.lastKeyPressed=time.time()*1000
                                return rect
                        rect.x-=movement
                # ===

                #Confirmation
                if key[pygame.K_a] and time.time()*1000>self.lastKeyPressed+self.intervale:
                    self.ready=not(self.ready)
                    self.lastKeyPressed=time.time()*1000
                return rect

            if player=="2":
                # == Déplacements ==
                if not(self.ready):
                    if key[pygame.K_UP] and time.time()*1000>self.lastKeyPressed+self.intervale:
                        rect.y-=movement
                        for i in posDict:
                            if rect.center == posDict[i][1] or rect.center == posDict[i][2]:
                                pygame.draw.rect(screen, (240,240,240), rect, 5)
                                self.lastKeyPressed=time.time()*1000
                                return rect
                        rect.y+=movement

                    elif key[pygame.K_DOWN] and time.time()*1000>self.lastKeyPressed+self.intervale:
                        rect.y+=movement
                        for i in posDict:
                            if rect.center == posDict[i][1] or rect.center == posDict[i][2]:
                                pygame.draw.rect(screen, (240,240,240), rect, 5)
                                self.lastKeyPressed=time.time()*1000
                                return rect
                        rect.y-=movement

                    elif key[pygame.K_LEFT] and time.time()*1000>self.lastKeyPressed+self.intervale:
                        rect.x-=movement

                        for i in posDict:
                            if rect.center == posDict[i][1] or rect.center == posDict[i][2]:
                                pygame.draw.rect(screen, (240,240,240), rect, 5)
                                self.lastKeyPressed=time.time()*1000
                                return rect
                        rect.x+=movement

                    elif key[pygame.K_RIGHT] and time.time()*1000>self.lastKeyPressed+self.intervale:
                        rect.x+=movement
                        for i in posDict:
                            if rect.center == posDict[i][1] or rect.center == posDict[i][2]:
                                pygame.draw.rect(screen, (240,240,240), rect, 5)
                                self.lastKeyPressed=time.time()*1000
                                return rect
                        rect.x-=movement
                # ===

                #Confirmation
                if key[pygame.K_RETURN] and time.time()*1000>self.lastKeyPressed+self.intervale:
                    self.ready=not(self.ready)
                    self.lastKeyPressed=time.time()*1000
                return rect






    caseSize=(screenWidth+screenHeight)/50
    Pre_SelectorImage = pygame.Surface([caseSize,caseSize])

    SelectorP1=Selector()
    SelectorP1Rect = Pre_SelectorImage.get_rect()
    SelectorP1Rect.center=(screenWidth//4,screenHeight//6*2.5)

    SelectorP2=Selector()
    SelectorP2Rect = Pre_SelectorImage.get_rect()
    SelectorP2Rect.center=(screenWidth//2+screenWidth//4,screenHeight//6*2.5)


    def ColorChoice(player:str, selectorRect):
        screenWidth, screenHeight = pygame.display.get_surface().get_size()
        PadsX1, PadsY1, PadsY2=(screenWidth/8, screenHeight/6*2, screenHeight/6*4)

        # ColorsDict -> ColorsDict{NomCouleur, CouleurRGB, PosPlayer1, PosPlayer2}
        ColorsDict={
            "blanc":[(255,255,255), (0,0), (0,0)],
            "jaune":[(255,200,50), (0,0), (0,0)],
            "orange":[(255,110,50), (0,0), (0,0)],
            "rouge":[(255,60,50), (0,0), (0,0)],
            "carmin":[(255,33,124), (0,0), (0,0)],
            "magenta":[(240,90,150), (0,0), (0,0)],
            "violet":[(170,40,165), (0,0), (0,0)],
            "bleu":[(100,80,230), (0,0), (0,0)],
            "outremer":[(80,130,230), (0,0), (0,0)],
            "cyan":[(45,160,230), (0,0), (0,0)],
            "turquoise":[(50,180,165), (0,0), (0,0)],
            "vert":[(40,180,75), (0,0), (0,0)],
            }

        caseSpace=20

        if player=="1":
            x=screenWidth//4
            xCompteur=0
            y=screenHeight//6*2.5

            # = Palette joueur 1 =
            for colorName, (color, posP1, posP2) in ColorsDict.items():
                CaseImage = pygame.Surface([caseSize,caseSize])
                CaseImage.fill(color)

                CaseRect = CaseImage.get_rect()
                CaseRect.center=(x,y)
                screen.blit(CaseImage,CaseRect)
                pygame.draw.rect(screen, (128,128,128), CaseRect, 4)
                ColorsDict[colorName][1]=CaseRect.center

                if xCompteur>=3:
                    y+=caseSpace+CaseRect.width
                    x=screenWidth//4
                    xCompteur=0
                else:
                    xCompteur+=1
                    x+=caseSpace+CaseRect.width
            # ===


            selectorRect=SelectorP1.controls("1", selectorRect, caseSpace+CaseRect.width, ColorsDict)
            SelectorP1.display(screen, selectorRect)

            for colorName, (color, posP1, posP2) in ColorsDict.items():
                if selectorRect.center==posP1:
                    pygame.draw.line(screen, color, (PadsX1, PadsY1), (PadsX1, PadsY2), (screenWidth+screenHeight)//90)
                    return color, selectorRect



        if player=="2":
            # = Palette joueur 2 =
            x=screenWidth//2+screenWidth//4
            xCompteur=0
            y=screenHeight//6*2.5

            for colorName, (color, posP1, posP2) in ColorsDict.items():
                CaseImage = pygame.Surface([caseSize,caseSize])
                CaseImage.fill(color)

                CaseRect = CaseImage.get_rect()
                CaseRect.center=(x,y)
                screen.blit(CaseImage,CaseRect)
                pygame.draw.rect(screen, (128,128,128), CaseRect, 3)
                ColorsDict[colorName][2]=CaseRect.center

                if xCompteur>=3:
                    y+=caseSpace+CaseRect.width
                    x=screenWidth//2+screenWidth//4
                    xCompteur=0
                else:
                    xCompteur+=1
                    x+=caseSpace+CaseRect.width
            # ===


            selectorRect=SelectorP2.controls("2", selectorRect, caseSpace+CaseRect.width, ColorsDict)
            SelectorP2.display(screen, selectorRect)

            for colorName, (color, posP1, posP2) in ColorsDict.items():
                if selectorRect.center==posP2:
                    pygame.draw.line(screen, color, (screenWidth/2+PadsX1, PadsY1), (screenWidth/2+PadsX1, PadsY2), (screenWidth+screenHeight)//90)
                    return color, selectorRect



    def updateReadyPlayers():
        screenWidth, screenHeight = pygame.display.get_surface().get_size()
        PongFontLittleSize=((screenWidth+screenHeight)//2)//23
        PongFontLittle = pygame.font.Font('ressources/pong-font.ttf',PongFontLittleSize)

        height=((screenWidth+screenHeight)//2)//16

        counter=0

        if SelectorP1.ready:
            counter+=1
        if SelectorP2.ready:
            counter+=1

        # === Compteur des joueurs prêts ===
        CounterConfirm = PongFontLittle.render(f"{counter} / 2", True , (255,255,255))
        CounterConfirm_Rect = CounterConfirm.get_rect()
        CounterConfirm_Rect.center=(screenWidth/2, height)
        screen.blit(CounterConfirm, CounterConfirm_Rect)

        CounterConfirmContainer_Image = pygame.Surface([CounterConfirm_Rect.width*1.8,CounterConfirm_Rect.height*2])
        CounterConfirmContainer_Rect = CounterConfirmContainer_Image.get_rect()
        CounterConfirmContainer_Rect.center=(screenWidth/2, height)
        if counter>=2:
            pygame.draw.rect(screen, (40,180,75), CounterConfirmContainer_Rect, 8)
        else:
            pygame.draw.rect(screen, (255,255,255), CounterConfirmContainer_Rect, 6)
        # ===





    #===== TERRAIN =====
    def updateTerrain():
        screenWidth, screenHeight = pygame.display.get_surface().get_size()
        PongFontSize=((screenWidth+screenHeight)//2)//13
        PongFontLittleSize=((screenWidth+screenHeight)//2)//23

        PongFont = pygame.font.Font('ressources/pong-font.ttf',PongFontSize)
        PongFontLittle = pygame.font.Font('ressources/pong-font.ttf',PongFontLittleSize)

        # === Players header text ===
        if SelectorP1.ready:
            Player1 = PongFont.render("JOUEUR 1", True, (40,180,75))
        else:
            Player1 = PongFont.render("JOUEUR 1", True, (255,255,255))
        Player1_Rect = Player1.get_rect()
        Player1_Rect.center=(screenWidth/4, Player1_Rect.height)
        screen.blit(Player1, Player1_Rect)

        if SelectorP2.ready:
            Player2 = PongFont.render("JOUEUR 2", True, (40,180,75))
        else:
            Player2 = PongFont.render("JOUEUR 2", True, (255,255,255))
        Player2_Rect = Player2.get_rect()
        Player2_Rect.center=(screenWidth/2+screenWidth/4, Player2_Rect.height)
        screen.blit(Player2, Player2_Rect)
        # ===


        # === Pads Default ===
        PadsX1, PadsY1, PadsY2=(screenWidth/8, screenHeight/6*2, screenHeight/6*4)
        pygame.draw.line(screen, (255,255,255), (PadsX1, PadsY1), (PadsX1, PadsY2), (screenWidth+screenHeight)//90)
        pygame.draw.line(screen, (255,255,255), (screenWidth/2+PadsX1, PadsY1), (screenWidth/2+PadsX1, PadsY2), (screenWidth+screenHeight)//90)
        # ===


        # === Confirmations indication ===
        if SelectorP1.ready:
            Player1Confirm = PongFontLittle.render("[A] pour annuler", True , (255,255,255))
        else:
            Player1Confirm = PongFontLittle.render("[A] pour confirmer", True , (255,255,255))
        Player1Confirm_Rect = Player1Confirm.get_rect()
        Player1Confirm_Rect.center=(screenWidth/4, screenHeight-Player1Confirm_Rect.height*1.6)
        screen.blit(Player1Confirm, Player1Confirm_Rect)


        if SelectorP2.ready:
            Player2Confirm = PongFontLittle.render("[ENTER] pour annuler", True , (255,255,255))
        else:
            Player2Confirm = PongFontLittle.render("[ENTER] pour confirmer", True , (255,255,255))
        Player2Confirm_Rect = Player2Confirm.get_rect()
        Player2Confirm_Rect.center=(screenWidth/2+screenWidth/4, screenHeight-Player2Confirm_Rect.height*1.6)
        screen.blit(Player2Confirm, Player2Confirm_Rect)
        # ===


        # === Controls Players ===
        ControlsP1Img = pygame.image.load('sprites/ControlsPlayer1.png')
        ControlsP1Img_Size=((screenWidth+screenHeight)//2)//280
        ControlsP1Img = pygame.transform.scale(ControlsP1Img, (ControlsP1Img.get_width()*ControlsP1Img_Size, ControlsP1Img.get_height()*ControlsP1Img_Size))
        ControlsP1Img_Rect = ControlsP1Img.get_rect()
        ControlsP1Img_Rect.center=(ControlsP1Img_Rect.width/1.5, ControlsP1Img_Rect.height/1.5)
        screen.blit(ControlsP1Img, ControlsP1Img_Rect)
        # ===


        pygame.draw.line(screen, MIDDLELINE_COLOR, (screenWidth//2, screenHeight//6), (screenWidth/2, screenHeight-screenHeight//20), 2)
    #==========




    while not SelectorP1.ready or not SelectorP2.ready:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        updateTerrain()
        updateReadyPlayers()

        # === Color choice ===
        player1Color, SelectorP1Rect=ColorChoice("1", SelectorP1Rect)
        player2Color, SelectorP2Rect=ColorChoice("2", SelectorP2Rect)
        # ===

        pygame.display.update()
        fpsClock.tick(fpsClock_value)

    return player1Color, player2Color

