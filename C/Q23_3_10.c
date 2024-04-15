#include<stdio.h>

int main(){
    char* p = "KOREA";
    printf("%s ", p);
    printf("%s ", p+1);
    printf("%c ", *p);
    printf("%c ", *(p+3));
    printf("%c ", *p+4);
}