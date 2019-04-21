#include<stdio.h>
#include<time.h>

void before(float r){
	float pi = 3.14;
	printf("Circumference = %f\n", 2 * pi * r);
	printf("Area = %f\n", pi * r * r);
}

void after(float r){
	float pi = 3.14, t;
	t = pi * r;
	printf("Circumference = %f\n", 2 * t);
	printf("Area = %f\n", t * r);
}

void main(){
	float r = 7.0;
	clock_t start, end;
	double time;

	start = clock();
	before(r);
	end = clock();
	time = ((double)(end - start)) / CLOCKS_PER_SEC;
	printf("Time before optimization: %f\n", time);
	
	start = clock();
	after(r);
	end = clock();
	time = ((double)(end - start)) / CLOCKS_PER_SEC;
	printf("Time after optimization: %f\n", time);
}