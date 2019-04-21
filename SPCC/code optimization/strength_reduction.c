#include<stdio.h>
#include<time.h>

void before(){
	int i, result;
	for(i = 1; i <= 10; i++){
		result = i * 7;
		printf("%d\n", result);
	}
}

void after(){
	int i, result = 0;
	for(i = 1; i <= 10; i++){
		result += 7;
		printf("%d\n", result);
	}
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