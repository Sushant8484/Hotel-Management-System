from Hotel_management import Hotel

class HotelManagement:
    database = []
    r_id = 101

    def Customerdetails(self):
        h = Hotel()
        h.setroom_no(HotelManagement.r_id)
        h.setname(input("enter your name : "))
        h.setaddress(input("enter your address : "))
        h.setcheck_in_date(input("enter check in  date : "))
        h.setcheck_out_date(input("enter check out date : "))
        h.setfood_bill(self.FoodBill())
        h.setroom_rent(self.RoomRent())
        h.settotal_amount(self.TotalAmount())
        HotelManagement.database.append(h)
        HotelManagement.r_id += 1

    def FoodBill(self):
        print("Menu :\n 1.Breakfast\n 2.Lunch\n 3.Dinner")
        self.Bill = 0
        Food_choice = int(input("enter your choice : "))
        if Food_choice == 1:
            print("Breakfast :\n 1.chai Rs 30 \n 2.Coffee Rs 50 \n 3.sandwich Rs 100\n 4.Maggi Rs 70")
            option = int(input("enter your option : "))
            Quantity = int(input("enter Quantity : "))
            if option == 1:
                self.Bill += (30 * Quantity)
            elif option == 2:
                self.Bill += (50 * Quantity)
            elif option == 3:
                self.Bill += (100 * Quantity)
            elif option == 4:
                self.Bill += (70 * Quantity)
            else:
                print("wrong option entered...")

        elif Food_choice == 2:
            print("Lunch :\n 1.Dal Rice Rs 200 \n 2.panner tikka Rs 250\n 3.chicken korma Rs 350")
            option = int(input("enter your option :"))
            Quantity = int(input("enter Quantity : "))
            if option == 1:
                self.Bill += (200 * Quantity)
            elif option == 2:
                self.Bill += (250 * Quantity)
            elif option == 3:
                self.Bill += (350 * Quantity)
            else:
                print("wrong option entered...")

        elif Food_choice == 3:
            print("Dinner :\n 1.Dal Rice Rs 200 \n 2.panner tikka Rs 250\n 3.chicken korma Rs 350")
            option = int(input("enter your option :"))
            Quantity = int(input("enter Quantity : "))
            if option == 1:
                self.Bill += (200 * Quantity)
            elif option == 2:
                self.Bill += (250 * Quantity)
            elif option == 3:
                self.Bill += (350 * Quantity)
            else:
                print("wrong option entered...")
        else:
            print("wrong option entered...")

        return self.Bill

    def RoomRent(self):
        print("Rooms are categorize into four type : \n"
              "1.Vip Amenities per night Rs 5000 \n"
              "2.suite per night Rs 4000 \n"
              "3.studio per night Rs 3000 \n"
              "4.Deluxe per night Rs 2000")
        choice = int(input("enter your choice = "))
        Night = int(input("how many nights you want to stay = "))
        self.roomrent = 0

        if choice == 1:
            self.roomrent = (5000 * Night)
        elif choice == 2:
            self.roomrent = (4000 * Night)
        elif choice == 3:
            self.roomrent = (3000 * Night)
        elif choice == 4:
            self.roomrent = (2000 * Night)
        else:
            print("wrong choice entered....")

        return self.roomrent

    def TotalAmount(self):
        A = self.Bill + self.roomrent
        return A

    def Showdetails(self):
        for i in HotelManagement.database:
            print(i)

    def SearchDetails(self):
        print("1.name\n2.address\n3.check_in_date\n4.check_out_date\n5.room_no\n6.room_rent\n7.food_bill\n8.total_amount")
        n = int(input("search by choice : "))
        if n == 1:
            Name = input("enter name : ")
            for i in  HotelManagement.database:
                if i.getname() == Name:
                    print(i)
            else:
                return "wrong name entered"
        elif n == 2:
            Address = input("enter Address : ")
            for i in  HotelManagement.database:
                if i.getaddress() == Address:
                    print(i)
            else:
                return "wrong Address entered"
        elif n == 3:
            check_in_date = input("enter check_in_date : ")
            for i in  HotelManagement.database:
                if i.getcheck_in_date() == check_in_date:
                    print(i)
            else:
                return "wrong check_in_date entered"
        elif n == 4:
            check_out_date = input("enter check_out_date : ")
            for i in  HotelManagement.database:
                if i.getcheck_out_date() == check_out_date:
                    print(i)
            else:
                return "wrong check_out_date entered"
        elif n == 5:
            room_no = input("enter room_no : ")
            for i in  HotelManagement.database:
                if i.getroom_no() == room_no:
                    print(i)
            else:
                return "wrong room_no entered"
        elif n == 6:
            room_rent = input("enter room_rent : ")
            for i in  HotelManagement.database:
                if i.getroom_rent() == room_rent:
                    print(i)
            else:
                return "wrong room_rent entered"
        elif n == 7:
            food_bill = input("enter food_bill : ")
            for i in  HotelManagement.database:
                if i.getfood_bill() == food_bill:
                    print(i)
            else:
                return "wrong food_bill entered"
        elif n == 8:
            total_amount = input("enter total_amount : ")
            for i in  HotelManagement.database:
                if i.gettotal_amount() == total_amount:
                    print(i)
            else:
                return "wrong total_amount entered"
        else:
            return "wrong choice entered"

    def UpdateDetails(self):
        n = int(input("enter existing room no : "))
        for i in HotelManagement.database:
            if i.getroom_no() == n:
                print("what you want to update\n1.name\n2.address\n3.check_in_date\n4.check_out_date\n5.room_no\n6.room_rent\n7.food_bill\n8.total_amount")
                choice = int(input('enter your choice : '))
                if choice == 1:
                    i.setname(input("enter new name : "))
                elif choice == 2:
                    i.setaddress(input("enter new address : "))
                elif choice == 3:
                    i.setcheck_in_date(input("enter new check_in_date : "))
                elif choice == 4:
                    i.setcheck_out_date(input("enter new check_out_date : "))
                elif choice == 5:
                    i.setroom_no(input("enter new room_no : "))
                elif choice == 6:
                    i.setroom_rent(i.getroom_rent() + self.RoomRent())
                    i.settotal_amount(i.getfood_bill()+i.getroom_rent())
                    # i.setroom_rent(input("enter new room_rent : "))
                elif choice == 7:
                    i.setfood_bill(i.getfood_bill() + self.FoodBill())
                    i.settotal_amount(i.getfood_bill()+i.getroom_rent())
                    # i.setfood_bill(input("enter new food_bill : "))
                elif choice == 8:
                    i.settotal_amount(input("enter new total_amount : "))
                else:
                    return "wrong"

    def DeleteDetails(self):
        r = int(input('enter existing room no : '))
        for index in range(len(HotelManagement.database)):
            room = HotelManagement.database[index]
            if room.getroom_no() == r:
                HotelManagement.database.pop(index)
                return "Room detail deleted successfully..."
        else:
            return "Room number not exist in database"



if __name__ == "__main__":
    ref = HotelManagement()
    ref.Customerdetails()
    ref.Showdetails()

    ref.Customerdetails()
    ref.Showdetails()
    ref.SearchDetails()
    ref.UpdateDetails()
