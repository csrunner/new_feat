//
//  unit_test.cpp
//  
//
//  Created by 史超 on 23/06/2018.
//

//#include "unit_test.hpp"
// header file for string split
#include<string>
#include<vector>
#include<iostream>

// header file for get the local time
#include <cstdio>
#include <ctime>

// read and write the txt file line by line
#include<fstream>
#include<string>

using namespace std;

/*-------------string split module----------------*/
void Tokenize(const string& str, vector<string>& tokens, const string& delimiters)
{
    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);
    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}
void string_split(string str){
    vector<string>tokens;
    Tokenize(str, tokens, ":");
    for( int i = 0; i < tokens.size() ; i++ )
    {
        cout << tokens[i] << endl;
    }
}
/*----------------------------------------------*/

/*--------------get the local time--------------*/
void get_local_time(){
    time_t rawtime;
    struct tm *ptminfo;
    
    time(&rawtime);
    ptminfo = localtime(&rawtime);
    printf("current: %02d-%02d-%02d %02d:%02d:%02d\n",
           ptminfo->tm_year + 1900, ptminfo->tm_mon + 1, ptminfo->tm_mday,
           ptminfo->tm_hour, ptminfo->tm_min, ptminfo->tm_sec);
}
/*---------------------------------------------*/

/*-----------convert char array to double-------*/

double char2double(char *char_string){
    double db;
    //sscanf(char_string, "%lf", &db);
    db = atof(char_string);
    return db;
}


/*----------convert double to char-------------*/
char * float2str(float val, int precision, char *buf)
{
    char *cur, *end;
    
    sprintf(buf, "%.6f", val);
    if (precision < 6) {
        cur = buf + strlen(buf) - 1;
        end = cur - 6 + precision;
        while ((cur > end) && (*cur == '0')) {
            *cur = '\0';
            cur--;
        }
    }
    
    return buf;
}
/*---------------------------------------------*/

string read_txt(string file_path){
    ifstream in(file_path);
    string s;
    return 0;
}


int main(int argc, char *argv[])
{
    string str("12:11:ccc:ddd:");
    string_split(str);
    
    get_local_time();
    
    char  szString[] = "092.12";
    double db = char2double(szString);
    printf("\nsscanf result:\n");
    printf("%f  %.12f  %.2f  %e  %E\n", db, db, db, db, db);
    
    
    char buf[128];
    printf("%s\n", float2str((float)5.123, 2, buf));
    
    // read txt file
    /*
    ifstream in("/Users/shichao/Downloads/result06.txt");
    string s;
    while(getline(in,s))//着行读取数据并存于s中，直至数据全部读取
        cout<<s.c_str()<<endl;
    */
    //
    ofstream in;
    in.open("/Users/shichao/Downloads/result.txt",ios::trunc); //ios::trunc表示在打开文件前将文件清空,由于是写入,文件不存在则创建
    int i;
    char a='a';
    for(i=1;i<=26;i++)//将26个数字及英文字母写入文件
    {
        if(i<10)
        {
            in<<"0"<<i<<"\t"<<a<<"\n";
            a++;
        }
        else
        {
            in<<i<<"\t"<<a<<"\n";
            a++;
        }
    }
    in.close();//关闭文件
    return 0;
}
