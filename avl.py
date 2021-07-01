class No:  
  
        def __init__(self, dado):
                self.dado = dado
                self.right = None
                self.left = None
                self.height = 1

class ArvoreAVL:


#Essa função vai inserir elementos na árvore, checando seus nós esquerdos e direitos
        def inserir(self, valor, raiz):
                #new_no = No(valor, None, None)
                if not raiz:         #se a arvore nao foi iniciada
                        #self.raiz = new_no
                        #print(sd)
                        return No(valor)
                else:
                        if valor == raiz.dado:
                                print("elemento {0} já existe" .format(valor))
                                
                        elif valor < raiz.dado:    #percorre o no a esquerda
                                raiz.left = self.inserir(valor, raiz.left)
                    
                        elif valor > raiz.dado:    #percorre o no a direita
                                raiz.right = self.inserir(valor, raiz.right)
                #Atualiza altura
                raiz.height = 1 + max(self.get_height(raiz.left), self.get_height(raiz.right)) 
  
                balance = self.get_balance(raiz) 
        
                #Balanceia o no 
                #Rot simples a direita LL
                if balance > 1 and valor < raiz.left.dado: 
                    return self.rot_right(raiz) 
        
                #Rot simples a esquerda RR
                if balance < -1 and valor > raiz.right.dado: 
                    return self.rot_left(raiz) 
        
                #Rot LR
                if balance > 1 and valor > raiz.left.dado: 
                    raiz.left = self.rot_left(raiz.left) 
                    return self.rot_right(raiz) 
        
                #Rot RL 
                if balance < -1 and valor < raiz.right.dado: 
                    raiz.right = self.rot_right(raiz.right) 
                    return self.rot_left(raiz) 
                                
                return raiz
                                
        def remover(self, valor, raiz):
                if raiz is None:
                        print("Arvore vazia ou No inexistente")
                        return raiz

                if valor == raiz.dado:
                        #if raiz.left is None and raiz.right is None:   #1° Caso: nó folha
                        #        print("entrou 1° caso de remoção")
                        #        return None
                        if raiz.left is None:                      #2° Caso: nó com 1 filho
                                print("entrou 2° caso de remoção / retorna dir")
                                aux = raiz.right
                                raiz = None
                                return aux
                        elif raiz.right is None:
                                print("entrou 2° caso de remoção / retorna esq")
                                return raiz.left
                        else:                                     #3° Caso: nó com 2 filhos
                                anterior = raiz.right
                                atual = raiz.right
                                while (atual is not None):
                                        anterior = atual
                                        atual = atual.left
                                
                                raiz.dado = anterior.dado         #o no deletado vai ter seu valor substituido
                                raiz.right = self.remover(raiz.dado, raiz.right)    #é aplicado o metodo de remoção p/ deletar o nó
                                #return raiz                                         #usado para a substituição

                elif valor < raiz.dado:          #percorrendo a arvore 
                        raiz.left = self.remover(valor, raiz.left)      
                elif valor > raiz.dado:
                        raiz.right = self.remover(valor, raiz.right)
                
                if raiz is None:
                    return raiz
                #Atualiza altura
                raiz.height = 1 + max(self.get_height(raiz.left), self.get_height(raiz.right)) 
   
                balance = self.get_balance(raiz)

                #Rot simples a direita LL
                print("checagem ll")
                if balance > 1 and self.get_balance(raiz.left) >= 0:
                    print("entrou na checagem LL")
                    print(self.get_balance(raiz.left))
                    return self.rot_right(raiz) 
        
                #Rot simples a esquerda RR
                print("checagem RR")
                if balance < -1 and self.get_balance(raiz.right) <= 0: 
                    return self.rot_left(raiz) 
        
                #Rot LR
                print("checagem LR")
                if balance > 1 and self.get_balance(raiz.left) < 0: 
                    print("entrou na checagem LR")
                    print(self.get_balance(raiz.left))
                    #print(sd)
                    raiz.left = self.rot_left(raiz.left) 
                    return self.rot_right(raiz) 
        
                #Rot RL
                print("checagem RL")
                if balance < -1 and self.get_balance(raiz.right) > 0:
                    print("entrou checagem RL")
                    raiz.right = self.rot_right(raiz.right) 
                    return self.rot_left(raiz)
                
                return raiz

        def rot_left(self, z):
                y = z.right
                T2 = y.left
 
                y.left = z
                z.right = T2
 
                #Atualiza altura
                z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
                y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
 
                return y
 
        def rot_right(self, z):
                y = z.left
                T3 = y.right
 
                y.right = z
                z.left = T3
 
                #Atualiza altura
                z.height = 1 + max(self.get_height(z.left), self.get_height(z.right)) 
                y.height = 1 + max(self.get_height(y.left), self.get_height(y.right)) 

                return y
 
        def get_height(self, raiz):
            if not raiz:
                return 0
    
            return raiz.height
    
        def get_balance(self, raiz):
            if not raiz:
                return 0
            
            return self.get_height(raiz.left) - self.get_height(raiz.right)

        def inorder(self, raiz):
                if not raiz:
                    return 
                        #return 0
                elif(raiz != None):
                        self.inorder(raiz.left)
                        print(raiz.dado)
                        self.inorder(raiz.right)

        def preorder(self, raiz):
                if not raiz:
                    return
                elif(raiz != None):
                    print(raiz.dado)
                    self.preorder(raiz.left)
                    self.preorder(raiz.right) 

        def percorre(self):
                #if not raiz:
                #    return
                self.inorder(self.raiz)
        
        def remov(self, valor):
                self.remover(valor, self.raiz) 
        
        def insere(self, valor):
                self.inserir(valor, self.raiz)

        def is_avl(self, raiz):
                balance = self.get_balance(raiz)
                if (balance >= 2) or (balance <= -1 ):
                        print("0")
                        return 0
                else:
                        print("1")
                        return 1


# Ainda é preciso olhar os métodos de rotação ou balanceamento, um dos dois
# ainda não funciona 100%

arvo = ArvoreAVL()                        #inserir : 25 10 8 3 1 5 15 18 16 17 23 30 28 26 27 47
                                          #remover : 26 15 52 8 5

raiz = None 
E1 = [5, 7, 8, 2, 10]
for i in E1:
        raiz = arvo.inserir(i, raiz)



#arvo.is_avl(raiz)

print("Árvore pós inserção: ")
#arvo.inorder(raiz)
arvo.preorder(raiz)
#print("valor a ser removido: ")
arvo.remover(10, raiz)
#arvo.inorder(raiz)
print("Árvore pós remoção")
arvo.preorder(raiz)
#print(do)