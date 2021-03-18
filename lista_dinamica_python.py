import math  
    
# no, lista encadeada    
class Node:   

    def __init__(self, data):  
        self.data = data   
        self.next = None

class LinkedList: 

    def __init__(self):  
        self.head = None
    
# FUNÇÕES
    
# inserir um nó no inicio da lista    
    def push(self, new_data): 
        #Aloca o no em data
        
        new_node = Node(new_data) 

        #Campo next do newnode recebe head

        new_node.next = self.head 
        #Head aponta para newnode
        #print(sd)

        self.head = new_node 

    def insertAfter(self, ant, new_data):  
  
        # Checa a existência do nó
        if ant is None:
            print(" ")
            print ("No anterior não está na lista")
            return
    
        # Cria novo nó &  
        # o coloca em data
        new_node = Node(new_data)  
    
        # Coloca no campo next do new_node o next do node anterior
        new_node.next = ant.next
    
        # Coloca no campo next do node aterior o new_node 
        ant.next = new_node

    def append(self, new_data):
        #Aloca o no em data
        new_node = Node(new_data)

        #Se o for o primeiro no, insere
        if self.head is None:
            self.head = new_node
            return
        else:  #Percorre a lista pela direita ate o ultimo no
            tail = self.head
            while(tail.next is not None):
                tail = tail.next
            
            tail.next = new_node

    def remove(self, value):
        aux = self.head
        #Caso o no head seja o valor a ser apagado
        if aux is not None:
            if aux.data == value:
                self.head = aux.next
                aux = None
                return
        
        #Procura o no
        while aux is not None:
            if aux.data == value:
                break
            prev = aux
            aux = aux.next
        
        #Se aux percorreu a lista e não chegou a encontrar o valor, ou seja
        #aux == None, então o valor não está na lista
        if aux == None:
            print(" ")
            print("Valor não está na lista")
            return

        #Atualiza os ponteiros após a saída do while
        prev.next = aux.next
        aux = None
    
# Printar o nó    
    def printList(self, node):   
    
        while (node != None):   
            print(node.data, end = " ")   
            node = node.next

    def show_list(self):
        self.printList(self.head)

l = LinkedList()
node = l.push(1)
node = l.push(5)
node = l.push(8)
node = l.insertAfter(l.head, 2)
#node = l.insertAfter(l.head.next, 2)
print("Pós inserção: ")

l.show_list()

#l.remove(2)
#l.remove(8)
l.remove(7)
print(" ")
print("Pós remoção: ")

l.show_list()
