from pickle import FALSE
import random

Command = list()
Food_Order = list()
Food_Main = ['เมนูอาหาร','เมนูเครื่องดื่ม']
Food_Menu = {}
Food_Menu_Food = {}
Food_Menu_Drinks = {'อเมริกาโน่': 95,'ลาเต้': 95, 'เอสเพรสโซ': 95,'คาปูชิโน่': 95
,'มอคค่า': 95,'ช็อคโกแลต': 95,'ไวท์ช็อคโกแลต': 95,'ชาไทย': 95,'ชาเขียว': 95 
,'มัทฉะ ลาเต้': 105,'ชาดำ': 85,'ชามะนาว': 95,'สตอเบอรี่โซดา': 70,'เเอปเปิลโซดา': 70,'มะนาวโซดา': 70}
Food_Menu_M = ['TH' , 'JAPAN' , 'INDIA']
Food_TH = {'ต้มยำกุ้ง ' : 70,'แกงส้มไหลบัว' : 60,'กระเพราะหมูสับ' : 50,'หมูกระเทียม' : 50
,'แกงเขียวหวานไก่' : 60,'น้ำพริกกระปิ':30,'แพนงหมู':50,'ผัดขี้เมาทะเล':80,'ปูผัดผงกะหรี่':120
,'ไข่พะโล้':40,'กุ้งอบวุ้นเส้น':60,'แกงเทโพ':50,'ข้าวผัดไข่':50,'ผัดไทยกุ้งสด':70,'แกงจืดเต้าหู้หมูสับ':50}
Food_JAPAN = {'แซลมอน ซาชิมิ' : 250,'อูด้ง' : 150,'กุ้งเทมปุระ' : 200,'มันปู' : 320
,'ข้าวหน้าปลาไหล' : 200,'ไก่ทอดคาราอาเกะ':150,'ข้าวหน้าเนื้อ':190,'โอนิกิริ':80,'ข้าวแกงกะหรี่':150
,'เต้าหู้':120,'ทาโกะยากิ':90,'ยากิโซบะ':150,'ปลาชัมมะย่างเกลือ':200,'ทงคัตสึ':120,'เกี๊ยวซ่า':180}
Food_INDIA = {'ข้าวหมกไก่' : 150,'ไก่ทันดูรี' : 250,'ตาล' : 100,'แป้งนาน' : 70
,'โดซ่า' : 90,'แกงไก่ทิกก้ามาซาล่า':190,'ทาริ':250,'ซาโมซ่า':200,'ปารี ปูริ':180
,'โมโม่':150,'ระซัม':200,'ปาปรี จาฎ':120,'แกงมาซาลาเนยปะนีย์':190,'เคบับ':200}
Food_ALL = [Food_TH,Food_JAPAN,Food_INDIA]
for b in range(0,3) :
    Food_Menu_Food[Food_Menu_M[b]] = Food_ALL[b]
Food_Menu[Food_Main[0]] = Food_Menu_Food
Food_Menu[Food_Main[1]] = Food_Menu_Drinks
Command.append(Food_Menu)
Command.append(Food_Order)

#Note Command[list] > 
# Food_Menu[dict] > Food(TH JAPAN INIDA) Drink
# Check_Order[dict]
# Promotion[dict]
def default() :
    global Command,Select

def menutype(count = 0) :
    print('════════════════════════════════════════')
    for key in Command[Select-1] :
        count += 1
        print(f'{count}.{key}')
    print('3.กลับไปหน้าหมวดคำสั่ง')

def menupick() :
    default()
    Menu = Command[Select-1]
    while True :
        menutype()
        Pick = int(input('เลือกประเภทเมนู : '))
        if Pick == 3 :
            return True
        elif Pick == 2 :
            drinks_option(Menu)
        elif Pick == 1 :
            food_option(Menu)
        else : print(f'ขออภัย ไม่มี {Pick} อยู่ในตัวเลือก')

def call_menu(Menu,count = 0) :
    print('════════════════════════════════════════\n\t【รายการทั้งหมด】\n════════════════════════════════════════')
    for key in Menu :
        count += 1
        print(f'{count}. {key} ({Menu[key]} บาท)')
    print(f'{len(Menu)+1}. กลับไปหน้าเลือกประเภทเมนู\n**หากต้องการยกเลิกรายการต้องกลับไปหมวดคำสั่ง')

