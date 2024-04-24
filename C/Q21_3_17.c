#include<stdio.h>

struct jsu{
    char name[12];
    int os, db, hab, hhab;
};

int main(){
    struct jsu st[3] = {{"데어터1",95,88},{"데어터2",84,91},{"데어터3",86,75}};
    struct jsu* p;

    p = &st[0];

    (p+1)->hab = (p+1)->os + (p+2)->db;
    (p+1)->hhab = (p+1)->hab + p->os + p->db;

    printf("%d\n",(p+1)->hab + (p+1)->hhab);
}