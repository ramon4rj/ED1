//lista dinamica
#include <iostream>
#include <stdlib.h>

using namespace std;

struct Lista {
    int dados;
    Lista *prox = nullptr;

};

Lista* cria_lista(){
    Lista *lista = (Lista*)malloc(sizeof(Lista));
    lista->prox = nullptr;
    return lista;
}

void insere_lista_dinamica(int num, int posi, Lista *lista){
    Lista *newlista = (Lista*) malloc(sizeof(Lista));
    newlista->dados = num;
    newlista->prox = nullptr;
    Lista *aux = lista;
    while(posi--){ //nao insere em 0
        aux = aux->prox;
    }
    if(aux->prox==nullptr){
        aux->prox = newlista;
    }else{
        newlista->prox = aux->prox;
        aux->prox = newlista;
    }
//    cout << lista->prox->dados << '\n';
    return;
}


Lista* remover_inicio(Lista *lista){
    if(lista==nullptr){
        cout << "Lista vazia..." << '\n';
    }
    Lista *newlista = lista;
    lista = newlista->prox;
    free(newlista);
}

Lista* remover_final(Lista *lista){
    if(lista==nullptr){
        cout << "Lista vazia..." << '\n';
    }
    Lista *ant, *newlista = lista;
    while(newlista->prox!=nullptr){ //la�o que percorre a lista em busca do ultimo elemento
        ant = newlista;
        newlista = newlista->prox;
    }
    if(newlista==lista){  //remove e aponta p/ o prox caso seja o primeri o elemento
        lista = newlista->prox;
    }else{
        ant->prox = newlista->prox;  //anterior vai receber o prox
        free(newlista);
    }
}

Lista* remover_lista(Lista *lista, int posi){
    Lista *ant, *newlista = lista;
    while(newlista!=nullptr && newlista->dados != posi){
        ant = newlista;
        newlista = newlista->prox;
    }
    if(newlista==lista){ //remove o primeiro e atualiza as posi��es
        lista = newlista->prox;
    }else{
        ant->prox = newlista->prox; //o espa�o do no atual sera atualizado com o elemento
        free(newlista);             //apontado(do no removido) por proximo
    }
}

void imprime_lista(Lista *lista){
    Lista *newlista = lista; //newlist recebe a estrutura lista
    if(lista->prox == nullptr){
    	cout << "Lista vazia" << '\n';
    }
    while(newlista->prox != nullptr){ //vai apontando para o pr�ximo, como "decrementa��o"
        cout << newlista->prox->dados << '\n';
    	newlista = newlista->prox;
    }
}

int main(){
    Lista *lista = cria_lista();

    insere_lista_dinamica(12,0,lista);
    insere_lista_dinamica(13,1,lista);
    insere_lista_dinamica(16,2,lista);
    insere_lista_dinamica(17,3,lista);
    insere_lista_dinamica(50,2,lista);
    imprime_lista(lista);
    cout << " " << '\n';

    remover_lista(lista,13); 
    //remover_final(lista);
    //remover_inicio(lista);


    imprime_lista(lista);


}

