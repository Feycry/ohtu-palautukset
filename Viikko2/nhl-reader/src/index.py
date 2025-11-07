from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box

def main():
    console = Console()
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    
    console.print(Panel.fit(
        "[bold cyan]NHL Statistics[/bold cyan]\n[dim]Season 2024-25[/dim]",
        border_style="cyan"
    ))
    
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    
    while True:
        console.print()
        nationality = Prompt.ask(
            "[bold yellow]Select nationality[/bold yellow] [dim][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS][/dim]"
        ).strip().upper()
        
        if not nationality:
            console.print("[red]Exiting...[/red]")
            break
            
        players = stats.top_scorers_by_nationality(nationality)
        
        if not players:
            console.print(f"[red]No players found for nationality: {nationality}[/red]")
            continue
        
        console.print()
        console.print(f"[bold green]Season 2024-25 players from {nationality}[/bold green]\n")
        
        table = Table(box=box.SIMPLE)
        table.add_column("Released", style="cyan")
        table.add_column("teams", style="magenta")
        table.add_column("goals", justify="right", style="green")
        table.add_column("assists", justify="right", style="green")
        table.add_column("points", justify="right", style="green")
        
        for player in players:
            table.add_row(
                player.name,
                player.team,
                str(player.goals),
                str(player.assists),
                str(player.score)
            )
        
        console.print(table)


if __name__ == "__main__":
    main()
