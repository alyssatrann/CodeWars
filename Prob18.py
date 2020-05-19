while True:
    try:
        [H, M] = map(int, input().split(':'))
        angle_mins = M * 6
        angle_hours = H * 30 + M * 0.5
        angle = min((angle_mins - angle_hours) % 360, (angle_hours - angle_mins) % 360)
        print(f'The angle between the Hour hand and the Minute hand is {angle:.2f} degrees')
    except EOFError:
        break
