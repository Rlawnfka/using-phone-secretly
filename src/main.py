import pygame
import sys
import os

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("선생님 몰래 폰하기")

# 색상
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
BLUE = (100,149,237)

# 폰트 파일 경로
font_Bold = os.path.join(os.path.dirname(__file__),"..","assets","Fonts","VITRO_Font_OTF","VITRO_Font_OTF","VITRO CORE OTF.otf")
font_Regular = os.path.join(os.path.dirname(__file__),"..","assets","Fonts","VITRO_Font_OTF","VITRO_Font_OTF","VITRO CORE OTF.otf")
font_Light = os.path.join(os.path.dirname(__file__),"..","assets","Fonts","VITRO_Font_OTF","VITRO_Font_OTF","VITRO CORE OTF.otf")

title_font = pygame.font.Font(font_Bold, 60)
button_font = pygame.font.Font(font_Regular,30)

title_text = title_font.render("선생님 몰래 폰하기 !!", True, BLACK)
startBtn_text = button_font.render("게임 시작", True, WHITE)

startBtn_rect = pygame.Rect(300,250,200,60)

# 메인 루프
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN : 
            if startBtn_rect.collidepoint(event.pos):
                pass 

    # 화면 색상 채우기
    screen.fill(WHITE)

    # 타이틀
    screen.blit(title_text,(140,80))
    
    pygame.draw.rect(screen,BLUE,startBtn_rect)
    text_rect = startBtn_text.get_rect(center=startBtn_rect.center)
    screen.blit(startBtn_text, text_rect)

    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
