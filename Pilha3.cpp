#include <iostream>
#include <stdlib.h>

using namespace std;

struct Node {
    int dados;
    Node *prox = nullptr;

};

Node* cria_pilha(){
    Node *topo = nullptr; //topo é iniciado como nulo
    return topo;
}

Node* insere_pilha(int num, Node *topo){
    // newnode vai ter dois campo: dados, e prox(ponteiro para o proximo elemento)

    Node *newnode = (Node*) malloc(sizeof(Node)); //aloca um espaço do tamanho de node
    if (newnode == nullptr){
        cout << "nulo \n";
    }
    newnode->dados = num;
    newnode->prox = topo; //newnode->prox vai receber o topo
    topo = newnode; //topo recebe o próximo elemento a ser recebido, o novo nó.
    return newnode;

}

void remove_pilha(Node *&topo){   //pega o valor de topo por referencia
    Node *aux;
    aux = topo->prox;
    free(topo);
    topo = aux;
    return;
}

void imprime_pilha(Node *topo){
    Node *newnode = topo; //newnode recebe o ultimo elemento(topo)
    if(newnode == nullptr){
    	cout << "Pilha vazia" << '\n';
    }
    while(newnode != nullptr){ //e a partir daí vai apontando para o próximo, como "decrementação"
        cout << newnode->dados << '\n';
    	newnode = newnode->prox;
    }
}

int main() {

   Node* topo = cria_pilha();

   topo = insere_pilha(13, topo);

   topo = insere_pilha(14, topo);

   topo = insere_pilha(12, topo);

   topo = insere_pilha(2, topo);
   imprime_pilha(topo);
//   cout << topo->dados << '\n';
   
   cout << "Pos remoçao: " << '\n';
   remove_pilha(topo);
   imprime_pilha(topo);
//   cout << topo->dados << '\n';

   return 0;

}
