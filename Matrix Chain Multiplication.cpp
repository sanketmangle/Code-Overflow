
Problem Statement:

Matrix Chain Multiplication

Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices i.e. determine where to place parentheses to minimise the number of multiplications.
You will be given an array p[] of size n + 1. Dimension of matrix Ai is p[i - 1]*p[i]. You need to find minimum number of multiplications needed to multiply the chain.
Input Format :
Line 1 : Integer n i.e. number of matrices
Line 2 : n + 1 integers i.e. elements of array p[] 
Output Format :
Line 1 : Minimum number of multiplication needed
Constraints :
1 <= n <= 100
Sample Input 1 :
3
10 15 20 25
Sample Output :
8000
Sample Output Explanation :
There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
If multiply in order A1*(A2*A3) then number of multiplications required are 15000.
If multiply in order (A1*A2)*A3 then number of multiplications required are 8000.
Thus minimum number of multiplications required are 8000



CODE:

#include<bits/stdc++.h>
int dp[101][101];
int helper(int *p,int s,int e)
{
    if(s>=e)
    {
        return 0;
    }
   
  
    if(dp[s][e]!=-1)
    {
       return dp[s][e];  
    }
       
    int ans=INT_MAX;
    for(int k=s;k<e;k++)
    {
        int temp=helper(p,s,k)+helper(p,k+1,e)+p[s-1]*p[k]*p[e];
        ans=min(ans,temp);
    }
    dp[s][e]=ans;
    return ans;
}
int mcm(int* p, int n)
{

    memset(dp, -1, sizeof dp);
    return helper(p,1,n);

}
