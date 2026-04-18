import art
print(art.logo)

dictBid = {}
valueTrue = 1
topName = ""
topPrice = 0

while valueTrue:
    name = input("What is your name?:")
    price = input("What is your bid?: $")

    dictBid[name] = price

    answer = input("Are there any other bidders? Type 'yes or 'no'.")
    if answer == "yes":
        print("\n" * 20)
        print(dictBid)
    elif answer == "no":
        for i in dictBid:
            if int(dictBid[i]) > topPrice:
                topName = i
                topPrice = int(dictBid[i])
        print(f"The winner is {topName} with a bid of ${topPrice}")
        valueTrue = 0


# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


