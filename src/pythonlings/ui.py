from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, MofNCompleteColumn, Progress, TextColumn
from rich.table import Table
from rich.text import Text

console = Console()


def print_success(exercise_name: str, current: int, total: int) -> None:
    console.print()
    console.print(f"[bold green]✅  Nice work! You solved {exercise_name}![/bold green]")
    console.print()
    _print_progress_bar(current, total)
    console.print()


def print_failure(exercise_name: str, error_output: str) -> None:
    console.print()
    console.print(f"[bold red]❌  Hmm, {exercise_name} didn't pass yet. Here's what happened:[/bold red]")
    console.print()
    if error_output.strip():
        console.print(Panel(error_output.strip(), border_style="red"))
    console.print()
    console.print("[yellow]💡 Run [bold]pythonlings hint[/bold] if you want more help.[/yellow]")
    console.print()


def print_hint(hint_text: str) -> None:
    console.print()
    console.print(Panel(hint_text.strip(), title="[bold yellow]💡 Hint[/bold yellow]", border_style="yellow"))
    console.print()


def print_info(message: str) -> None:
    console.print(f"[cyan]{message}[/cyan]")


def print_not_done_reminder(exercise_name: str) -> None:
    console.print()
    console.print(f"[bold yellow]⏳  {exercise_name} is not done yet![/bold yellow]")
    console.print("[yellow]When you're ready, delete the line that says:[/yellow]")
    console.print("[bold]    # I AM NOT DONE[/bold]")
    console.print("[yellow]Then save the file.[/yellow]")
    console.print()


def print_progress(completed: int, total: int) -> None:
    console.print()
    console.print("[bold cyan]🐍 Your Pythonlings Progress[/bold cyan]")
    console.print()
    _print_progress_bar(completed, total)
    pct = int(completed / total * 100) if total > 0 else 0
    console.print(f"\n[cyan]{completed}/{total} exercises done ({pct}%)[/cyan]")
    if completed == total:
        console.print("[bold green]🎉 You've completed all exercises! Amazing work![/bold green]")
    console.print()


def _print_progress_bar(completed: int, total: int) -> None:
    with Progress(
        TextColumn("    🐍 Progress:"),
        BarColumn(bar_width=30),
        MofNCompleteColumn(),
        console=console,
        transient=False,
    ) as progress:
        task = progress.add_task("", total=total, completed=completed)
        progress.stop()


def print_exercise_list(exercises: list[dict], completed_set: set[str]) -> None:
    table = Table(title="Pythonlings Exercises", show_header=True, header_style="bold cyan")
    table.add_column("#", style="dim", width=4)
    table.add_column("Exercise", style="bold")
    table.add_column("Path")
    table.add_column("Done?", justify="center")

    for i, ex in enumerate(exercises, 1):
        done = "✅" if ex["name"] in completed_set else "  "
        table.add_row(str(i), ex["name"], ex["path"], done)

    console.print(table)
