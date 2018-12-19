#include "stdio.h"

int main() {
    /*int f = 10551264;*/
    int f = 24;
    int a = 0;
    int b = 1;

    int d = 0;
    int c = 0;

    loop1:
        d = 1;
        loop2:
            c = b * d;
            if (c == f) {
                a = b + a;
                printf("%d\n", b);
            }
            d++;
            if (d > f) {
                b++;
                if (b > f) {
                    printf("%d\n", a);
                    return 0;
                } else {
                    goto loop1;
                }
            } else {
                goto loop2;
            }
}
