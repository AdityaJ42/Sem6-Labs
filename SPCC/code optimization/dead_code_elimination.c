#include<stdio.h>
#include<time.h>
int global;

void before(){
	int i;
	i = 1;
	global = 1;
	global = 2;
	printf("Global: %d\n", global);
	global = 3;
}

void after(){
	global = 2;
	printf("Global: %d\n", global);
}

void main(){
	clock_t start, end;
	double time;

	start = clock();
	before();
	end = clock();
	time = ((double)(end - start)) / CLOCKS_PER_SEC;
	printf("Time before optimization: %f\n", time);
	
	start = clock();
	after();
	end = clock();
	time = ((double)(end - start)) / CLOCKS_PER_SEC;
	printf("Time after optimization: %f\n", time);
}