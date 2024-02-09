#include <iostream>
#include <fstream>
#include "menu.h"
using namespace std;

int main(){
    //displaying ascii 
    string fileline;
    ifstream myfile("ascii.txt");
    if (myfile.is_open()){
        while(getline(myfile, fileline)){
        cout << fileline << endl ;
        } 
        myfile.close();
    }else {
        cout << "ERROR \n";
    }
    cout << endl ;
    cout << "Welcome to Cyberpunk 2077 Breach Protocol!\n" ;
    menu();
    return 0;
}