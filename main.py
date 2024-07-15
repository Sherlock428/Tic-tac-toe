

def exibirtabela(tab):
    
    print(f"""
{tab[0]} | {tab[1]} | {tab[2]}
{'-' * 10}
{tab[3]} | {tab[4]} | {tab[5]}
{'-' * 10}
{tab[6]} | {tab[7]} | {tab[8]}""")
    
def jogadorinput(tab, player):

    while True:
        try:
            inp = int(input("Escolha um número de 1 a 9: "))

            if inp >= 1 and inp <= 9 and tab[inp - 1] == "-":
                tab[inp - 1] = player
                break

            else:
                print("ERRO: escolha uma posição vazia")
        
        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido")

def checkwin(tab):
    #horizontal
    if tab[0] == tab[1] == tab[2] != "-":
        return True
    elif tab[3] == tab[4] == tab[5] != "-":
        return True
    elif tab[6] == tab[7] == tab[8] != "-":
        return True
    
    #Vertical

    if tab[0] == tab[3] == tab[6] != "-":
        return True
    if tab[1] == tab[4] == tab[7] != "-":
        return True
    if tab[2] == tab[5] == tab[8] != "-":
        return True
    
    #Diagonal

    if tab[0] == tab[4] == tab[8] != "-":
        return True
    if tab[2] == tab[4] == tab[6] != "-":
        return True

    #Velha

def empate(tab):

    if '-' not in tab:
        print("Deu Velha")
        return True

def trocarjogador(player):
    if player == "X":
        return "O"
    else:
        return "X"
def main():
    player = "X"
    playerXpontos = 0
    playerOpontos = 0
    while True:
        tab = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        while True:
            exibirtabela(tab)
            pinput = jogadorinput(tab, player)
            checkwin(tab)

            if checkwin(tab):
                print(f"Player {player} ganhou")
                if player == "X":
                    playerXpontos += 1
                    print(f"\nPontuação:\n"
                        f"PlayerX: {playerXpontos}\n"
                        f"PlayerO: {playerOpontos}\n")
                    cont = input("Desejar ir mais um partida? (S/N) ").upper()

                    if cont != "S":
                        return
                    else:
                        break
                
                elif player == "O":
                    playerOpontos += 1
                    print(f"\nPontuação:\n"
                        f"PlayerX: {playerXpontos}\n"
                        f"PlayerO: {playerOpontos}\n")
                    cont = input("Desejar ir mais um partida? (S/N) ").upper()

                    if cont != "S":
                        break


            if empate(tab):
                print("acabou")
                break
                

            player = trocarjogador(player)

            

main()