int fact(int n){
	if (n == 0){
		return 1;
	}
	else{
		return n * fact(n - 1);
	}
}

int main(int argc, char const *argv[]){
	int n;

	scanf("%d", &n);

	printf("%d", fact(n));
	return 0;
}