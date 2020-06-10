# put your python code here
duration_in_days = int(input())
food_cost_per_day = int(input())
one_way_flight_cost = int(input())
hotel_cost_per_night = int(input())

sum_of_money = (food_cost_per_day * duration_in_days) \
               + (one_way_flight_cost * 2) \
               + (hotel_cost_per_night * (duration_in_days - 1))

print(sum_of_money)