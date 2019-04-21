#include<stdio.h>
#include<time.h>

void before(int a, int b){
	int i = 0, z, t;
	while(i < 10){
		t = a * b;
		z = t * 2;
		i++;
	}
	printf("Value: %d\n", z);
}

void after(int a, int b){
	int i = 0, z, t;
	t = a * b;
	while(i < 10){
		z = t * 2;
		i++;
	}
	printf("Value: %d\n", z);
}

void main(){
	int a = 111, b = 222;
	clock_t start, end;
	double time;

	start = clock();
	before(a, b);
	end = clock();
	time = ((double)(end - start)) / CLOCKS_PER_SEC;
	printf("Time before optimization: %f\n", time);
	
	start = clock();
	after(a, b);
	end = clock();
	time = ((double)(end - start)) / CLOCKS_PER_SEC;
	printf("Time after optimization: %f\n", time);
}