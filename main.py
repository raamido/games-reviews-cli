import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

from initialize import Review, session

console = Console()


table = Table(show_header=True, header_style="bold magenta")
table.add_column(" ")
table.add_column("Game Name")
table.add_column("Rate", justify="center")
table.add_column("Review", justify="center")


def get_reviews():
    reviews = []
    for review in session.query(Review):
        reviews.append(review)
    return reviews


def leave_review(game_name, rating, review):
    record = Review(game_name=game_name, rate=rating, review=review)
    session.add(record)
    session.commit()


def reset_table():
    global table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column(" ")
    table.add_column("Game Name")
    table.add_column("Rate", justify="center")
    table.add_column("Review", justify="center")


global game_name
global rate
global rev

while True:
    console.clear()
    console.print(Panel(Text("Main Menu", justify="center")))
    console.print("1. [bold]Reviews[/bold]")
    console.print("2. [bold]New Review[/bold]")
    console.print("3. [bold]About[/bold]")
    Option = Prompt.ask("Insert Your Option")

    if Option == "1":
        while True:
            console.clear()
            console.print(Panel(Text("Reviews", justify="center")))
            for review in get_reviews():
                table.add_row(str(review.id), review.game_name, "⭐" *
                              review.rate, review.review)
            console.print(table)
            input("")
            reset_table()
            break

    elif Option == "2":
        while True:
            console.clear()
            console.print(Panel(Text("Add Review", justify="center")))
            while True:
                game_name = Prompt.ask('Game Name')
                if len(game_name) == 0:
                    console.print("Game Name [red]CANNOT BE EMPTY![/red]")
                    continue
                elif len(game_name) < 2:
                    console.print("Game Name Cannot Be less than 2 chars")
                    continue
                else:
                    break

            while True:
                rate = Prompt.ask('Rating')
                if not rate.isdigit():
                    console.print("rating must be a number")
                    continue
                elif int(rate) > 5 and int(rate) < 0:
                    console.print("rating must be a number between 0 and 5")
                    continue
                else:
                    break

            while True:
                rev = Prompt.ask('Type Your review')
                if len(rev) < 2 and len(rev) > 999:
                    console.print(
                        "review length must be between 2 and 999 chars")
                    continue
                else:
                    break
            leave_review(game_name, rate, rev)
            print("[green]Review Added![/green]")
            time.sleep(3)
            break

    elif Option == "3":
        console.clear()
        console.print(Panel(Text("About", justify="center")))
        console.print(
            "Game Reviews, is a command line program designed and developed by Raamido!")
        Prompt.ask("")
        continue

    elif Option == "exit!":
        break

    else:
        continue
