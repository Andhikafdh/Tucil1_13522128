#ifndef __MENU__
#define __MENU_H__

#include <bits/stdc++.h>

using namespace std;

void menu();
// User choice cards' input manually or randomly

void result(int choice);
// if the choice is '1' then user manually input their cards, if '2' system will generate randomized cards

void txtInput();
// user manually input their cards

void ansToTxt(vector<int> cards, vector<string> solutions, float time);
// save solutions to file .txt

#endif