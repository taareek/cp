#include <iostream>

using namespace std;

int main()
{
    int a,b,c,t;
    cin>>t;
    for(int i=0; i<t; i++){
        cin>>a>>b>>c;
        if (a+b==c || b+c==a || a+c==b){
           cout<<"YES\n";
        }else{
            cout<<"NO\n";
        }
    }

    return 0;
}
