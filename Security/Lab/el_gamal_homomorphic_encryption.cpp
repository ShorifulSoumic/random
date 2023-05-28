#include <bits/stdc++.h>
using namespace std;

typedef double db;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<int, int> pii;



int p=1549;
long long bigmod(ll a, ll b) //(a^b)%mod
{
    ll anss=1;
    while(b)
    {
        if(b%2==1) anss=(anss*a)%p;
        a=(a*a)%p;
        b/=2;
    }
    return anss%p;
}

int main()
{
    // int p=1549;
    int x=1234;

    int g=1;
    while(g++)
    {
        set<int>s;
        int mul=1;
        for(int i=0;i<p-1;i++)
        {
            s.insert(mul%p);
            mul=(mul*g)%p;
        }
        if(s.size()==p-1 || g>=p)
            break;
    }

    int y=1;
    for(int i=1;i<=x;i++)
        y=(y*g)%p;

    int m1=456, m2=1233, r1=122, r2=145;
    cout<<"m1: "<<m1<<endl;
    cout<<"m2: "<<m2<<endl;
    cout<<"g: "<<g<<endl;
    cout<<"y: "<<y<<endl;

    int c11=1, c21=1;
    for(int i=1;i<=r1;i++)
    {
        c11=(c11*g)%p;
    }
    cout<<"c11: "<<c11<<endl;
    for(int i=1;i<=r1;i++)
    {
        c21=(c21*y)%p;
    }
    c21=(c21*m1)%p;
    cout<<"c21: "<<c21<<endl;


    int c12=1, c22=1;
    for(int i=1;i<=r2;i++)
    {
        c12=(c12*g)%p;
    }
    cout<<"c12: "<<c12<<endl;
    for(int i=1;i<=r2;i++)
    {
        c22=(c22*y)%p;
    }
    c22=(c22*m2)%p;
    cout<<"c22: "<<c22<<endl;

    int c1=(c11*c12)%p, c2=(c21*c22)%p;
    cout<<"c1: "<<c1<<endl;
    cout<<"c2: "<<c2<<endl;


    //decryption
    int c11x=1;
    for(int i=1;i<=x;i++)
        c11x=(c11x*c11)%p;
    int m_1=(c21*bigmod(c11x, p-2))%p;
    cout<<"m_1: "<<m_1<<endl;

    int c12x=1;
    for(int i=1;i<=x;i++)
        c12x=(c12x*c12)%p;
    int m_2=(c22*bigmod(c12x, p-2))%p;
    cout<<"m_2: "<<m_2<<endl;

    cout<<"(m_1*m_2)%p: "<<(m_1*m_2)%p<<endl;

    int c1x=1;
    for(int i=1;i<=x;i++)
        c1x=(c1x*c1)%p;
    int m1m2=(c2*bigmod(c1x, p-2))%p;
    cout<<"m1m2: "<<m1m2<<endl;
}


/*
<----SAMPLE---->



<----OUTPUT---->



*/