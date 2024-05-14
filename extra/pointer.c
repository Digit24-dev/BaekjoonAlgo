#include <stdio.h>

int main()
{
    int a = 1;
    int *p = &a;

    printf("a: %d \n", a);
    printf("p: %p \n", p);
    
    p++;

    printf("a: %d \n", a);
    printf("p: %p \n", p);
}