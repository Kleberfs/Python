opcao = int(input('''0-Xtudo
1-Xegg
2-Xbacon 
3-Xsalada 
4-Batata Frita 
5-Refri0gerante'''))
print("\n0-Xtudo \n1-Xegg \n2-Xbacon \n3-Xsalada \n4-Batata Frita \n5-Refrigerante")
cardapio=["Xtudo","Xegg","Xbacon","Xsalada","BatataFrita","Refrigerante"]
preço=[17,14,15,13,9,6]
print("Pedido")
pedido=int(input("Escolha um lanche:"))
quantidade=int(input("Quantidade:"))
print(quantidade*preço)
