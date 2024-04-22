#include<stdio.h>
// 정수 역순출력 1234 >> 4321 12340 12344
int main(){
    int number = 1234;
    int div = 10;
    int result = 0;

    while (number != 0){
        result = result * div;
        result = result + number % div;
        number = number / div;
    }
    printf("%d", result);
    return 0;
}