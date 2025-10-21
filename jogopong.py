import pygame
import sys

pygame.init()

LARGURA = 1920
ALTURA = 1080
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pong")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

largura_raquete = 15
altura_raquete = 245
velocidade_raquete = 10

tamanho_bola = 30
vel_bola_x = 5.0  # Começa na diagonal
vel_bola_y = 5.0
velocidade_inicial = 5.0

pontuacao_esquerda = 0
pontuacao_direita = 0
fonte = pygame.font.Font(None, 74)

raquete_esquerda = pygame.Rect(50, ALTURA // 2 - altura_raquete // 2, largura_raquete, altura_raquete)
raquete_direita = pygame.Rect(LARGURA - 50 - largura_raquete, ALTURA // 2 - altura_raquete // 2, largura_raquete, altura_raquete)
bola = pygame.Rect(LARGURA // 2 - tamanho_bola // 2, ALTURA // 2 - tamanho_bola // 2, tamanho_bola, tamanho_bola)

primeiro_toque = False

clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()

    if not primeiro_toque:
        # Antes do primeiro toque: livre movimento para ambas raquetes
        if teclas[pygame.K_w] and raquete_esquerda.top > 0:
            raquete_esquerda.y -= velocidade_raquete
        if teclas[pygame.K_s] and raquete_esquerda.bottom < ALTURA:
            raquete_esquerda.y += velocidade_raquete

        if teclas[pygame.K_UP] and raquete_direita.top > 0:
            raquete_direita.y -= velocidade_raquete
        if teclas[pygame.K_DOWN] and raquete_direita.bottom < ALTURA:
            raquete_direita.y += velocidade_raquete

    else:
        # Depois do primeiro toque: controle condicionado ao lado da bola
        if bola.centerx > LARGURA // 2:
            if teclas[pygame.K_w] and raquete_esquerda.top > 0:
                raquete_esquerda.y -= velocidade_raquete
            if teclas[pygame.K_s] and raquete_esquerda.bottom < ALTURA:
                raquete_esquerda.y += velocidade_raquete

        if bola.centerx < LARGURA // 2:
            if teclas[pygame.K_UP] and raquete_direita.top > 0:
                raquete_direita.y -= velocidade_raquete
            if teclas[pygame.K_DOWN] and raquete_direita.bottom < ALTURA:
                raquete_direita.y += velocidade_raquete

    bola.x += int(vel_bola_x)
    bola.y += int(vel_bola_y)

    if bola.top <= 0 or bola.bottom >= ALTURA:
        vel_bola_y *= -1

    if bola.colliderect(raquete_esquerda) or bola.colliderect(raquete_direita):
        vel_bola_x *= -1.1
        vel_bola_y *= 1.05
        primeiro_toque = True

        max_vel = 20
        vel_bola_x = max(min(vel_bola_x, max_vel), -max_vel)
        vel_bola_y = max(min(vel_bola_y, max_vel), -max_vel)

    if bola.left <= 0:
        pontuacao_direita += 1
        bola.center = (LARGURA // 2, ALTURA // 2)
        vel_bola_x = -velocidade_inicial
        vel_bola_y = velocidade_inicial
        primeiro_toque = False

    if bola.right >= LARGURA:
        pontuacao_esquerda += 1
        bola.center = (LARGURA // 2, ALTURA // 2)
        vel_bola_x = velocidade_inicial
        vel_bola_y = velocidade_inicial
        primeiro_toque = False

    tela.fill(PRETO)
    pygame.draw.rect(tela, BRANCO, raquete_esquerda)
    pygame.draw.rect(tela, BRANCO, raquete_direita)
    pygame.draw.ellipse(tela, BRANCO, bola)
    pygame.draw.aaline(tela, BRANCO, (LARGURA // 2, 0), (LARGURA // 2, ALTURA))

    player1 = fonte.render("Player 1", True, BRANCO)
    player2 = fonte.render("Player 2", True, BRANCO)
    tela.blit(player1, (LARGURA // 4.7, 50))
    tela.blit(player2, (LARGURA * 3.55 // 5, 50))

    texto_esquerda = fonte.render(str(pontuacao_esquerda), True, BRANCO)
    texto_direita = fonte.render(str(pontuacao_direita), True, BRANCO)
    tela.blit(texto_esquerda, (LARGURA // 4, 10))
    tela.blit(texto_direita, (LARGURA * 3 // 4, 10))

    pygame.display.flip()
    clock.tick(60)