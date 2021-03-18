class No:  
  
	def __init__(self, dado, right, left):
		self.dado = dado
		self.right = right
		self.left = left

class Arvore:
		
	def __init__(self):                         #dado iniciado como none
	#	self.raiz = No(None, None, None)    #se existir, recebe valor
		self.raiz = None

#Essa função vai inserir elementos na árvore, checando seus nós esquerdos e direitos
	def inserir(self, valor):
		new_no = No(valor, None, None)
		if self.raiz == None:         #se a arvore nao foi iniciada
			self.raiz = new_no 
		else:
			atual = self.raiz
			while atual is not None:
				anterior = atual
				if valor == atual.dado:
					print("elemento {0} já existe" .format(valor))
					break
				
				if valor <= atual.dado:            #checa o valor p esquerda
					atual = atual.left
					if atual == None:      #se não existir no a esquerda
						anterior.left = new_no
				else:
					atual = atual.right       #checa o valor p direita
					if atual == None:
						anterior.right = new_no    #se não existir no a direita
	
	def remover(self, valor, raiz):
		if raiz is None:
			print("Arvore vazia")
			return raiz

		if valor == raiz.dado:
			if raiz.left is None and raiz.right is None:   #1° Caso: nó folha
				print("entrou 1° caso de remoção")
				return None
			elif raiz.left is None:                      #2° Caso: nó com 1 filho
				print("entrou 2° caso de remoção / retorna dir")
				return raiz.right
			elif raiz.right is None:
				print("entrou 2° caso de remoção / retorna esq")
				return raiz.left
			else:	                                     #3° Caso: nó com 2 filhos
				anterior = raiz.right
				atual = raiz.right
				while (atual is not None):
					anterior = atual
					atual = atual.left
				    
				raiz.dado = anterior.dado         #o no deletado vai ter seu valor substituido
				raiz.right = self.remover(raiz.dado, raiz.right)    #é aplicado o metodo de remoção p/ deletar o nó
				return raiz                                         #usado para a substituição

		elif valor < raiz.dado:          #percorrendo a arvore 
			raiz.left = self.remover(valor, raiz.left)	
		elif valor > raiz.dado:
			raiz.right = self.remover(valor, raiz.right)

		return raiz
					
	def inorder(self, raiz):
		if self.raiz == None:
			return 0
		elif(raiz != None):
			self.inorder(raiz.left)
			print(raiz.dado)
			self.inorder(raiz.right)
	
	def percorre(self):
		self.inorder(self.raiz)
	
	def remov(self, valor):
		self.remover(valor, self.raiz) 


arvo = Arvore()

raiz = arvo.inserir(8)
arvo.inserir(5)
arvo.inserir(10)
arvo.inserir(7)
arvo.inserir(9)
arvo.inserir(3)
arvo.inserir(6)
arvo.inserir(15)
arvo.inserir(20)
arvo.inserir(12)
arvo.inserir(3)
arvo.inserir(4)
arvo.inserir(2)

print("Árvore pós inserção")
arvo.percorre()
print(" ")
arvo.remov(5)
print("Árvore pós remoção")
arvo.percorre()