def importorder(OrderDrink,PickDrink,MenuDrink) :
    OrderPick = (PickDrink.strip()).split(' ')
    for i in OrderPick :
        OrderDrink.append(int(i))
    for i in OrderDrink :
        count = 0
        for key in MenuDrink :
            count += 1
            if count == i :
                Food_Order.append(key)
    if len(MenuDrink)+1 in OrderDrink :
        return 'exit'

def reportorder(OrderDrink,count = 0) :
    if len(OrderDrink) != 0 :
            print('รายการที่คุณสั่ง : ', end = '')
            for i in Food_Order :
                count += 1
                if count == len(Food_Order) :
                    print(f'{i}')
                else :print(f'{i} ,',end = '')

def drinks_option(Menu,OrderDrink = list()) :
    MenuDrink = Menu[Food_Main[1]]
    call_menu(MenuDrink)
    while True :
        PickDrink = input('เลือกรายการที่ต้องการ : ')
        if ((PickDrink.strip()).replace(' ','')).isdigit() :
            check = importorder(OrderDrink,PickDrink,MenuDrink)
            reportorder(OrderDrink)
            OrderDrink.clear()
            if check == 'exit' :
                break
        else : print('ขออภัย กรุณากรอกใหม่เป็นตัวเลขเท่านั้น')

def food_menu(Menu,count = 0) :
    print('════════════════════════════════════════\n\t',end = ' ')
    for key in Menu :
        count += 1
        if count == len(Menu) :
            print(key+'\n↳ หรือพิมพ์ exit เพื่อกลับไปหน้าเลือกประเภทเมนู')
        else :
            print(key + ' , ', end = '')

def food_option(Menu,OrderDrink = list()) :
    MenuFood = Menu[Food_Main[0]]
    food_menu(MenuFood)
    while True : 
        Pick = input('เลือกประเภท : ')
        if Pick in MenuFood :
            MenuTH = MenuFood[Pick]
            call_menu(MenuTH)
            while True :
                PickDrink = input('เลือกรายการที่ต้องการ : ')
                if ((PickDrink.strip()).replace(' ','')).isdigit() :
                    check = importorder(OrderDrink,PickDrink,MenuTH)
                    reportorder(OrderDrink)
                    OrderDrink.clear()
                    if check == 'exit' :
                        return
                else : print('ขออภัย กรุณากรอกใหม่เป็นตัวเลขเท่านั้น')
        else : 
            print('ขออภัย ไม่มีประเภทเมนูนี้ในรายการ')

def check() :
    then,Price = checkorder()
    if then == True :
        promo,disc,disper = promotion(Price)
        if disper > 0 :
            disper = 100-(disper*100)
        print(f'โปรโมชั่นลดราคาทั้งหมด = {disc} บาท กับ อีก {disper}%\n════════════════════════════════════════\n1. ยืนยันทำรายการ\n2. เลือกลบรายการ\n3. เช็คโปรโมชั่นที่คุณได้รับ\n4. กลับไปหน้าหมวดคำสั่ง')
        while True :
            Pick = int(input('เลือกคำสั่งที่ต้องการ : '))
            if Pick == 1 :
                Food_Order.clear()
                print(f'════════════════════════════════════════\nคุณได้ยืนยันการทำรายการเรียบร้อยแล้ว\nกรุณาจ่ายเงินที่เคาน์เตอร์เป็นจำนวน {(Price-disc)*(disper/100)} บาท')
                return False
            elif Pick == 2 :
                return removeorder()
            elif Pick == 3 :
                for i in promo :
                    print(i)
            elif Pick ==  4 :
                return True
            else : print('ขออภัย ',Pick,' ไม่มีอยู่ในตัวเลือกกรุณากรอกใหม่ครับ')

