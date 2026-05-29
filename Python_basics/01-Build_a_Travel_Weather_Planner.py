# Values
distance_mi = 7
is_raining = True
has_bike = True
has_car = True
has_ride_share_app = True

travel = False

# Validation
if isinstance(distance_mi, (int, float)):
    if not distance_mi:
        travel = False
    elif distance_mi <= 1 and not is_raining:
        travel = True
    elif 1 < distance_mi <= 6 and has_bike and not is_raining:
        travel = True
    elif distance_mi > 6 and (has_car or has_ride_share_app):
        travel = True
    else:
        travel = False
else:
    travel = False

print(travel)