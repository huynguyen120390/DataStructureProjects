#include <iostream>
#include <map>
#include <iterator>
#include <vector>


using namespace std;

int find_num_with_firstRecurrent(vector <int> arr){
    map<int,int> logTable;
    int num ;

    for(int i  = 0; i < arr.size() ; i++){
        logTable[arr[i]] =  NULL;
    }

    for(int i = 0; i < arr.size(); i++){
        if(logTable[arr[i]] == NULL){
            logTable[arr[i]] = 1;
        }
        else if (logTable[arr[i]] == 1){
            num = arr[i];
            break;
        }
    }
    return num;

}

int main(){
    int arr[] = {2,5,1,2,3,5,1,2,4};
    int n = sizeof(arr)/sizeof(arr[0]);

    vector<int> array (arr, arr + n);
    int num = find_num_with_firstRecurrent(array);
    cout << num << endl;

}