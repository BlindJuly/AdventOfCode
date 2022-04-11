#include <iostream>
#include <string>
#include <cmath>
#include <iomanip>
#include <fstream>
#include <map>
#include <array>
#include <algorithm>
using namespace std; 

int main() {
    int count = 0;
    int iterDone[12];

    string bitString;
    ifstream diagnostic;
    diagnostic.open("input.txt");
    

    map<int, int> bitMap;
    for (int i = 0; i < 12; i++){
        bitMap[i] = 0;
    }

    cout << "******************************************************************" << endl;

    while(diagnostic >> bitString){
        count += 1;
        for (int i = 0; i < 12; i++){
            if (count >= 500){
                if (iterDone[i] == i){
                    continue;
                }
            }
            if (count){
                cout << "count: " << count << ", BitString: " << bitString << ", CurrBit: " << bitString[i] << ", Ones: " << bitMap[i] << ", i: " << i << endl;
            }    
            if (bitString[i] == '1'){
                bitMap[i] += 1;
                if (bitMap[i] > 500){
                    bitMap[i] = 1;
                    iterDone[i] = i;
                }
                else if ((count - bitMap[i]) > 500){
                    bitMap[i] = 0;
                    iterDone[i] = i;
                }
            }
        }
    }
    map<int, int>::iterator it;
    for (it = bitMap.begin(); it != bitMap.end(); it++){
        cout << it->second << " , ";
    }
    diagnostic.close();
    cout << endl << "****************************************************************" ;
return 0;
}
