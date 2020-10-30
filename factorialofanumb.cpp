#include<iostream.h>
using namespace std;

int main()
{
  int n;
  cin>>n;
  long long pro=1;
  for(int i=2;i<=n;i++)
  {
    pro*=i;
  }
  cout<<"Factorial of "<<n<<" is "<<pro;
}
