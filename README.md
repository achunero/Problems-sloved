#include <iostream>
using namespace std;

int reversenum(int num)
{
int result=0;
while(num!=0)
{
result=result*10+num%10;
num=num/10;
}
 return result;
}
int main()
{
int count,num1,num2,sum,a,b;
cout<<"\nEnter the count:";
cin>>count;
while(count!=0)
{
cin>>num1;
cin>>num2;
sum=reversenum(num1) + reversenum(num2);
cout<<reversenum(sum);
count--;
}
return 0;
}


