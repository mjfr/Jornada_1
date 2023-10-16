# import pygame
# import sys
#
# # Iniciando o PyGame
# pygame.init()
#
# # Setando a janela e sua resolução da janela
# screen = pygame.display.set_mode([800, 600])
#
# # Objeto fonte para escrita em tela
# base_font = pygame.font.Font(None, 32)
# user_text = ''
#
# # Cor para separar quando o objeto quando selecionado
# color_activated = pygame.Color('lightskyblue3')
# color_deactivated = pygame.Color('crimson')
# color = color_deactivated
#
# # Booleans
# # Se o objeto for clicado, active = True
# active = False
# # Ao salvar o nome, saved = True
# saved = False
#
# # Offset do texto para posição no input
# text_offset = 0
#
# # Loop principal
# while True:
#     # Obtendo eventos que ocorrem no jogo
#     for event in pygame.event.get():
#         # Ao clicar no X da janela, fecha o processo do pygame e fecha o processo do python
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#
#         # Pressionar uma tecla enquanto o objeto for selecionado, captura a tecla pressionada até o limite de caractere
#         if event.type == pygame.KEYDOWN and active:
#             # Faz com que a string seja igual a si mesma menos sua última posição
#             if event.key == pygame.K_BACKSPACE:
#                 user_text = user_text[:-1]
#                 # Adiciona na string o caractere capturado
#             elif len(user_text) <= 15:
#                 user_text += event.unicode
#
#         # Faz a tela ficar com a cor escolhida
#         screen.fill((255, 255, 255))
#
#         # Altera a cor do objeto dependendo do seu estado (selecionado ou não)
#         if active:
#             color = color_activated
#         else:
#             color = color_deactivated
#
#         # Renderiza o texto escrito pelo usuário
#         text_surface = base_font.render(user_text, True, (255, 255, 255))
#         # Renderiza o texto do botão fixo
#         continue_surface = base_font.render('Continuar', True, (255, 255, 255))
#
#         # Se o nome não for salvo:
#         if not saved:
#             # Criando retângulos e seus posicionamentos e tamanhos em tela
#             input_rect = pygame.Rect(350, 200, 150, 40)
#             save_rect = pygame.Rect(350, 300, 150, 40)
#
#             # Ao clicar no botão, seu estado é alterado (selecionado)
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if input_rect.collidepoint(event.pos):
#                     active = True
#                 else:
#                     active = False
#
#             # Desenha os retângulos em tela
#             pygame.draw.rect(screen, color, input_rect)
#             pygame.draw.rect(screen, color_deactivated, save_rect)
#
#             # Calcula o offset do texto a partir de uma comparação de largura entre o texto e o retângulo
#             if text_surface.get_width() > input_rect.w:
#                 # O offset é calculado pela largura do texto menos a largura do retângulo, adiciona-se 20 para que o
#                 # final do texto não fique cortado
#                 text_offset = text_surface.get_width() - input_rect.w + 20
#             else:
#                 # Reseta o offset para zero caso apague o texto
#                 text_offset = 0
#
#             # Desenhando o texto na superfície escolhida
#             screen.blit(text_surface, (input_rect.x+10 - text_offset, input_rect.y+5))
#             # Centralizando o texto
#             screen.blit(continue_surface, (save_rect.x + (save_rect.w - continue_surface.get_width()) // 2,
#                                            save_rect.y+5))
#
#             # Setando a largura máxima do retângulo
#             input_rect.w = max(200, text_surface.get_width()+10)
#             save_rect.w = max(120, text_surface.get_width()+10)
#             # Se o nome possuir um ou mais caracteres
#             if event.type == pygame.MOUSEBUTTONDOWN and len(user_text) > 0:
#                 # se a posição em que o cursor do mouse clicado for o botão de salvar:
#                 if save_rect.collidepoint(event.pos):
#                     # Apenas por testes: abrindo um arquivo no modo append
#                     with open(file='save.csv', mode='a+', encoding='utf-8') as file:
#                         print('aaa')
#                         # Salvando o nome escrito pelo usuário e formatando o csv para primeiro uso e posteriores
#                         file.write(f'{"Nome" if file.tell() == 0 else ""}\n{user_text}')
#                         # Setando saved para True para que as variáveis save_rect e input_rect não sejam mais utilizadas
#                         saved = True
#                         # Deletando as variáveis (tratadas pelo gc e em tela elas não aparecem mais)
#                         # Embora, não seja necessário
#                         # del save_rect
#                         # del input_rect
#
#         # Atualiza a tela
#         pygame.display.flip()
