#include<stdio.h>
#include<time.h>

void before(){
	int x, y, z;
	x = 7;
	y = 2 * (x - 1);
	z = 3 * (y + 1);
	printf("Value = %d\n", z);
}

void after(){
	int y, z;
	y = 2 * (7 - 1);
	z = 3 * (y + 1);
	printf("Value = %d\n", z);
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