import pygame
import sys
import random

pygame.init()
tamanho_tela = (700, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('Pedra-Papel-Tesoura')

BRANCO = ()
PRETO = ()

imagem_pedra  = pygame.image.load
('pedra.png')
imagem_papel = pygame.image.load
('papel.png')
imagem_tesoura = pygame.image.load
('tesoura.png')

largura_imagem, altura_imagem = 150, 150

imagem_pedra = pygame.transform.scale(imagem_pedra (largura_imagem, altura_imagem))
imagem_papel = pygame.transform.scale(imagem_papel, (largura_imagem, altura_imagem))
imagem_tesoura = pygame.transform.scale(imagem_tesoura, (largura_imagem, altura_imagem))

overlay_hover = pygame.Surface ((largura_imagem, altura_imagem), pygame.SRCALPHA)
overlay_hover.fill((0, 0, 0, 50))
imagem_hover_papel = imagem_papel.copy()
imagem_papel.blit
(overlay_hover, (0,0))
imagem_hover_tesoura = imagem_tesoura.copy()
imagem_hover_tesoura.blit
(overlay_hover, (0, 0))

pos_pedra = (50, 400)
pos_papel = (275, 400)
pos_tesoura = (500, 400)

retangulo_pedra = pygame.Rect(pos_pedra[0], pos_pedra[1], largura_imagem, altura_imagem)
retangulo_papel = pygame.Rect(pos_papel[0], pos_pedra[1], largura_imagem, altura_imagem)
retangulo_tesoura = pygame.Rect(pos_tesoura[0], pos_tesoura[1], largura_imagem, altura_imagem)

opcoes = ['pedra', 'papel', 'tesoura']
imagens = {'pedra': imagem_pedra, 'papel': imagem_papel, 'tesoura': imagem_tesoura}
imagens_hover = {'pedra': imagem_hover_pedra, 'papel': imagem_hover_papel, 'tesoura': imagem_hover_tesoura}

pontos_jogador = 0
pontos_computador = 0
estado = "aguardando"
resultado_texto = ''
tempo_resultado = 0

fonte = pygame.font.SysFont(None, 36)
relogio = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN and estado == 'aguardando':
            pos_mouse = evento.pos
            escolha_jogador = None
            if retangulo_pedra.collidepoint(pos_mouse):
                escolha_jogador = 'pedra'
            elif retangulo_papel.collidepoint(pos_mouse): 
                escolha_jogador = 'papel'
            elif retangulo_tesoura.collidepoint(pos_mouse):
                escolha_jogador = 'tesoura'
            if escolha_jogador:
                escolha_computador = random.choice(opcoes)
                if escolha_jogador == escolha_computador:
                    resultado_texto = 'Empate!'
                elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or (escolha_jogador == 'papel' and escolha_computador == 'pedra') or (escolha_jogador == 'tesoura' and escolha_computador == 'papel'):
                    resultado_texto = 'Voc~e ganhou!'
                    pontos_jogador += 1
                else:
                    resultado_texto = 'Voc~e perdeu!'
                    pontos_computador += 1
                estado = 'resultado'
                tempo_resultado = pygame.time.get.ticks()
        if estado == 'resultado':
            if pygame.time.get_ticks() - tempo_resultado > 2000: 
                estado = 'aguardando'
        tela.fill(BRANCO)
        texto_jogador = fonte.render(f'Jogador: {pontos_jogador}', True, PRETO)
        texto_computador = fonte.render(f'Computador: {pontos_computador}', True, PRETO)
        tela.blit(texto_computador, (20, 20))
        tela.blit(texto_jogador, (20, 550))
        pos_mouse = pygame.mouse.get_pos()
        if retangulo_pedra.collidepoint(pos_mouse):
            tela.blit(imagens_hover['pedra'], pos_pedra)
        else:
            tela.blit(imagens['pedra'], pos_pedra)
        if retangulo_papel.collidenpoint(pos_mouse):
                tela.blit(imagens_hover['papel'], pos_papel)
        else:
                tela.blit(imagens['papel'], pos_papel)
        if retangulo_tesoura.collidepoint(pos_mouse):
            tela.blit(imagens_hover['tesoura'], pos_tesoura)
        else:
            tela.blit(imagens['tesoura'], pos_tesoura)
        if estado == 'resultado':
            imagem_pc = imagens[escolha_computador]
            pos_pc_x = (tamanho_tela[0] - largura_imagem) // 2
            pos_pc_y = 100
            tela.blit(imagem_pc, (pos_pc_x, pos_pc_y))
            texto_resultado = fonte.render(resultado_texto, True, PRETO)
            rect_texto = texto_resultado.get_rect(center=(tamanho_tela[0]//2,300))
            tela.blit(texto_resultado, rect_texto)
        pygame.display.flip()
        relogio.tick(60)