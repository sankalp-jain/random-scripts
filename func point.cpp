#include<iostream>
#include<conio.h>
using namespace std;

int main(){
    string factors[] = {"No. of external inputs", "External outputs", "External inquiries", "internal logic files", "External Interface files"};
    int simple[] = {3, 4, 3, 7, 5};
    int avg[] = {4, 5, 4, 10, 7};
    int complex[] = {6, 7, 6, 15, 10};
    int count, i, fi, fp;
    float fs = 0;
    char choice;
    
    int uaf = 0;
    for (i = 0; i < 5; i++){
        cout<<"Enter the count for the factor "<<factors[i]<<endl;
        cin>>count;
        cout<<"Enter your choice whether simple, average, complex"<<endl;
        cin>>choice;
        if (choice == 's')
           uaf += count * simple[i];
        if (choice == 'a')
           uaf += count * avg[i];
        
        if (choice == 'c')
           uaf += count * complex[i];
    }
    cout<<"uaf"<<endl;
    cout<<uaf<<endl;
    for (i = 0; i < 14; i++){
    	cout<<"Enter the value of fi"<<endl;
        cin>>fi;
        fs += fi;
    }
    cout<<fs<<endl;
    float vaf = 0.65 + (fs / 100);
    cout<<vaf<<endl;
    fp = vaf * uaf;
    cout<<"Functional Point is"<<endl;
    cout<<fp;
    return 0;
}

