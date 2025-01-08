#include <iostream>
#include <iomanip>
#include<limits>
using namespace std;
class Buyer{
    public:
        int amount,day,customer;
        void set(int a,int d,int c){
            amount = a;
            day = d;
            customer = c;
        };
};

class Reporting{
    public:
        string *conver,game[5];
        int price_game[5];
        Reporting(string list_game[5],int list_price[5]){
            for(int i = 0;i<5;i++){
                game[i] = list_game[i];
                price_game[i] = list_price[i];
            }
        }
        Reporting(string i[]){conver = i;}
        void show(int a){cout << conver[a] << endl;};
        void show2(int a){cout << game[a] << endl;};
        void show3(int a){cout << price_game[a];}
};


class Price: public Buyer{
    public:
        int sum=0;
        int *price_game;
        void setprice(int pgame[]){price_game = pgame;};
        void seting(int game);
};

void Price::seting(int game){
            sum+=price_game[game-1];
};

class Total: public Price {
    public:
        float total;
        void calculate(){total = (sum*day)/customer;};
        void toshow();
};

void Total::toshow(){
            cout<<"============================================="<<endl;
            cout<<"Total Price = " << sum << "x" << day << "/" << customer;
            cout<<" = "<<total<<endl;
};

class Slip{
    public :
        int count,*games,days,custome,*price;
        string show[5];
        Slip(){cout << "\nCompleted game rental....\n=============================================" << endl;}
        Slip(int a,int b[],int e,int f){
            count = a;
            games = b;
            days = e;
            custome = f;
        }
        void setoption(string a[],int b[]){
            for (int i = 0;i<5;i++){show[i] = a[i];}
            price = b;
        }
        void create(){
            char trans[20];
            int sum=0;
            for(int i = 0;i < count;i++){sum+=price[games[i]-1];}
            FILE *slip;
            slip = fopen("game rental receipt.txt","w");
            fprintf(slip,"----- Your Rental List -----\n");
            for(int i = 0;i < count;i++){
                for(int j = 0;j < show[games[i]-1].length();j++){trans[j] = show[games[i]-1][j];}
                for(int j = show[games[i]-1].length();j <= 20;j++){trans[j] = ' ';}
                fprintf(slip,"%d.[%d/day] %s\n",i+1,price[games[i]-1],trans);
            }
            fprintf(slip,"\nNumber of rental days : %d",days);
            fprintf(slip,"\nNumber of customer in this slip : %d",custome);
            fprintf(slip,"\nCalculated price : %d*%d/%d",sum,days,custome);
            fprintf(slip,"\n\nTotal price : %.2d",(sum*days)/custome);
            fclose(slip);
        };
};


int check(){
    if (cin.fail()){cin.clear();cin.ignore(numeric_limits<streamsize>::max(),'\n');
    cout << "!!!please only enter number..."<<endl;
    return 1;
    } else {return 0;}};
 
    
int main(){
    int amount=0,day=0,cust=0,sum,ask;
    float total = 0;
    string text[4] = {"if don't rent just get out from my store..."
                    ,"That's more than the games I for rent. (enter again)"
                    ,"This store for rents atleast 1 day as a minimum. (enter again)"
                    ,"That's less than the games I for rent. (enter again)"};
    string list_game[5] = {"Home Sweet Home "
                        ,"Battlefield V "
                        ,"Grand theft auto V "
                        ,"Call of duty 4: Modern Warfare "
                        ,"Naruto Shippuden: Ultimate Ninja Storm 4 "};
    int list_price[5] = {20,40,35,30,35};
    Reporting checker(text);
    Reporting gamer(list_game,list_price);
    cout << "=============== Game Rental Store ==============="<<endl;
    for(int i = 0;i < 5;i++){
        cout << i+1 << ". [";
        gamer.show3(i);
        cout << "/day] ";
        gamer.show2(i);
    }
 
    
    cout << "\nManager : How many game do you want...?(Max 5)"<<endl;
    while(amount > 5 or amount < 1){
        cout << "Amount of game : ";cin >> amount;
        if (check() == 0){
            if (amount < 1){checker.show(0);exit(0);}
            else if (amount > 5 ){checker.show(1);}
        }
    }


    cout << "\nManager : How many day you want to borrow?"<<endl;
    while(day < 1){
        cout << "Amount of day : ";cin >> day;
        if (check() == 0){if (day < 1 ){checker.show(2);}}
    }
        
        
    cout << "\nManager : How many people do you want to split the payment?\t(if not type 1)\nAmount of customer : ";cin >> cust;
    while(cust < 1){
        cout << "Amount of customer : ";cin >> cust;
        if (check() == 0){ if (cust < 1 ){checker.show(0);exit(0);}}
    }


    Total customer;
    customer.setprice(list_price);
    customer.set(amount,day,cust);
    int select[amount];
    cout << "\n";
    
    
    cout << "=============== Game Rental Store ==============="<<endl;
    for(int i = 0;i < 5;i++){cout << i+1 << ". ";gamer.show2(i);}
    cout<<"(Enter number of game you need)\n";
    for(int e = 0;e < amount;e++){
        while(select[e] > 5 || select[e] < 1){
            cout << "Game " << e+1 << " : ";cin >> select[e];            
            customer.seting(select[e]);
            if (check() == 0){
                if (select[e] < 1){checker.show(3);}
                else if (select[e] > 5 ){checker.show(1);}
            }
        }
    }
        
    cout<<fixed<<setprecision(2);
    customer.calculate();
    customer.toshow();
    
    cout << "\nManager : Are you need slip ?\n(1 for Yes & 2 for No)"<<endl;
    while(ask > 2 or ask < 1){
        cout << "Your Answer : ";cin >> ask;
        if (check() == 0){
            if (ask > 2 or ask < 1){cout << "please answer only 1 or 2..." << endl;}
        }
    }
    if (ask == 2) {Slip end;}
    else{
        Slip end(amount,select,day,cust);
        end.setoption(list_game,list_price);
        end.create();}
}
