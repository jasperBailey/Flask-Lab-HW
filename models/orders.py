import datetime
from models.order import Order

order_1 = Order("Jasper", datetime.datetime(2023,3,10,3,22,55), 1, "Gibson SG", "Gibson_SG.png")
order_2 = Order("Rodger", datetime.datetime(2023,3,14,0,30,24), 1, "PRS Custom", "PRS_Custom.png")
order_3 = Order("Sky", datetime.datetime(2023,2,12,8,45,24), 1, "Fender Telecaster", "Fender_Telecaster.png")
order_4 = Order("Keith", datetime.datetime(2023,1,10,18,20,40), 2, "Fender Stratocaster", "Fender_Stratocaster.png")

order_list = [order_1, order_2, order_3, order_4]
