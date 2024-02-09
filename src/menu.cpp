#include <bits/stdc++.h>
#include "menu.h"

using namespace std ;

void menu() {
    string option;
    bool valid=false;
    cout << "\n" ;
    cout << "##### MENU #####\n" ;
    cout << "1. Input txt\n" ;
    cout << "2. Input Random\n" ;
    cout << "3. Exit\n" ;
    do{
        cout << "Input your choice: ";
        getline(cin, option);
        if (option == "1"){
            result(1);
            valid = true;
        }else if (option =="2"){
            result(2);
            valid = true;
        }else if (option =="3"){
            valid = true;
            printf("\n"
                   "###### Thanks for Playing Cyberpunk 2077 Breach Protocol ######\n");
        }else{
            printf("Invalid Input!\n");
        }
    } while (!valid);
}

void result (int option){
    if (option == 1) {
        txtInput();
    }else {

    }
}



void txtInput() {
    cout << "\n" ;
    cout << "##### Input #####\n";
    // Get input for the file name
    cout << "Masukkan nama file (.txt): ";
    string namaFile;
    getline(cin, namaFile);

    // Construct the file path
    string filePath = "../test/" + namaFile + ".txt";

    // Open the file for reading
    ifstream file(filePath);

    // Check if the file is opened successfully
    if (!file.is_open()) {
        cout << "Error opening the file." << endl;
    }

    // Read and process the content of the file
    string line;
    while (getline(file, line)) {
        // Process each line as needed
        cout << line << endl;
    }

    // Close the file
    file.close();
}

void cliInput() {

}
