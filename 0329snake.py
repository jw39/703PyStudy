import pygame  #pygame 설치
import time     #time 모듈 호출
import random   #random 모듈 호출
 
pygame.init()      #pygame 초기화

#pygame에 사용되는 전역변수 선언
 
white = (255, 255, 255) #white는
yellow = (255, 255, 102) #yellow는 스코어의 글자색
black = (0, 0, 0)   #black은 뱀 색
red = (213, 50, 80) #red는 종료 안내 문자 색
green = (0, 255, 0) #green은 사과 색
blue = (50, 153, 213) #blue는 배경색
#게임에서 사용되는 색깔들을 RGB 형태로 정의
 
dis_width = 600 #가로는 600
dis_height = 400 #세로는 400
#화면의 가로와 세로 크기를 정의
 
dis = pygame.display.set_mode((dis_width, dis_height)) #dis width,height 설정한 값으로 지정 //화면에 대한 변수pygame의 display 가져옴
pygame.display.set_caption('Snake Game by Edureka')
#화면을 생성하고 타이틀을 정의
 
clock = pygame.time.Clock() #게임 루프 내에서 사용될 시계를 생성 #import time 과 다름 pygame안에 있는 time //중첩의 개념
snake_block = 10
snake_speed = 15 #뱀 블록의 크기와 뱀의 이동 속도를 정의
 
font_style = pygame.font.SysFont("bahnschrift", 25) #죽으면 나오는 글씨 폰트
score_font = pygame.font.SysFont("comicsansms", 35) #점수를 나타내는 글씨 폰트
 
 
def Your_score(score): #사용자 함수(Your_score) 만든 것
    value = score_font.render("Your Score: " + str(score), True, yellow)  #true는 render하겠다는 의미, yellow는 글씨 색상
    dis.blit(value, [0, 0]) #점수를 화면에 출력하는 함수 //위에 value를 0,0 좌표 위에 찍겠다
 
 
 
def our_snake(snake_block, snake_list): #사용자 함수(our_snake) 만든 것, 블록, 리스트 
    for x in snake_list: #snake_list값만큼 반복
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) 
        #뱀을 그리는 함수 //display 공간에 black색으로 x값 사이즈의 snake block 생성할 거다
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3]) #게임 오버 메시지를 출력하는 함수
 
 
def gameLoop(): #함수 gameLoop를 정의
    game_over = False
    #변수 game_over는 게임이 끝났는지 나타내는 부울 변수 
    #초기값은 False이며, 게임이 끝나면 True로 설정.
    game_close = False
    #게임이 종료되는지 여부를 나타내는 또 다른 부울 변수, 초기값은 False이며, 
    # 게임이 종료되면 True로 설정

 
    x1 = dis_width / 2
    y1 = dis_height / 2
    # x1과 y1은 뱀의 머리 위치를 나타내는 변수 
    # dis_width와 dis_height는 게임 화면의 너비와 높이를 나타내는 변수 
    # 이 변수를 사용하여 뱀이 화면 내에서 이동할 수 있음
 
    x1_change = 0
    y1_change = 0
    # 뱀의 이동 방향을 나타내는 변수. 이 변수를 사용하여 뱀의 이동 방향을 제어

 
    snake_List = []
    Length_of_snake = 1
    # snake_List는 뱀의 몸통 위치를 저장하는 리스트 
    # Length_of_snake는 뱀의 길이를 나타내는 변수,  뱀의 초기 길이를 1로 설정(10*10)
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    #foodx와 foody는 음식의 위치를 나타내는 변수 
    # 이 변수는 random.randrange 함수를 사용하여 먹이의 x좌표오와 y좌표를 무작위로 설정
 
 
    #게임 루프는 while문으로 구현되며, 게임이 종료되거나 닫히지 않는 한 계속 실행 
    # 내부 while문은 게임이 종료되었는지 확인하고, 게임이 종료되면 반복을 중지
    while not game_over:
     #게임이 끝나지 않았다면 반복

 
        while game_close == True: # 게임이 오버된 경우, 게임 오버 화면을 출력하고 키보드 이벤트를 대기

            dis.fill(blue) #화면을 파란색으로 채움
            message("You Lost! Press C-Play Again or Q-Quit", red) # 메시지를 출력
            Your_score(Length_of_snake - 1) #현재 점수를 출력
            pygame.display.update() #변경된 화면을 업데이트
 
            for event in pygame.event.get(): #이벤트를 처리
                if event.type == pygame.KEYDOWN: #키보드 이벤트가 발생한 경우 처리
                    if event.key == pygame.K_q: #Q키를 누른 경우, 게임 종료.
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c: # C키를 누른 경우, 게임 재시작
                        gameLoop()
 
        for event in pygame.event.get(): #이벤트를 처리
            if event.type == pygame.QUIT: #창을 닫는 이벤트가 발생한 경우, 게임 종료.
                game_over = True
            if event.type == pygame.KEYDOWN: #방향키에 따라 뱀의 이동 방향이 결정
                if event.key == pygame.K_LEFT:#왼쪽
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #오른쪽
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP: #위
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN: #아래
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True 
            #뱀의 머리가 화면 밖으로 나갔을 때 게임 오버 상태
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue) #화면을 파란색으로 채움
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #초록색 사각형 생성  //먹이를 생성
        #뱀 추가 코드
        snake_Head = []
        snake_Head.append(x1)   #바뀐 값을 head값에 넣고 list에 넣고,,,?
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        # 뱀의 좌표를 저장하는 리스트에 머리 좌표 생성
        
 
        for x in snake_List[:-1]: #거꾸로 출력 //맨 오른쪽 값을 제외하고 출력       [start:end]
            if x == snake_Head:
                game_close = True
        #자신의 몸과 충돌했을 때 게임 오버 상태가 됨
 
        our_snake(snake_block, snake_List) #def
        Your_score(Length_of_snake - 1) #현재 점수를 출력
 
        pygame.display.update()
        # 현재 점수를 표시하는 역할
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            # 먹이를 먹었을 때 뱀의 길이를 증가시키고, 새로운 먹이를 생성
 
        clock.tick(snake_speed) # 게임 속도를 조절
 
    pygame.quit()
    quit()
 
 
gameLoop() # 함수 

#한꺼번에 사과 여러개, 여러 스테이지, 이미지 첨부