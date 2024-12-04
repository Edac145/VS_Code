#include <stdio.h>

#include <time.h>
#include<conio.h>

int main() {
     time_t t;
       time(&t);
       printf("Today's date and time : %s",ctime(&t));
       getch();
    return 0;
}