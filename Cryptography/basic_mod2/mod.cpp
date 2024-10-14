#include <bits/stdc++.h>    
using namespace std;

int main() {
    vector <int> arr1;
    while(1) {
        int x;
        cin >> x;
        if(x == -1) break;
        else arr1.push_back(x);
    }

    vector <int> arr2;
    for(int i = 0; i<arr1.size();i++)
        arr2.push_back(arr1[i] % 41);
    
    for(int i = 0; i<arr2.size();i++)
        cout << arr2[i] << " ";
   
}