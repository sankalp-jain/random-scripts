#include<iostream>
using namespace std;

class time{
	public:
		int hours, minute, second;
		
		
		void get_time(int hrs, int min, int sec){
			hours = hrs;
			minute = min;
			second = sec;
		}
		
		time operator- (time &t1){
			time t;
			
			cout<<t1.hours<<":"<<t1.minute<<":"<<t1.second<<endl;	
			cout<<this->hours<<":"<<this->minute<<":"<<this->second<<endl;				
			
			if(t1.second > this -> second)
		    {
		        --this -> minute;
		        this -> second += 60;
		    }
		
		    t1.second = this -> second - t1.second;
		    if(t1.minute > this -> minute)
		    {
		        --this -> hours;
		        this -> minute += 60;
		    }
		    t1.minute = this->minute-t1.minute;
		    t1.hours = this->hours-t1.hours;
			
			return t1;
		}
		
		void show_diff(time input, time end){
			cout<<"input"<<endl;
			cout<<input.hours<<" "<<input.minute<<" "<<input.second<<endl;
			cout<<"output"<<endl;
			cout<<end.hours<<" "<<end.minute<<" "<<end.second<<endl;
			
			time t = end - input;
			cout<<t.hours<<":"<<t.minute<<":"<<t.second<<endl;		
		}
};

int main(){
	int inp_hrs, inp_min, inp_sec, op_hrs, op_min, op_sec;
	cin>>inp_hrs>>inp_min>>inp_sec;
	cin>>op_hrs>> op_min>>op_sec;
	time t1;
	time t2;
	
	t1.get_time(inp_hrs, inp_min, inp_sec);
	t2.get_time(op_hrs, op_min, op_sec);
	
	t1.show_diff(t1, t2);
	return 0;
}
