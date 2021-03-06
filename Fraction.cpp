class Fraction{

private:

	int numerator;
	int denominator;

public:

	Fraction(int numerator, int denominator){
		this -> numerator = numerator;
		this -> denominator = denominator;
	}

	void print(){
		cout << this -> numerator << " / " << this -> denominator << endl;
	}

	void simplify(){
		int gcd = 1;
		int j = min(this -> numerator, this -> denominator);

		for (int i = 1; i <= j; i++){
			if (this -> numerator % i == 0 && this -> denominator % i == 0)
				gcd = i;
		}

		this -> numerator = this -> numerator / gcd;
		this -> denominator = this -> denominator / gcd;
	}

	void add(Fraction f2){
		int lcm = this -> denominator * f2.denominator;
		int num = (lcm / this -> denominator) * numerator + (lcm / f2.denominator) * f2.numerator;

		this -> numerator = num;
		this -> denominator = lcm;

		simplify();
	}

};