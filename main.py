from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

console = Console()


while True:
    console.clear()
    console.print(Panel(Text("Main Menu", justify="center")))
    console.print("1. [bold]List Reviews[/bold]")
    console.print("2. [bold]New Review[/bold]")
    console.print("3. [bold]Delete Review[/bold]")
    Option = Prompt.ask("Insert Your Option")

    if Option == "1":
        break
    elif Option == "2":
        break
    elif Option == "3":
        break
    elif Option == "exit!":
        break
    else:
        continue
