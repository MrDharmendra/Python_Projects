Hours=int(input("Enter the working HRS="))
Rate=int(input("Enter the rate="))
if Hours<40:
    pay=round(Hours*Rate,2)
    print("The  pay is ",pay)

else:
    overtime=Hours-40
    pay=round(Hours*Rate*overtime*1.5,2)
    print("The Overtime  is ",pay)
