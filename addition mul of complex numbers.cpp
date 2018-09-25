/**********
 
Following is the main function we are using internally.
Refer this for completing the ComplexNumbers class.

*/
#include<iostream>
using namespace std;

class ComplexNumbers {
    // Complete this class
  
  public:
    int real;
  	int imaginary;
  
  	ComplexNumbers(int r, int i){
      real = r;
      imaginary = i;      
    }
  
  	void plus(ComplexNumbers const &c2){
      real = real + c2.real;
      imaginary = imaginary + c2.imaginary;
    }
  
  	void multiply(ComplexNumbers const &c2){
      int a1 = real * c2.real;
      int a2 = imaginary * c2.imaginary;
      
      int a3 = real * c2.imaginary;
      int a4 = imaginary * c2.real;
      
      real = a1 - a2;
      imaginary = a3 + a4;
    }
  
  	void print(){
      cout<<real<<" + i"<<imaginary<<endl;
    }	    
};
 
 
int main() {
    int real1, imaginary1, real2, imaginary2;
    int choice;
    cin >> real1 >> imaginary1 >> real2 >> imaginary2 >> choice;
    
    ComplexNumbers c1(real1, imaginary1);
    ComplexNumbers c2(real2, imaginary2);
    
    
    if(choice == 1) {
        c1.plus(c2);
        c1.print();
    }
    else if(choice == 2) {
        c1.multiply(c2);
        c1.print();
    }
    else {
        return 0;
    }
    
}
 




