#include<stdio.h>

void main(){
    int field[4][4] = {{0,1,0,1},{0,0,0,1},{1,1,1,0},{0,1,1,1}};
    int mines[4][4] = {{0,0,0,0},{0,0,0,0},{0,0,0,0},{0,0,0,0}};

    int w = 4, h = 4;

    for (int y=0;y<h;y++){  // y 값 0,1,2,3
        for(int x=0;x<w;x++){  // x 값 0,1,2,3
            
            if(field[y][x]==0) continue;  // field배열의 00 01 02 03 10 11 12 13 ... 값 0이면 continue
            
            for(int i=y-1;i<=y+1;i++){
                for(int j=x-1;j<=x+1;j++){
                    if(calculate(w,h,j,i)==1){
                        mines[i][j] += 1;
                    }
                }
            }
        } 
    }

    for (int y=0;y<h;y++){  // y 값 0,1,2,3
        for(int x=0;x<w;x++){  // x 값 0,1,2,3
            printf("%d",mines[y][x]);
            printf("\n");
        }
    }
    

}

int calculate(int w,int h,int j,int i){
    if(i>=0&&i<h&&j>=0&&j<w) return 1;
    return 0;
}