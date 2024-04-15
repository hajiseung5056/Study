#include<stdio.h>
#include<stdlib.h>

typedef struct Data{
    char c;
    int *numPtr;
} Data;

int main(){
    int num = 10;
    Data d1;
    Data *d2 = malloc(sizeof(Data));

    d1.numPtr = &num;
    d2->numPtr = &num;
    printf("%d\n", *d1.numPtr);
    printf("%d\n", *d2->numPtr);

    free(d2);
    return 0;
}