def removeorder() :
    checkprice(True)
    print('↳ พิมพ์ exit เพื่อกลับไปหน้าเลือกประเภทเมนู\n════════════════════════════════════════')
    while True : 
        count = 0
        PickDrink = input('ชื่อรายการที่ต้องการลบ : ')
        remt = PickDrink.split(' ')
        for i in remt :
            if i in Food_Order :
                Food_Order.remove(i)
            elif i == 'exit' :
                return True
            else :
                count += 1
                if count == 1 :
                    print(f'ไม่มี {i} ,', end = '')
                else :
                    print(f' {i} ,', end = '')
        if count > 0 :
            print(' อยู่ในตะกร้าของคุณ')

def checkprice(TF,count = 0) :
    sum = 0
    print('════════════════════════════════════════\n\t【รายการที่สั่ง】')
    Food_Check = Food_Order.copy()
    Food_List = list()
    for i in Food_Check :
        for a in Command[0] :
            for b in Command[0][a] :
                if i == b :
                    if not i in Food_List :
                        count += 1
                        if TF == False :
                            print(f'{count}. {i} มี {Food_Check.count(i)} รายการ {Command[0][a][b]*Food_Check.count(i)} บาท')
                        else : print(f'{i} มี {Food_Check.count(i)} รายการ {Command[0][a][b]*Food_Check.count(i)} บาท')
                        sum += Command[0][a][b]*Food_Check.count(i)
                    if Food_Check.count(i) > 1 :
                        Food_List.append(i)
                elif b in Food_Menu_M :
                    for c in Command[0][a][b] :
                        if i == c :
                            if not i in Food_List :
                                count += 1
                                if TF == False :
                                    print(f'{count}. {i} มี {Food_Check.count(i)} รายการ {Command[0][a][b][c]*Food_Check.count(i)} บาท')
                                else : print(f'{i} มี {Food_Check.count(i)} รายการ {Command[0][a][b][c]*Food_Check.count(i)} บาท')
                                sum += Command[0][a][b][c]*Food_Check.count(i)
                            if Food_Check.count(i) > 1 :
                                Food_List.append(i)
    Food_Check.clear()
    Food_List.clear()
    return sum

def checkorder() :
    if len(Food_Order) == 0 :
        print('☐ ขออภัย คุณยังไม่ได้สั่งรายการใดๆ')
        return False,0
    else :
        Price = checkprice(True)
        return True,Price
    print('════════════════════════════════════════')

def promotion1() :
    print ("- ปูผัดผงกะหรี่+มัทฉะ ลาเต้ ลด 25 บาท\n- ผัดขี้เมาทะเล+ชามะนาว ลด 15 บาท\n- ต้มยำกุ้ง+ชาดำ ลด 15 บาท\n- อูด้ง+มะนาวโซดา ลด 20 บาท\n- ข้าวแกงกะหรี่+มอคค่า ลด 25 บาท\n- ปลาซันมะย่างเกลือ+ไวท์ช็อคโกแลต ลด 25 บาท\n- เคบับ+ช็อคโกแลต ลด 25 บาท\n- ปารี ปูริ+ชาเขียว ลด 25 บาท\n- ข้าวหมกไก่+คาปูชิโน่ ลด 25 บาท\n- ซื้อตั้งแต่ 1000 บาทขึ้นไป ลด 15 %\n- ซื้อตั้งแต่ 500 บาทขึ้นไป ลด 10 %\n- ซื้อตั้งแต่ 200 บาทขึ้นไป ลด 5 %")
    return exit_promotion()

def info() :
    print ("วิธีการกรอกตัวเลือก\n - หากระบบให้เลือกรายการเป็น [ตัวเลข] จะย้อนกลับด้วยการเลือก [เลขสุดท้าย]\n - หากระบบให้เลือกรายการเป็น [ชื่อ] จะย้อนกลับด้วยการกรอก 'exit'\n**การเลือกในที่นี้สามารถเลือกหลายรายการพร้อมกันได้ด้วยการเว้นวรรค\n**ตัวอย่าง[หากเป็นเลือกด้วยตัวเลข] - 1 14 12 4\n**ตัวอย่าง[หากเป็นเลือกด้วยชื่อ] - มะนาว ส้มตำ")
    return exit_promotion()

