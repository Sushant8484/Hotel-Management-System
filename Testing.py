from CRUD_Operation import HotelManagement

obj = HotelManagement()

while True:
    print("**************** New Details ****************")
    print(" 1.Add Customer Details\n 2.Show All Details\n 3.Search Details\n 4.Update Details\n 5.Delete Details")
    print("For exit enter any number(except 1 to 5)")
    choice = int(input('enter your choice : '))
    if choice == 1:
        obj.Customerdetails()
    elif choice == 2:
        obj.Showdetails()
    elif choice == 3:
        obj.SearchDetails()
    elif choice == 4:
        obj.UpdateDetails()
    elif choice == 5:
        obj.DeleteDetails()
    else:
        print("Thank you for using...")
        break