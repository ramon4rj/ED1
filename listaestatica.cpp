#include <iostream>
#include <stdlib.h>

using namespace std;  // defini��o do tamanho da lista, da frente e traseira;

const int tamanho = 5;
int head ,tail;

int lista[tamanho];

void constroi_lista(){
    head = 0;
    tail = -1;
}

int lista_tamanho(){
    return tail+1;
}

int insere_inicio_lista(int valor){
    if (tail == tamanho-1){
        cout << "Lista cheia " << '\n';
    }
    for(int i=tail-1; i>=head; i--){ //o la�o pega a posi��o anterior a �ltima, pega seu campo de dados
        lista[i] = lista[i-1];       //e substitui o campo de dados superior com o da posi��o anterior e
    }                                //assim sucessivamente
    lista[head] = valor;
    tail++;
}

int insere_final_lista(int valor){
    if (tail = tamanho-1){
        cout << "Lista cheia " << '\n';
    }
    lista[tail] = valor;
    tail++;
}

int insere_lista(int valor, int posi){ //inser��o em qualquer parte da lista
    if (tail = tamanho-1){
        cout << "... " << '\n';
    }
    if(posi>head && posi<=tail){ //
        for(int i=tail+1; i>posi; i--){
            lista[i] = lista[i-1];
        }
        lista[posi] = valor;
        tail++;
    }else{
        cout << "Posi��o inv�lida " << '\n';
    }
}

int remove_lista_final(int &valor){  //valor � usado para receber o valor de tal posi��o
        valor = lista[tail];         //que nesse caso � a �ltima, localizada em tail
//        lista[tail-1] =  checar depois
        tail--;
    }

int remove_lista_frente(int &valor){  //valor recebe o valor da primeira posi��o e a posi��o em
    if (head>tail){                   //que ele estava vai recebendo os valores subsequentes.
        valor = lista[head];
    }
    for (int i=head; i<tail; i++){
        lista[i] = lista[i+1];
    }
    tail--;
}

int remove_lista_meio(int posi){
    int valor;
    if (head>tail){  //se a lista estiver vazia, insere o elemento no come�o
//        valor = lista[head];
    }if (posi>head && posi<tail){
//        valor = lista[posi];
        for(int i=posi; i<tail; i++)
            lista[i] = lista[i+1];
    }
    tail--;
}


int main(){
    int op1, op2, op3, op4, op5;
    int val;

    constroi_lista();
    cout << "tamanho: " << tamanho << '\n';

    insere_inicio_lista(4);
    op1 = insere_lista(2,1);
    op2 = insere_lista(3,2);
    op2 = insere_lista(8,3);
    op2 = insere_lista(7,4);

    for(int i=0; i<tamanho; i++){
        cout << "lista: " << lista[i] << '\n';
    }
    cout << " " << '\n';

//    op3 = remove_lista_meio(3);
//    for(int i=0; i<tamanho; i++){
//        cout << "lista: " << lista[i] << '\n';
//    }

    op3 = remove_lista_frente(val);
    for(int i=0; i<tamanho; i++){
        cout << "lista: " << lista[i] << '\n';
    }

//    op3 = remove_lista_final(val);
//    for(int i=0; i<tamanho-1; i++){
//        cout << "lista: " << lista[i] << '\n';
//    }
}