def promotion(Price):
    text = list()
    sum = 0
    discount = 0
    if 'ปูผัดผงกะหรี่' in Food_Order and 'มัทฉะ ลาเต้' in Food_Order :
        sum += 25
        text.append('- ปูผัดผงกะหรี่+มัทฉะ ลาเต้ ลด 25 บาท')
    elif 'ผัดขี้เมาทะเล' in Food_Order and 'ชามะนาว' in Food_Order :
        sum += 15
        text.append('- ผัดขี้เมาทะเล+ชามะนาว ลด 15 บาท')
    elif 'ต้มยำกุ้ง' in Food_Order and 'ชาดำ' in Food_Order :
        sum += 15
        text.append('- ต้มยำกุ้ง+ชาดำ ลด 15 บาท')
    elif 'อูด้ง' in Food_Order and 'มะนาวโซดา' in Food_Order :
        sum += 20
        text.append('- อูด้ง+มะนาวโซดา ลด 20 บาท')
    elif 'ข้าวแกงกะหรี่' in Food_Order and 'มอคค่า' in Food_Order :
        sum += 25
        text.append('- ข้าวแกงกะหรี่+มอคค่า ลด 25 บาท')
    elif 'ปลาซันมะย่างเกลือ' in Food_Order and 'ไวท์ช็อคโกแลต' in Food_Order :
        sum += 25
        text.append('- ปลาซันมะย่างเกลือ+ไวท์ช็อคโกแลต ลด 25 บาท')
    elif 'เคบับ' in Food_Order and 'ช็อคโกแลต' in Food_Order :
        sum += 25
        text.append('- เคบับ+ช็อคโกแลต ลด 25 บาท')
    elif 'ปารี ปูริ' in Food_Order and 'ชาเขียว' in Food_Order :
        sum += 25
        text.append('- ปารี ปูริ+ชาเขียว ลด 25 บาท')
    elif 'ข้าวหมกไก่' in Food_Order and 'คาปูชิโน่' in Food_Order :
        sum += 25
        text.append('- ข้าวหมกไก่+คาปูชิโน่ ลด 25 บาท')
    else : pass
    if Price >= 1000 :
        discount = 0.85
        text.append('- ซื้อตั้งแต่ 1000 บาทขึ้นไป ลด 15 %')
    elif Price >= 500 and Price < 1000 :
        discount = 0.90
        text.append('- ซื้อตั้งแต่ 500 บาทขึ้นไป ลด 10 %')
    elif Price >= 200 and Price < 500 :
        discount = 0.95
        text.append('- ซื้อตั้งแต่ 200 บาทขึ้นไป ลด 5 %')
    else : pass 
    return text,sum,discount


def exit_promotion() :
    print('1. ออกจากโปรโมชั่น\n2. ออกจากโปรแกรม\n════════════════════════════════════════\n*กรุณากรอกเป็นตัวเลขหัวข้อคำสั่ง*')
    Select = int(input('เลือกคำสั่งที่ต้องการ : '))
    if Select == 1 :
        return True
    elif Select == 2 :
        return False
        
def option() :  
    if Select == 1 :
        return menupick()
    elif Select == 2 :
        return check()
    elif Select == 3 :
        return promotion1()
    elif Select == 4 :
        return True
    elif Select == 5 :
        return False
    else :
        pass

def repeat() :
    global Select
    while True :
        Select = int(input('เลือกคำสั่งที่ต้องการ : '))
        if Select > 0 :
            return option()
        else :
            print('ขออภัย ',Select,' ไม่มีอยู่ในตัวเลือกกรุณากรอกใหม่ครับ')
            continue

while True :
    print(f'\nInternational food restaurant\n═════════════ 【หมวดคำสั่ง】 ═════════════\n1. เมนู(อาหารและเครื่องดื่ม)\n2. ตะกร้าสินค้าของคุณ\n3. รายระเอียดโปรโมชั่นต่างๆ\n4. วิธีใช้หมวดคำสั่งอย่างระเอียด\n5. ออกจากโปรแกรม\n════════════════════════════════════════\n*กรุณากรอกเป็นตัวเลขหัวข้อคำสั่ง*')
    if repeat() == False :
        break
    else : pass


