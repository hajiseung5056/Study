#include<stdio.h>
#include<stdlib.h>

struct A{
    int n;
    int g;
};

int main(){
    struct A* a = malloc(2 * sizeof(struct A));
    int i;
    for(i=0;i<2;i++){
        a[i].n=i;
        a[i].g=i+1;
    }

    printf("%d",a[0].n + a[1].g);
    free(a);

    return 0;

}