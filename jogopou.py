import pygame
import sys
import random

# Inicialização do Pygame
pygame.init()

# Constantes da tela
LARGURA = 400
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pou Escalador")

# Cores
BRANCO = (255, 255, 255)
VERDE = (0, 200, 0)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Jogador
jogador_largura = 50
jogador_altura = 60
jogador_x = LARGURA // 2 - jogador_largura // 2
jogador_y = ALTURA - 150
velocidade_x = 0
velocidade_y = 0
gravidade = 0.5
forca_pulo = -11


imagem_jogador = pygame.image.load("pou.webp").convert_alpha()
imagem_jogador = pygame.transform.scale(imagem_jogador, (jogador_largura, jogador_altura))

# Plataformas (geradas aleatoriamente)
plataformas = [pygame.Rect(300, ALTURA - 40, 200, 20)]
for i in range(6):
    x = random.randint(0, LARGURA - 150)
    y = ALTURA - i * 100 - 100
    plataformas.append(pygame.Rect(x, y, 50, 20))

pontuacao = 0

# Loop principal
while True:
    clock.tick(FPS)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclado — apenas movimento lateral
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jogador_x -= 5
    if teclas[pygame.K_RIGHT]:
        jogador_x += 5

    # Bloquear nas bordas da tela (sem teletransporte)
    if jogador_x < 0:
        jogador_x = 0
    elif jogador_x + jogador_largura > LARGURA:
        jogador_x = LARGURA - jogador_largura

    # Gravidade
    velocidade_y += gravidade
    jogador_y += velocidade_y

    # Criar o retângulo do jogador
    jogador = pygame.Rect(round(jogador_x), round(jogador_y), jogador_largura, jogador_altura)

    # Colisão com plataformas — pulo automático
    if velocidade_y > 0:
        for plataforma in plataformas:
            if jogador.colliderect(plataforma) and jogador.bottom <= plataforma.bottom + 10:
                velocidade_y = forca_pulo
                break

    # Subida (plataformas descem)
    if jogador_y < ALTURA / 3:
        jogador_y += 5
        for p in plataformas:
            p.y += 5
        pontuacao += 1

    # Remove plataformas que saem da tela
    plataformas = [p for p in plataformas if p.y < ALTURA]

    # Cria novas plataformas no topo
    while len(plataformas) < 7:
        x = random.randint(0, LARGURA - 150)
        y = plataformas[-1].y - random.randint(80, 120)
        plataformas.append(pygame.Rect(x, y, 50, 20))

    # Game Over se cair
    if jogador_y > ALTURA:
        print("Game Over! Pontuação:", pontuacao)
        pygame.quit()
        sys.exit()

    # --- Desenhar ---
    TELA.fill(BRANCO)

    # Plataformas
    for p in plataformas:
        pygame.draw.rect(TELA, VERDE, p)

    # 🔹 Desenhar o Pou (imagem)
    TELA.blit(imagem_jogador, (jogador.x, jogador.y))

    # Atualizar tela
    pygame.display.flip()
