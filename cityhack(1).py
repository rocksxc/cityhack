import psycopg2
import csv
import json
import os
class cityhack:
    def __init__(self):
        self.connect=psycopg2.connect(database="postgres",user="postgres",password="Excalibur123",host="121.196.40.134",port='5433')
        self.cursor=self.connect.cursor()
    def sort(self):
        sql="select * from covid_19 order by p desc";
        self.cursor.execute(sql)
        rows=self.cursor.fetchall()
        for i in rows:
            print(i)
        print();
    def special(self,city):
        try:
            if(city=='Q' or city=='q'):return
            sql = "select * from covid_19 where code =" +city+";"
            self.cursor.execute(sql);
            rows=self.cursor.fetchall()
            print(rows)
            print()
        except psycopg2.errors.UndefinedColumn:
            print("unknown code number please input again or input Q for quit\n");
            command=input();
            self.special(command)
                
    def file(self):
        csv_file=open("data.csv",'w',newline='')
        writer=csv.writer(csv_file)
        writer.writerow(['code','name','p','have','not']);
        sql="select * from covid_19 order by p desc";
        self.cursor.execute(sql)
        rows=self.cursor.fetchall()
        for i in rows:
            i=list(i)
            writer.writerow([ i[0] , i[1] , i[2] , i[3] , i[4] ] )
        csv_file.close()
        print('finish\n')

    def start(self):
        while(1):
            print("-------------------------")
            print("Hello user, please input the command you want\n")
            print("input R for check the risk sorted for all distinct\n")
            print("input O for a csv which have all imformation\n")
            print("input C for check the distinct you want\n")
            print("input Q for quit\n")
            print("-------------------------")
            command=input()
            if(command=='R' or command =='r'):
                self.sort()

            elif (command=='C' or command=='c'):
                print("---------------------")
                print("please input the code number for the distinct you want to check or input Q for quit\n")
                print("---------------------")
                city=input()
                self.special(city)

            elif(command=='Q' or command=='q'):
                print("thanks for using\n")
                self.cursor.close()
                self.connect.close()
                break;
            elif (command=='O' or command=='o'):
                self.file();
            else:
                print("unkown command please input again\n");

start= cityhack();
start.start();