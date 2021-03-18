
class HashTable:
    def __init__(self):
        self.table_size = 10
        self.array = [None] * self.table_size

    def hashDivisao(self, key):
        key = self.get_hash(key)
        return (key & int(0x7FFFFFFF)) % self.table_size
        #return key % table_size

    def tratamento_colisoes(self, pos, i):
        return ((pos + (i+3)) & 0x7FFFFFFF) % self.table_size
    
    def insere_tratamento_colisao(self, key, valor):
        pos = self.hashDivisao(key) 
        for i in range(self.table_size + 1):
            newpos = self.tratamento_colisoes(pos, i)
            if self.array[newpos] == None:   #se a posição obtida for vazia
                newval = valor
                self.array[newpos] = valor
                break
                return newval

    def busca_tratamento_colisao(self, key, valor):    #Busca e retorna a posição do elemento desejado
        pos = self.hashDivisao(key)
        for i in range(self.table_size + 1):
            newpos = self.tratamento_colisoes(pos, i)

            if self.array[newpos] == None:     
                return 0                       
            if self.array[newpos] == valor:      
                newval = self.array[newpos]
                print(newval)
                print(newpos)
                return newpos
                break

#Esse método retorna o numero de telefone dado uma chave, usando dois for
    def busca_telefone(self, key):
        #Com tratamento de colisão
        pos0 = self.hashDivisao(key)
        pos = self.hashDivisao(key)
        for i in range(self.table_size + 1):
            newpos0 = ((pos0 + (i+3)) & 0x7FFFFFFF) % self.table_size
            valor = newpos0
            for i in range(self.table_size + 1):
                newpos = ((pos + (i+3)) & 0x7FFFFFFF) % self.table_size
                if self.array[newpos] == None:
                    return 0
                if newpos == valor:
                    newval = self.array[newpos]
                    print(newval)
                    return newpos

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        
        #return h % self.table_size
        return h
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.array[h] = val
        return h 

    def get(self, key):
        h = self.get_hash(key)
        print(h)

        #return self.array[h]

    def imprime_tabela(self):
        print(self.array)


if __name__ == '__main__':
    t = HashTable()

    t.insere_tratamento_colisao("jorge", 12345678)
    t.insere_tratamento_colisao("leticia", 87654321)
    t.insere_tratamento_colisao("matheus", 18233496)
    t.insere_tratamento_colisao("geralt", 93162149)
    t.insere_tratamento_colisao("lua", 99999999)
    t.insere_tratamento_colisao("lucas", 33311152)
    t.insere_tratamento_colisao("rosa", 93934477)
    t.insere_tratamento_colisao("rogerin", 83419462)
    t.insere_tratamento_colisao("fabiana", 13418156)
    t.insere_tratamento_colisao("michael", 89233217)

    t.busca_tratamento_colisao("rogerin", 83419462)
    #t.busca_tratamento_colisao("lua", 99999999)
    #t.busca_tratamento_colisao("fabiana", 13418156)

    t.busca_telefone("rogerin")
    #t.busca_telefone("lua")
    #t.busca_telefone("fabiana")
    
    t.imprime_tabela()