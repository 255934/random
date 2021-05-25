# pylint: disable=R1705,E1111, W0105,W0612,R0912,R0915, R0914,W0702,R1710,C0301,C0114,C0116,C0121,C0103
import sqlite3

def Payment(mobile, due, name):
    cnt = 0
    for i in mobile:
        if i.isalpha():
            cnt = cnt + 1
    if len(str(mobile)) == 10 and cnt == 0:
        if due > 0:
            status = 0
        else:
            status = 1

        conn = sqlite3.connect('project.db')
        c = conn.cursor()
        d = c.execute('SELECT * from duetable where mobile = ? ', (mobile,))
        set_status = d.fetchall()
        if set_status:
            c.execute('''UPDATE duetable SET status = ? WHERE mobile = ?''', (0, mobile))
            conn.commit()
        else:
            c.execute('INSERT INTO duetable VALUES (?,?,?)', (name, mobile, status))
            conn.commit()

        payment_type = input("Enter 1 to pay through Wallet \n 2 to pay through upi \n Enter other key to exit")
        if payment_type == '1':
            value = payment_wallet(mobile, due, name)

        elif payment_type == '2':
            value = payment_upi(mobile, due, name, val='payment')

        d = c.execute('SELECT * from duetable where mobile = ? ', (mobile,))
        status_data = d.fetchall()
        if status_data[0][2] == 1:
            return 'Payment Success'
        else:
            return 'Payment Failed'

    else:
        return 'Invalid Mobile number'


def payment_wallet(mobile, due, name):
    initial_amount = 0
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    d = c.execute('SELECT * from wallettable where mobile = ? ', (mobile,))
    w_data = d.fetchall()

    # check if new user
    if w_data:
        print("\nhello", w_data[0][0], "\nyour wallet balance is", w_data[0][2])
    else:
        # c = conn.cursor()
        c.execute('INSERT INTO wallettable VALUES (?,?,?)', (name, mobile, initial_amount))
        conn.commit()

    mode_selection = input("\nEnter 1 to add money \nEnter 2 to pay \n Any other to GoBack")

    if mode_selection == '1':
        # adding money to wallet
        value_add = payment_upi(mobile, due, name, 'add_to_wallet')
        '''if value_add == False:
            return False'''
    elif mode_selection == '2':
        c = conn.cursor()
        d = c.execute('SELECT * from wallettable where mobile = ? ', (mobile,))
        w_data = d.fetchall()
        # paying through wallet
        if due <= w_data[0][2]:
            balance = w_data[0][2]
            balance = balance - due
            c.execute('''UPDATE wallettable SET amount = ? WHERE mobile = ?''', (balance, mobile))
            conn.commit()
            print("Amount paid")
            due = 0
            c.execute('''UPDATE duetable SET status = ? WHERE mobile = ?''', (1, mobile))
            conn.commit()
        else:
            print("\nInsufficient Balance")
            payment_wallet(mobile, due, name)

    else:
        Payment(mobile, due, name)
    conn.close()


def payment_upi(mobile, due, name, val):
    val1 = val
    conn = sqlite3.connect('project.db')
    if val1 == 'payment':
        upi_user = input('\nEnter 1 to create upi \nEnter 2 to pay \nEnter 3 to check balance \n Anyother to GoBack')
        if upi_user == '1':
            c = conn.cursor()
            d = c.execute('SELECT * from upitable where mobile = ? ', (mobile,))
            u_data = d.fetchall()
            if u_data:
                print("\nupi already exist")
                payment_upi(mobile, due, name, 'payment')
            else:
                money = 10000

                def pin1_generation():
                    try:
                        upi_pin1 = int(input("\nEnter four digit upi pin"))
                        return upi_pin1
                    except:
                        print("\nplease enter integer")
                        pin1_generation()

                def pin2_generation():
                    try:
                        upi_pin2 = int(input("\nRe Enter four digit upi pin"))
                        return upi_pin2
                    except:
                        print("\nplease enter integer")
                        pin2_generation()

                upi_pin1 = pin1_generation()
                upi_pin2 = pin2_generation()
                if upi_pin1 == upi_pin2:
                    c.execute('INSERT INTO upitable VALUES (?,?,?,?)', (name, mobile, upi_pin2, money))
                    conn.commit()
                    print("Upi created successfully")
                    Payment(mobile, due, name)
                else:
                    print("\nplease enter unique pin")
                    pin1_generation()
                    pin2_generation()

        elif upi_user == '2':
            c = conn.cursor()
            d = c.execute('SELECT * from upitable where mobile = ? ', (mobile,))
            u_data = d.fetchall()
            if u_data:
                upi_balance = u_data[0][3]
                upi_pin = int(input("\nEnter pin"))
                if upi_pin == u_data[0][2]:
                    if due <= upi_balance:
                        upi_balance = upi_balance - due
                        c.execute('''UPDATE upitable SET acc_balance = ? WHERE mobile = ?''', (upi_balance, mobile))
                        conn.commit()
                        print("\nAmount paid")
                        due = 0
                        c.execute('''UPDATE duetable SET status = ? WHERE mobile = ?''', (1, mobile))
                        conn.commit()
                    else:
                        print("\nInsufficient balance")
                        return False
                else:
                    print("\nInvalid pin")
                    Payment(mobile, due, name)
            else:
                print("\ncreate upi to pay")
                payment_upi(mobile, due, name, 'payment')
        elif upi_user == '3':
            c = conn.cursor()
            d = c.execute('SELECT * from upitable where mobile = ? ', (mobile,))
            u_data = d.fetchall()
            if u_data:
                print("\nHello", u_data[0][0], "\nyour account balance is", u_data[0][3])
            else:
                print("\nCreate upi to view balance")
            payment_upi(mobile, due, name, 'payment')

        else:
            Payment(mobile, due, name)

    elif val1 == 'add_to_wallet':
        # The comment here removed by Vinuthna.
        c = conn.cursor()
        d = c.execute('SELECT * from upitable where mobile = ? ', (mobile,))
        u_data = d.fetchall()

        if u_data:
            add_money = int(input("\nEnter amount to add"))
            upi_pin = int(input("\nEnter pin"))
            if upi_pin == u_data[0][2]:
                if u_data[0][3] >= add_money:
                    bank_balance = u_data[0][3]
                    bank_balance = bank_balance - add_money
                    c.execute('''UPDATE upitable SET acc_balance = ? WHERE mobile = ?''', (bank_balance, mobile))
                    conn.commit()

                    d = c.execute('SELECT * from wallettable where mobile = ? ', (mobile,))
                    w_data = d.fetchall()
                    wallet_balance = w_data[0][2]
                    wallet_balance = wallet_balance + add_money
                    c.execute('''UPDATE wallettable SET amount = ? WHERE mobile = ?''', (wallet_balance, mobile))
                    conn.commit()
                    print("\nMoney added")
                    payment_wallet(mobile, due, name)

                else:
                    print("\nInsufficient balance in account")
                    return False
            else:
                print(upi_pin)
                print("\nIncorrect Pin")
                payment_wallet(mobile, due, name)
        else:
            print("\nYou are not a upi user")
            payment_upi(mobile, due, name, 'payment')

    conn.close()
