#include <stdio.h>

void main(){
	char a[100];
	printf("HELLO! your name?\n");
	while (scanf("%s", &a)!=1){
		if (scanf("%s", &a)){
			printf("NO!\n");
		}else{

			printf("HEllo, %s!", a);
		}
	}
}

