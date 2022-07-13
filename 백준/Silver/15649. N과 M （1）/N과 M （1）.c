#include <stdio.h>

#define MAX 9
typedef enum {false, true} bool;
int N, M;
int arr[MAX];
bool visited[MAX];

void func(int count){
	if(count == M){
		for (int i = 0; i < M; i++){
			printf("%d ", arr[i]);
		}
		printf("\n");
	}

	for (int i = 1; i <= N; i++){
		if (!visited[i]){
			visited[i] = true;
			arr[count] = i;
			func(count + 1);
			visited[i] = false;
		}
	}
}
int main(int argc, char const *argv[])
{
	scanf("%d%d", &N, &M);

	func(0);

	return 0;
}
