#include <iostream>
using namespace std;

int sumDigits(int n){
	if (n == 0)
		return 0;
	int smallOutput = sumDigits(n / 10);
	return n%10 + smallOutput;
}

int main(){
	int n;
	cin >> n;
	int sum = sumDigits(n);
	cout<<sum;
	return 0;
}
