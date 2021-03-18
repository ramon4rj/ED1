#include <iostream>
#include <stdlib.h>

using namespace std;  // definição do tamanho da lista, da frente e traseira;

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
    for(int i=tail-1; i>=head; i--){ //o laço pega a posição anterior a última, pega seu campo de dados
        lista[i] = lista[i-1];       //e substitui o campo de dados superior com o da posição anterior e
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

int insere_lista(int valor, int posi){ //inserção em qualquer parte da lista
    if (tail = tamanho-1){
        cout << "... " << '\n';
    }
    if(posi>head && posi<=tail){
        for(int i=tail+1; i>posi; i--){
            lista[i] = lista[i-1];
        }
        lista[posi] = valor;
        tail++;
    }else{
        cout << "Posição inválida " << '\n';
    }
}

int remove_lista_final(int &valor){  //valor é usado para receber o valor de tal posição
        valor = lista[tail];         //que nesse caso é a última, localizada em tail
        tail--;
    }

int remove_lista_frente(int &valor){  //valor recebe o valor da primeira posição e a posição em
    if (head>tail){                   //que ele estava vai recebendo os valores subsequentes.
        valor = lista[head];
    }
    for (int i=head; i<tail; i++){
        lista[i] = lista[i+1];
    }
    tail--;
}

int remove_lista_meio(int posi){
    if (posi>head && posi<tail){
        for(int i=posi; i<tail; i++)
            lista[i] = lista[i+1];
    }
    tail--;
}


int main(){
    int op1, op2, op3;
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
