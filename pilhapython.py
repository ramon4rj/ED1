import math 

class Node:
    def __init__(self, dado):
    	self.value = dado
    	self.next = None

class Pilha:
	
#Inicia a pilha
    def __init__(self):
    	self.topo = Node(None) #Topo é iniciado como None
    	self.size = 0
    
    #Retorna o tamanho da pilha
    def get_size(self):
    	return self.size
    	
    #Checa se a pilha está vazia
    def is_empty(self):
    	return self.size == 0
    
    #Método de inserção
    def insere_pilha(self, valor):
    	node = Node(valor)
    	node.next = self.topo.next
    	self.topo.next = node
    	self.size += 1
    	
    #Método de remoção 
    def remove_pilha(self):
    	if self.is_empty():
    		print("Pilha vazia")
    	remove = self.topo.next
    	self.topo.next = self.topo.next.next
    	self.size -= 1
    	return remove.value
    
    #Método para imprimir a pilha
    def imprime_pilha(self):
        newnode = self.topo.next
        while(newnode != None):
            print(newnode.value)
            newnode = newnode.next



if __name__ == "__main__":
    p = Pilha()
    for i in range(1, 11):
    	p.insere_pilha(i)
    print("Pós inserção")
    p.imprime_pilha()
    
    for j in range(1, 6):
    	remove = p.remove_pilha()
    
    print("Pós remoção")
    
    p.imprime_pilha()
