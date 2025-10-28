import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Constantes da tela
LARGURA_INICIAL, ALTURA_INICIAL = 600, 400
LARGURA, ALTURA = LARGURA_INICIAL, ALTURA_INICIAL
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERDE_CLARO = (0, 200, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Blocos
TAMANHO_BLOCO = 20

# Relógio
clock = pygame.time.Clock()

# --- Carregar imagens ---
img_cabeca = pygame.image.load("cabeca.png").convert_alpha()
img_cabeca = pygame.transform.scale(img_cabeca, (TAMANHO_BLOCO*1.5, TAMANHO_BLOCO*1.5))

img_maca = pygame.image.load("maca.png").convert_alpha()
img_maca = pygame.transform.scale(img_maca, (TAMANHO_BLOCO*1.5, TAMANHO_BLOCO*1.5))

# Funções
def gerar_fruta(largura, altura):
    x = random.randint(0, (largura - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    y = random.randint(0, (altura - TAMANHO_BLOCO) // TAMANHO_BLOCO) * TAMANHO_BLOCO
    return [x, y]

def desenhar_cobra(cobra, direcao):
    for i, segmento in enumerate(cobra):
        if i == 0:  # cabeça
            if direcao == "CIMA":
                cabeca_rot = pygame.transform.rotate(img_cabeca, 0)
            elif direcao == "BAIXO":
                cabeca_rot = pygame.transform.rotate(img_cabeca, 180)
            elif direcao == "ESQUERDA":
                cabeca_rot = pygame.transform.rotate(img_cabeca, 90)
            elif direcao == "DIREITA":
                cabeca_rot = pygame.transform.rotate(img_cabeca, -90)
            TELA.blit(cabeca_rot, (segmento[0], segmento[1]))
        else:  # corpo
            pygame.draw.rect(TELA, VERDE, pygame.Rect(segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO))

def mostrar_texto(texto, tamanho, cor, pos):
    fonte = pygame.font.SysFont('arial', tamanho)
    txt = fonte.render(texto, True, cor)
    TELA.blit(txt, pos)

def game_over_screen(pontuacao):
    global LARGURA, ALTURA, TELA
    LARGURA, ALTURA = LARGURA_INICIAL, ALTURA_INICIAL
    TELA = pygame.display.set_mode((LARGURA, ALTURA))

    TELA.fill(PRETO)
    mostrar_texto("GAME OVER", 50, VERMELHO, (LARGURA//4, ALTURA//3))
    mostrar_texto(f"Pontuação: {pontuacao}", 36, BRANCO, (LARGURA//3, ALTURA//2))
    mostrar_texto("Pressione R para reiniciar ou Q para sair", 24, BRANCO, (LARGURA//6, ALTURA*2//3))
    pygame.display.flip()
   
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    esperando = False
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Loop principal
def main():
    global LARGURA, ALTURA, TELA

    largura_atual, altura_atual = LARGURA, ALTURA
    cobra = [[100, 100]]
    direcao = 'DIREITA'
    frutas = [gerar_fruta(largura_atual, altura_atual)]
    pontuacao = 0
    velocidade = 10

    while True:
        clock.tick(velocidade)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direcao != 'BAIXO':
                    direcao = 'CIMA'
                elif event.key == pygame.K_DOWN and direcao != 'CIMA':
                    direcao = 'BAIXO'
                elif event.key == pygame.K_LEFT and direcao != 'DIREITA':
                    direcao = 'ESQUERDA'
                elif event.key == pygame.K_RIGHT and direcao != 'ESQUERDA':
                    direcao = 'DIREITA'

        # Mover cobra
        x, y = cobra[0]
        if direcao == 'CIMA':
            y -= TAMANHO_BLOCO
        elif direcao == 'BAIXO':
            y += TAMANHO_BLOCO
        elif direcao == 'ESQUERDA':
            x -= TAMANHO_BLOCO
        elif direcao == 'DIREITA':
            x += TAMANHO_BLOCO

        # Wrap-around
        x %= largura_atual
        y %= altura_atual
        nova_cabeca = [x, y]

        # Colisão com o próprio corpo
        if nova_cabeca in cobra:
            game_over_screen(pontuacao)

        cobra.insert(0, nova_cabeca)

        # Comer frutas
        frutas_comidas = []
        for i, f in enumerate(frutas):
            if nova_cabeca == f:
                pontuacao += 1
                velocidade += 0.3
                frutas_comidas.append(i)

        for i in sorted(frutas_comidas, reverse=True):
            frutas.pop(i)
            frutas.append(gerar_fruta(largura_atual, altura_atual))

        # Crescimento
        if not frutas_comidas:
            cobra.pop()

        # A cada múltiplo de 10 pontos, aumentar tela e adicionar frutas
        if pontuacao > 0 and pontuacao % 10 == 0:
            largura_atual += 100
            altura_atual += 100
            LARGURA, ALTURA = largura_atual, altura_atual
            TELA = pygame.display.set_mode((LARGURA, ALTURA))
            frutas.append(gerar_fruta(largura_atual, altura_atual))
            pontuacao += 1  # evita repetir o aumento

        # Desenhar
        TELA.fill(PRETO)
        desenhar_cobra(cobra, direcao)
        for f in frutas:
            TELA.blit(img_maca, (f[0], f[1]))
        mostrar_texto(f"Pontuação: {pontuacao}", 24, BRANCO, (10, 10))
        pygame.display.flip()

# Tela inicial
TELA.fill(PRETO)
mostrar_texto("SNAKE GAME", 70, VERDE, (LARGURA//9, ALTURA//3))
mostrar_texto("Pressione qualquer tecla para começar", 24, BRANCO, (LARGURA//6, ALTURA//2))
pygame.display.flip()

esperando = True
while esperando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            esperando = False

main()