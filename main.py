from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.text import Text
from rich.live import Live
import os
import time
import subprocess


console = Console()


def animate_text(text, style="bold green", delay=0.05):
    for i in range(len(text) + 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        styled_text = Text(text[:i], style=style)
        console.print(styled_text)
        time.sleep(delay)


def typing_effect(text, style="bold cyan", delay=0.03):
    output = Text(style=style)
    for char in text:
        output.append(char)
        console.print(output, end="\r")
        time.sleep(delay)
    console.print(output)


def loading_animation():
    typing_effect(f"──────────────────── ─> [ LOADING ]", delay=0.05)
    for _ in track(range(100), description="[bold cyan]╭───────────────────────────\n[bold cyan]╰─> [ PROSES ]\n"):
        time.sleep(0.20)
    time.sleep(1)


def clear_screen_animation():
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Text(" ", style="on black"), justify="center")
        time.sleep(0.1)


def main_menu():
    clear_screen_animation()
    panel_content = (
        "[bold green]\n╋╋╋[bold blue]┏┓[bold green]╋[bold blue]┏┓[bold green]╋╋╋╋╋╋╋╋[bold blue]┏━┓[bold green]╋[bold blue]┏┓[bold green]╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋\n[bold green]╋[bold blue]┏━┛┃[bold green]╋[bold blue]┗┛[bold green]╋[bold blue]┏━━━┓[bold green]╋[bold blue]┏┛┗┓[bold green]╋[bold blue]┃┃[bold green]╋╋[bold blue]┏┓[bold green]╋[bold blue]┏┓[bold green]╋[bold blue]┏━━━┓[bold green]╋[bold blue]┏━━┓[bold green]╋\n[bold green]╋[bold blue]┃┏┓┃[bold green]╋[bold blue]┏┓[bold green]╋[bold blue]┣━━┃┃[bold green]╋[bold blue]┗┓┏┛[bold green]╋[bold blue]┃┃[bold green]╋╋[bold blue]┃┗━┛┃[bold green]╋[bold blue]┣━━┃┃[bold green]╋[bold blue]┃┃━┫[bold green]╋\n╋[bold blue]┃┗┛┃[bold green]╋[bold blue]┃┃[bold green]╋[bold blue]┃┃━━┫[bold green]╋╋[bold blue]┃┃[bold green]╋╋[bold blue]┃┗┓[bold green]╋[bold blue]┗━┓┏┛[bold green]╋[bold blue]┃┃━━┫[bold green]╋[bold blue]┃┃━┫[bold green]╋\n╋[bold blue]┗━━┛[bold green]╋[bold blue]┗┛[bold green]╋[bold blue]┗━━━┛[bold green]╋╋[bold blue]┗┛[bold green]╋╋[bold blue]┗━┛[bold green]╋[bold blue]┗━━┛[bold green]╋╋[bold blue]┗━━━┛[bold green]╋[bold blue]┗━━┛[bold green]╋\n╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋\n\n"
        "[bold yellow]╋╋╋ ALL SHOP MENU ╋╋╋[/]\n\n"
        "[1] SCRIPT DDOS\n"
        "[2] SCRIPT BRUTE FORCE\n"
        "[3] SCRIPT SPAM REPORT WA\n"
        "[4] SCRIPT SPAM REPORT IG\n"
        "[5] SCRIPT SPAM LIKE IG\n"
        "[6] SCRIPT VIEW TIKTOK\n"
        "[7] SCRIPT PHISHING\n"
        "[8] WA ANTI BANNED\n"
        "[9] TUTOR KEBAL BUG\n"
        "[0] EXIT\n"
    )
    animate_text("©LICENSI : [ SC SHOP DIZ FLYZE ]", style="bold yellow")
    console.print(
        Panel(panel_content, title="[bold green]DIZ SHOP[/]", border_style="bright_yellow")
    )


def transition_message(message, style="bold green"):
    os.system('cls' if os.name == 'nt' else 'clear')
    typing_effect(message, style=style)
    time.sleep(1)


def execute_choice(choice):
    if choice == "0":
        transition_message("GOOD BYE")
        clear_screen_animation()
        exit()
    elif choice in [str(i) for i in range(1, 10)]:
        transition_message(f"[ ANDA MEMILIH NOMER ] : {choice}")
        subprocess.run(["python", "register.py"])
    else:
        transition_message("TIDAK ADA PILIHAN ITU")

if __name__ == "__main__":
    loading_animation()
    while True:
        main_menu()
        console.print(f"\n[bold cyan]╭──────────────────────────────────")
        user_choice = console.input("[bold cyan]╰─> [ PILIH SCRIPT ] :")
        execute_choice(user_choice)