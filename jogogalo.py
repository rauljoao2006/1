import pygame
import sys

pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
VERDE_CLARO = (180, 255, 180)

LARGURA = 600
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Super Jogo do Galo")

fonte = pygame.font.SysFont("Arial", 30)
fonte_grande = pygame.font.SysFont("Arial", 80)

TAMANHO_CELULA = LARGURA // 3
TAMANHO_MINI_CELULA = TAMANHO_CELULA // 3

class MiniTabuleiro:
    def __init__(self):
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.vencedor = None
        self.completo = False

    def jogar(self, linha, coluna, jogador):
        if self.tabuleiro[linha][coluna] == "" and not self.completo:
            self.tabuleiro[linha][coluna] = jogador
            self.verificar_vitoria()
            return True
        return False

    def verificar_vitoria(self):
        t = self.tabuleiro
        for i in range(3):
            if t[i][0] == t[i][1] == t[i][2] != "":
                self.vencedor = t[i][0]
                self.completo = True
                return
            if t[0][i] == t[1][i] == t[2][i] != "":
                self.vencedor = t[0][i]
                self.completo = True
                return
        if t[0][0] == t[1][1] == t[2][2] != "":
            self.vencedor = t[0][0]
            self.completo = True
            return
        if t[0][2] == t[1][1] == t[2][0] != "":
            self.vencedor = t[0][2]
            self.completo = True
            return
        if all(cell != "" for row in t for cell in row):
            self.completo = True

tabuleiro_principal = [[MiniTabuleiro() for _ in range(3)] for _ in range(3)]

jogador_atual = "X"
mini_ativo = None
jogo_encerrado = False
vencedor_geral = None

def verificar_vitoria_principal():
    global vencedor_geral, jogo_encerrado
    t = [[mini.vencedor for mini in linha] for linha in tabuleiro_principal]
    for i in range(3):
        if t[i][0] == t[i][1] == t[i][2] != None:
            vencedor_geral = t[i][0]
            jogo_encerrado = True
            return
        if t[0][i] == t[1][i] == t[2][i] != None:
            vencedor_geral = t[0][i]
            jogo_encerrado = True
            return
    if t[0][0] == t[1][1] == t[2][2] != None:
        vencedor_geral = t[0][0]
        jogo_encerrado = True
        return
    if t[0][2] == t[1][1] == t[2][0] != None:
        vencedor_geral = t[0][2]
        jogo_encerrado = True
        return
    if all(mini.completo for row in tabuleiro_principal for mini in row):
        vencedor_geral = None
        jogo_encerrado = True

def reiniciar_jogo():
    global tabuleiro_principal, jogador_atual, mini_ativo, jogo_encerrado, vencedor_geral
    tabuleiro_principal = [[MiniTabuleiro() for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    mini_ativo = None
    jogo_encerrado = False
    vencedor_geral = None

def desenhar_tabuleiro():
    TELA.fill(BRANCO)
    for i in range(3):
        for j in range(3):
            x_offset = j * TAMANHO_CELULA
            y_offset = i * TAMANHO_CELULA
            if mini_ativo is None:
                if not tabuleiro_principal[i][j].completo:
                    pygame.draw.rect(TELA, VERDE_CLARO, (x_offset, y_offset, TAMANHO_CELULA, TAMANHO_CELULA))
            elif mini_ativo == (i, j):
                pygame.draw.rect(TELA, VERDE_CLARO, (x_offset, y_offset, TAMANHO_CELULA, TAMANHO_CELULA))
            for m in range(1, 3):
                pygame.draw.line(TELA, PRETO,
                                 (x_offset + m * TAMANHO_MINI_CELULA, y_offset),
                                 (x_offset + m * TAMANHO_MINI_CELULA, y_offset + TAMANHO_CELULA), 1)
                pygame.draw.line(TELA, PRETO,
                                 (x_offset, y_offset + m * TAMANHO_MINI_CELULA),
                                 (x_offset + TAMANHO_CELULA, y_offset + m * TAMANHO_MINI_CELULA), 1)
            mini = tabuleiro_principal[i][j]
            for mi in range(3):
                for mj in range(3):
                    marca = mini.tabuleiro[mi][mj]
                    if marca != "":
                        texto = fonte.render(marca, True, AZUL if marca == "X" else VERMELHO)
                        pos_x = x_offset + mj * TAMANHO_MINI_CELULA + TAMANHO_MINI_CELULA // 2 - texto.get_width() // 2
                        pos_y = y_offset + mi * TAMANHO_MINI_CELULA + TAMANHO_MINI_CELULA // 2 - texto.get_height() // 2
                        TELA.blit(texto, (pos_x, pos_y))
            if mini.vencedor:
                marca = mini.vencedor
                texto = fonte_grande.render(marca, True, AZUL if marca == "X" else VERMELHO)
                TELA.blit(texto, (x_offset + TAMANHO_CELULA // 2 - texto.get_width() // 2,
                                  y_offset + TAMANHO_CELULA // 2 - texto.get_height() // 2))
    for i in range(1, 3):
        pygame.draw.line(TELA, PRETO, (0, i * TAMANHO_CELULA), (LARGURA, i * TAMANHO_CELULA), 5)
        pygame.draw.line(TELA, PRETO, (i * TAMANHO_CELULA, 0), (i * TAMANHO_CELULA, ALTURA), 5)
    if jogo_encerrado:
        msg = "Empate!" if vencedor_geral is None else f"{vencedor_geral} venceu!"
        texto = fonte.render(msg + " – Clique para reiniciar", True, PRETO)
        TELA.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - texto.get_height() // 2))

while True:
    desenhar_tabuleiro()
    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if jogo_encerrado:
                reiniciar_jogo()
                continue
            x, y = pygame.mouse.get_pos()
            linha = y // TAMANHO_CELULA
            coluna = x // TAMANHO_CELULA
            if mini_ativo is None:
                if not tabuleiro_principal[linha][coluna].completo:
                    mini_ativo = (linha, coluna)
                else:
                    continue
            else:
                if (linha, coluna) != mini_ativo:
                    continue
                mini = tabuleiro_principal[mini_ativo[0]][mini_ativo[1]]
                mini_x = x - mini_ativo[1] * TAMANHO_CELULA
                mini_y = y - mini_ativo[0] * TAMANHO_CELULA
                mi = mini_y // TAMANHO_MINI_CELULA
                mj = mini_x // TAMANHO_MINI_CELULA
                if mini.jogar(mi, mj, jogador_atual):
                    verificar_vitoria_principal()
                    proximo = (mi, mj)
                    if proximo[0] < 0 or proximo[0] > 2 or proximo[1] < 0 or proximo[1] > 2:
                        mini_ativo = None
                    elif tabuleiro_principal[proximo[0]][proximo[1]].completo:
                        mini_ativo = None
                    else:
                        mini_ativo = proximo
                    jogador_atual = "O" if jogador_atual == "X" else "X"