import random 
import pygame

screen_w=960
screen_h=720

color_b=(0,0,0)
color_w=(255,255,255)

def main():
    pygame.init()
    screen=pygame.display.set_mode((screen_w,screen_h))
    
    pygame.display.set_caption("Pong Pong")


                
    paddle_1_rect=pygame.Rect(30,0,7,100)
    paddle_2_rect=pygame.Rect(screen_w-50,0,7,100)

    pad1_mov=0
    pad2_mov=0

    ball=pygame.Rect(screen_w/2,screen_h/2,25,25)

    ball_acc_x=random.randint(2,4)*0.1
    ball_acc_y=random.randint(2,4)*0.1


    if random.randint(1,2)==1:
        ball_acc_x*= -1
    if random.randint(1,2)==1:
        ball_acc_y*= -1

    
    clock = pygame.time.Clock()
        
    game_over=True
    
    
    
    while True:
        screen.fill(color_b)
        
        
        if game_over:
            font=pygame.font.SysFont("Times New Roman",30)
            text = font.render('Press space to start',True,color_w)
            text_rect=text.get_rect()
            text_rect.center=(screen_w//2,screen_h//2)
            screen.blit(text,text_rect)
            
            pygame.display.flip()
            
            clock.tick(60)
            
            
        delta_time=clock.tick(60)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                return
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_SPACE and game_over:
                    #started=True
                    game_over= False
                    
                    ball.left,ball.top= screen_w//2,screen_h//2
                    
                    ball_acc_x =random.choice([-1,1])* 0.3
                    ball_acc_y =random.choice([-1,1]) *0.3
                    
                    paddle_1_rect.top =screen_w//2 - paddle_1_rect.height//2
                    paddle_2_rect.top =screen_w//2 - paddle_2_rect.height//2
            if event.type == pygame.KEYDOWN:
                #player 1
                if event.key == pygame.K_w:
                    pad1_mov= -0.5
                
                if event.key == pygame.K_s:
                    pad1_mov= 0.5
                #player 2
                if event.key == pygame.K_UP:
                    pad2_mov= -0.5
                
                if event.key == pygame.K_DOWN:
                    pad2_mov= 0.5

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_w or event.key==pygame.K_s:
                    pad1_mov= 0.0
                    
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pad2_mov=0.0
                
        paddle_1_rect.top+= pad1_mov *delta_time
        paddle_2_rect.top+= pad2_mov *delta_time
        
        
        
                    
        
        if paddle_1_rect.top<0:
            paddle_1_rect.top=0
        if paddle_1_rect.bottom> screen_h:
            paddle_1_rect.bottom = screen_h
        
        if paddle_2_rect.top<0:
            paddle_2_rect.top=0
        if paddle_2_rect.bottom >screen_h:
            paddle_2_rect.bottom = screen_h    
            
            
                    
        
        if ball.left <=0 or ball.left >=screen_w:
            game_over=True
            #return
        if ball.top<0:
            ball_acc_y *= -1
            ball.top = 0
        
        if ball.bottom >= screen_h :
            ball_acc_y *= -1
            ball.bottom=screen_h 
            
            
        if paddle_1_rect.colliderect(ball) and paddle_1_rect.left < ball.left:
            ball_acc_x *=-1
            ball.left += 4
        if paddle_2_rect.colliderect(ball) and paddle_2_rect.left >ball.left:
            ball_acc_x *= -1
            ball.left -= 4
            
        if not game_over:
            ball.left+=ball_acc_x * delta_time
            ball.top+=ball_acc_y * delta_time
        

        pygame.draw.rect(screen,color_w,paddle_1_rect)
        pygame.draw.rect(screen,color_w,paddle_2_rect)
        
        pygame.draw.rect(screen,color_w,ball)
        
        pygame.display.update()
        
        
if __name__== "__main__":
        main()  
        
        
        