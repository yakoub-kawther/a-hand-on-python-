riverq={'contry1':'river1' , 'contry2':'river2' , 'contry3':'river3' , 'contry4':'river4', 'contry5':'river5' , 'contry6':'river6'}

for contry , river in riverq.items():
    print(f"{river} runs in {contry}")

for river in riverq.values():
    print(river)

for contry in riverq.keys():
    print(contry)