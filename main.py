from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

from initialize import Review, session

console = Console()


table = Table(show_header=True, header_style="bold magenta")
table.add_column("Game Name")
table.add_column("Rate", justify="center")
table.add_column("Review", justify="center")


def get_reviews():
    reviews = []
    for review in session.query(Review):
        reviews.append(review)
    return reviews


def reset_table():
    global table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Game Name")
    table.add_column("Rate", justify="center")
    table.add_column("Review", justify="center")


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
                table.add_row(review.game_name, "⭐" *
                              review.rate, review.review)
            console.print(table)
            input("")
            reset_table()
            break

    elif Option == "2":
        break

    elif Option == "exit!":
        break

    else:
        continue
