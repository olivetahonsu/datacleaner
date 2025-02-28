# Import necessary libraries
import typer
import pandas as pd
import logging
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, BarColumn, TimeElapsedColumn
from rich.prompt import Confirm
import shutil


from src.cleaner import DataCleaner


app = typer.Typer()
console = Console()


# Configure logging
LOG_FILE = "datacleaner.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


@app.command()
def check_missing(file: str):

    """Check missing values in a CSV file."""

    df = pd.read_csv(file)
    cleaner = DataCleaner(df)

    with Progress(SpinnerColumn(), BarColumn(), TimeElapsedColumn()) as progress:
        task = progress.add_task("[cyan]Checking missing values...", total=1)
        missing_summary = cleaner.check_missing_values()
        progress.update(task, advance=1)

    if missing_summary.empty:
        console.print("[bold green]No missing values found![/bold green]")
        logging.info("No missing values found in the dataset")
    else:
        table = Table(title="Missing Values Summary")
        table.add_column("Column", style="cyan", justify="left")
        table.add_column("Missing Count", style="red", justify="right")

        for column, count in missing_summary.items():
            table.add_row(column, str(count))

        console.print(table)
        logging.info(f"Missing values found: \n{missing_summary}")


@app.command()
def clean(file: str):
    """Interactively clean missing values in a CSV file."""
    df = pd.read_csv(file)
    cleaner = DataCleaner(df)
    missing_summary = cleaner.check_missing_values()

    if missing_summary.empty:
        console.print("[bold green]No missing values found! Nothing to clean.[/bold green]")
        return

    with Progress(SpinnerColumn(), BarColumn(), TimeElapsedColumn()) as progress:
        for column in missing_summary.index:
            console.print(f"\n[bold yellow]Column: [/bold yellow] {column} "
                          f"[bold red]Missing Value:[/bold red] {missing_summary[column]}")
            method = typer.prompt("Choose method (drop/mean/median/mode/fill)")

            task = progress.add_task(f"[cyan]Cleaning {column}...", total=1)

        if method == "fill":
            fill_value = typer.prompt(f"Enter custom value for {column}")
            cleaner.handle_missing_values(column, method, fill_value)
        else:
            cleaner.handle_missing_values(column, method)

        progress.update(task, advance=1)

    # Preview cleaned data
    console.print("\n[bold cyan]Preview of cleaned data:[/bold cyan]")
    console.print(cleaner.get_cleaned_data().head())

    # Ask user if they want to save
    if Confirm.ask("\nDo you want to save the cleaned data?", default=True):
        cleaner.get_cleaned_data().to_csv("cleaned_data.csv", index=False)
        console.print("[bold green]Cleaned data saved to cleaned_data.csv[/bold green]")
        logging.info("Data cleaning completed and saved to cleaned_data.csv")
    else:
        console.print("[bold red]Data was not saved.[/bold red]")


@app.command()
def export_logs(destination: str = "logs_backup.log"):
    """Export the log file to a different location for debugging."""
    try:
        shutil.copy(LOG_FILE, destination)
        console.print(f"[bold green]Logs exported to {destination}[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Failed to export logs: {str(e)}[/bold red]")


@app.command()
def clear_logs():
    """Clear the log file."""
    try:
        open(LOG_FILE, "w").close()    # Truncate the file
        console.print("[bold green]Log file cleared successfully.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Failed to clear logs: {str(e)}[/bold red]")


if __name__ == "__main__":
    app()
