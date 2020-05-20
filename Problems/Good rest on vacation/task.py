# put your python code here
stay_duration,daily_food_cost,flight_cost,daily_room_cost=int(input()),int(input()),int(input()),int(input())
print((stay_duration * daily_food_cost) + (2 * flight_cost) + ((stay_duration-1) * daily_room_cost))
