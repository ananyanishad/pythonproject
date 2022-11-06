import pymysql

con = None
cur = None

con = pymysql.connect(host='localhost',
                        database='bank',
                        user='root',
                        password='')
cur = con.cursor()

        
def OpenAcc(name,account,DOB,address,openbalance):
        sql = 'insert into account values(%s,%s,%s,%s,%s)'
        c = con.cursor()
        c.execute(sql)
        con.commit()
                
def DepositAmo():
        sql = 'update amount set balance = %s where AccountNo = %s'
        c = con.cursor()
        myresult = c.fetchone()
        cur.execute(sql)
        con.commit()
                
def WithAmm(data):
        sql = 'update amount set balance = %s where AccountNo = %s'
        c = con.cursor()
        cur.execute(sql)
        con.commit()
                
def BalanceEnq():
        sql = 'select balance from amount where AccountNo = %s'
        c = con.cursor()
        c.execute(sql)
        myresult = c.fetchone()
        con.commit()

def DisplayAcc():
        sql = 'select from account whhere AccountNo = %s'
        c = con.cursor()
        c.execute(sql)
        myresult = c.fetchone()
        for i in myresult:
                print(i,end=" ")
