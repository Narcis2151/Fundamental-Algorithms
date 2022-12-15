// Complexitate O(n*m)
#include <fstream>
#include <vector>
#include <math.h>
using namespace std;

ifstream fin("retea2.in");
ofstream fout("retea2.out");

int vizitat[30000]= {0};
vector<pair<int,int>> blocuri,centrale;
vector<double> distEnergie;

int n,m;
double distMinEnerg,costFinal;

double calcDist(pair<int,int> a,pair<int,int> b){ //formula de distanta
    return sqrt(1.0*(a.first-b.first)*(a.first-b.first) + 1.0*(a.second-b.second)*(a.second-b.second));
}


void Prim(){

    int indexBloc=-1; //retinem la care bloc am gasit energie

    distMinEnerg=INT_MAX;
    for (int j = 0; j < m; j++) { // trecem pe la fiecare bloc si tinem minte la ce blocuri am gasit energie
        if(distEnergie[j]<distMinEnerg && !vizitat[j]){  
            indexBloc=j;
            distMinEnerg=distEnergie[j];
        }
    }
    vizitat[indexBloc]=1;
    costFinal+=distMinEnerg;
    for (int j = 0; j < m; j++) { // daca avem un bloc cu energie mai apropiat de blocul curent, actualizam distanta pana la acel bloc
        distEnergie[j]= min(distEnergie[j], calcDist(blocuri[j],blocuri[indexBloc])); 
    }
}

int main()
{
    fin>>n>>m;
    blocuri.resize(m+1);
    centrale.resize(n+1);
    distEnergie.resize(m+1,INT_MAX); //distanta pana la cea mai apropiata cladire cu energie

    for (int i = 0; i < n; i++) {
        int x ,y;
        fin>>x>>y;
        centrale[i]= {x,y};
    }
    for (int i = 0; i < m; i++) {
        int x, y;
        fin>>x>>y;
        blocuri[i]= {x,y};
    }
    // Presupunem ca fiecare bloc trebuie sa fie conectat direct de o centrala, deci calculcam distanta de la fiecare
    // bloc pana la o centrala
    for (int i = 0; i < m; i++) 
        for (int j = 0; j < n; j++) 
            distEnergie[i]=min(distEnergie[i], calcDist(blocuri[i],centrale[j]));
        


    // Dupa ce avem distantele initiala de la blocuri la centrale, 
    // facem Prim din fiecare bloc pentru a gasi surse si mai apropiate de energie
    for (int i = 0; i < m; i++) 
        Prim();

    fout.precision(6);
    fout<<fixed<<costFinal;
    return 0;
}