while True:
    try:
        name = input().split(" ")[1]
        rate = float(input().split(" ")[1]) / 60  # calc by the minute, not by the hour

        amount = sum(  # add up all lengths
            (rate * (stop - start))  # $/hr * hr = $
            for ([start, stop])  # separate stop and start
            in (
                (
                    int(time[:2]) * 60 + int(time[2:])  # parse time from x hrs and y mins to (x*60)+y mins
                    for time
                    in (input().split(" ")[1], input().split(" ")[1])  # get input
                )
                for _ in range(2)  # each employee has two times
            )
        )

        print(f'{name} earned ${amount:.2f}')
    except EOFError:
        break
