#include <fstream>
using namespace std;

ifstream fin("disjoint.in");
ofstream fout("disjoint.out");

int tata[100001];
int h[100001];

//Compresie de cale
int Reprez(int u)
{
    while(tata[u]!=0)
        u = tata[u];
    return u;
}

void Reuneste(int u, int v)
{
    int ru = Reprez(u);
    int rv = Reprez(v);
    
    if(h[ru] > h[rv])
    {
        tata[rv] = ru;
    }
    else
    {
        tata[ru] = rv;
        if(h[ru]==h[rv])
            h[rv] = h[rv] + 1;
    }


}
int main()
{
    int n,m;
    fin>>n>>m;

    for(int i = 0; i<n; i++)
    {
        tata[i] = 0;
        h[i] = 0;
    }

    for(int i = 0; i<m; i++)
    {
        int c, u, v;
        fin>>c>>u>>v;

       if(c == 1) 
            Reuneste(u,v);
            
        if(c == 2)
        {
            if(Reprez(u) == Reprez(v)) 
                fout<<"DA\n";
            else fout<<"NU\n";
        }
                
    }

    fin.close();
    fout.close();
    return 0;
}