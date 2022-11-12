class Hotel:
    def __init__(self):
        self.__name = ''
        self.__address = ''
        self.__check_in_date = ""
        self.__check_out_date = ""
        self.__room_no = 0
        self.__room_rent = 0
        self.__food_bill = 0
        self.__total_amount = 0

    def getname(self):
        return self.__name

    def getaddress(self):
        return self.__address

    def getcheck_in_date(self):
        return self.__check_in_date

    def getcheck_out_date(self):
        return self.__check_out_date

    def getroom_no(self):
        return self.__room_no

    def getroom_rent(self):
        return self.__room_rent

    def getfood_bill(self):
        return self.__food_bill

    def gettotal_amount(self):
        return self.__total_amount

    def setname(self,__name):
        self.__name = __name

    def setaddress(self,__address):
        self.__address = __address

    def setcheck_in_date(self,__check_in_date):
        self.__check_in_date = __check_in_date

    def setcheck_out_date(self,__check_out_date):
        self.__check_out_date = __check_out_date

    def setroom_no(self,__room_no):
        self.__room_no = __room_no

    def setroom_rent(self,__room_rent):
        self.__room_rent = __room_rent

    def setfood_bill(self,__food_bill):
        self.__food_bill = __food_bill

    def settotal_amount(self,__total_amount):
        self.__total_amount = __total_amount

    def __str__(self):
        return f"CustomerDeatils[name = {self.__name} , Address = {self.__address} , check in date = {self.__check_in_date} , check out date = {self.__check_out_date} , " \
               f"Room no = {self.__room_no} , Room rent = {self.__room_rent} , Food bill = {self.__food_bill} , Totol amount = {self.__total_amount}]"

if __name__ == "__main__":
    obj = Hotel()
    print(obj)







