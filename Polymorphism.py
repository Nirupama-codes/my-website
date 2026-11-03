# class CashPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using cash")

# class UPIPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using UPI")

# class CardPayment:
#     def pay(self,amount):
#         print("Paid",amount,"using Card")

# class NetBanking:
#     def pay(self,amount):
#         print("Paid",amount,"NetBanking")


# payments=[
#     CashPayment(),
#     UPIPayment(),
#     CardPayment(),
#     NetBanking()
# ]

# choice=input("Choose payment menthod")
# if choice == "cash":
#     payment=CashPayment()
# elif choice == "upi":
#     payment=UPIPayment()
# elif choice == "card":
#     payment = CardPayment()
# elif choice == "netbanking":
#     payment = NetBanking()
#     exit()

# for payment in payments:
#     payment.pay(1000)

# Consider an application that sends notifications.

# class MobileNotification:
#     def send_notification(self):
#         print("Your order has been placed successfully via Mobile Notification")

# class EmailNotification:
#     def send_notification(self):
#         print("Your order confirmation has been sent to your Email")

# class SMSNotification:
#     def send_notification(self):
#         print("Your order has been confirmed via SMS")     

# notifications=[
#     MobileNotification(),
#     EmailNotification(),
#     SMSNotification(),
# ]  
# choice=input("Choose notification method")
# if choice == "mobile push notification":
#     send=MobileNotification()
# elif choice == "email":
#     notification = EmailNotification()
# elif choice == "sms":
#     notification = SMSNotification()
#     exit()
# for notification in notifications:
#     notification.send_notification()         
    

