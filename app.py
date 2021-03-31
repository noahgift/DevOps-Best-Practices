#!/usr/bin/env python
import click


def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1, 5, 10, 25]  # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem = divmod(int(amount * 100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num: coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num: coin_lookup[coin]})
    return res


@click.command()
@click.option(
    "--amount",
    prompt="Amount: ",
    help="Creates change for dollar and cents value:  i.e. 1.34",
)
def make_change(amount):
    """Gives Correct Change"""

    result = change(float(amount))
    click.echo(click.style(f"Change for {amount}:", fg="red"))
    for correct_change in result:
        for num, coin in correct_change.items():
            click.echo(click.style(f"{coin}: {num}", fg="green"))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    make_change()
