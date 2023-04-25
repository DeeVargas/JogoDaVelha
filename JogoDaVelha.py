import os
tabuleiro = [[1 ,  2 ,  3 ],
            [4 ,  5 ,  6 ] ,
            [7 ,  8 ,  9 ]]

lista = [
    [0, 0],  [0, 1], [0, 2],
    [1, 0],  [1, 1], [1, 2],
    [2, 0],  [2, 1], [2, 2]]

def reiniciar_tabuleiro():
    posicao = 1
    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = posicao 
            posicao += 1



def menu():
    reiniciar_tabuleiro()
    continuar = 0
    while continuar != 2:
        continuar = int(input("1. JOGAR NOVAMENTE \n"+
                              "2. SAIR\n"))
        if continuar == 1:
            os.system('cls' if os.name == 'nt' else 'clear') 
            game()
        elif continuar != 2:
            print(continuar)
        else:
            print("Saindo...")
        break

    
def vencedor():
    vencedor = False
    jogador = None

    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]:
        vencedor = True
        jogador = tabuleiro[0][0]
    if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]:
        vencedor = True
        jogador = tabuleiro[0][0]
    if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]:
        vencedor = True
        jogador = tabuleiro[0][0]
    if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]:
        vencedor = True
        jogador = tabuleiro[0][0]
    if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]:
        vencedor = True
        jogador = tabuleiro[0][1]
    if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]:
        vencedor = True
        jogador = tabuleiro[0][2]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]:
        vencedor = True
        jogador = tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]:
        vencedor = True
        jogador = tabuleiro[0][2]    
    
    if vencedor: 
        print(f"Parabéns jogador {jogador}, você é o vencedor da rodada!\n")
        return vencedor
    else:
        for i in range(3):
            for j in range(3):
                if isinstance(tabuleiro[i][j], int):
                    return False 
        print("EMPATE!\n")
        return True


def game():
    jogador1 = "X"
    jogador2 = "O"
    ganhador = False
    print("┌───┬───┬───┐")
    print(f"| {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} |")
    print("├───┼───┼───┤")
    print(f"| {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} |")
    print("├───┼───┼───┤")
    print(f"| {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} |")
    print("└───┴───┴───┘")
    print()

    posicoes_validas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while not ganhador:
        valido = False
        while not valido:
            p1 = int(input("\nJogador 1, escolha a posição da sua jogada: "))
            p1 = p1 - 1
            if p1 + 1 not in posicoes_validas:
                print('\nTente novamente com os números disponíveis no tabuleiro.')
                continue
            else:
                posicoes_validas.remove(p1 + 1)
                posicao = lista[p1]
                tabuleiro[posicao[0]][posicao[1]] = jogador1
                print("┌───┬───┬───┐")
                print(f"| {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} |")
                print("├───┼───┼───┤")
                print(f"| {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} |")
                print("├───┼───┼───┤")
                print(f"| {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} |")
                print("└───┴───┴───┘")
                print()
                break

        ganhador = vencedor()
        if ganhador:
            break
        
        valido = False
        while not valido:
            p2 = int(input("\nJogador 2, escolha a posição da sua jogada: "))
            p2 = p2 - 1
            if p2 + 1 not in posicoes_validas:
                print('\nTente novamente com os números disponíveis no tabuleiro.')
                continue
            else:
                posicoes_validas.remove(p2 + 1)
                posicao = lista[p2]
                tabuleiro[posicao[0]][posicao[1]] = jogador2
                print("┌───┬───┬───┐")
                print(f"| {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} |")
                print("├───┼───┼───┤")
                print(f"| {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} |")
                print("├───┼───┼───┤")
                print(f"| {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} |")
                print("└───┴───┴───┘")
                print()
                break

        ganhador = vencedor()
        if ganhador:
            break
    
  
    menu()

game()