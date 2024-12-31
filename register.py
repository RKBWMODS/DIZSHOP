import random
import string
from faker import Faker
from fake_useragent import UserAgent
import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.text import Text
from rich.table import Table
from datetime import datetime


fake = Faker()
ua = UserAgent()
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
    typing_effect("──────────────────── ─> [ LOADING ]", delay=0.05)
    for _ in track(range(100), description="[bold cyan]╭───────────────────────────\n[bold cyan]╰─> [ PROSES ]\n"):
        time.sleep(0.20)
    time.sleep(0.5)


def generate_random_cookie():
    device_id = "".join(random.choices(string.ascii_letters + string.digits, k=32))
    user_id = str(fake.random_int(min=1000000000000, max=9999999999999))
    referring_domain = fake.domain_name()
    initial_referrer = f"https://{referring_domain}/"
    cookie = {
        "mp_device_id": device_id,
        "mp_user_id": user_id,
        "initial_referrer": initial_referrer,
        "initial_referring_domain": referring_domain,
    }
    return "; ".join([f"{key}={value}" for key, value in cookie.items()])


def show_panel():
    os.system('cls' if os.name == 'nt' else 'clear')  
    panel_content = (
        "[bold green]\n╋╋╋[bold blue]┏┓[bold green]╋[bold blue]┏┓[bold green]╋╋╋╋╋╋╋╋[bold blue]┏━┓[bold green]╋[bold blue]┏┓[bold green]╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋\n[bold green]╋[bold blue]┏━┛┃[bold green]╋[bold blue]┗┛[bold green]╋[bold blue]┏━━━┓[bold green]╋[bold blue]┏┛┗┓[bold green]╋[bold blue]┃┃[bold green]╋╋[bold blue]┏┓[bold green]╋[bold blue]┏┓[bold green]╋[bold blue]┏━━━┓[bold green]╋[bold blue]┏━━┓[bold green]╋\n[bold green]╋[bold blue]┃┏┓┃[bold green]╋[bold blue]┏┓[bold green]╋[bold blue]┣━━┃┃[bold green]╋[bold blue]┗┓┏┛[bold green]╋[bold blue]┃┃[bold green]╋╋[bold blue]┃┗━┛┃[bold green]╋[bold blue]┣━━┃┃[bold green]╋[bold blue]┃┃━┫[bold green]╋\n╋[bold blue]┃┗┛┃[bold green]╋[bold blue]┃┃[bold green]╋[bold blue]┃┃━━┫[bold green]╋╋[bold blue]┃┃[bold green]╋╋[bold blue]┃┗┓[bold green]╋[bold blue]┗━┓┏┛[bold green]╋[bold blue]┃┃━━┫[bold green]╋[bold blue]┃┃━┫[bold green]╋\n╋[bold blue]┗━━┛[bold green]╋[bold blue]┗┛[bold green]╋[bold blue]┗━━━┛[bold green]╋╋[bold blue]┗┛[bold green]╋╋[bold blue]┗━┛[bold green]╋[bold blue]┗━━┛[bold green]╋╋[bold blue]┗━━━┛[bold green]╋[bold blue]┗━━┛[bold green]╋\n╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋\n\n"
        "[bold yellow]PEMBUAT   : DIZFLYZE[/]\n"
        "[bold yellow]YOUTUBE   : DIZFLYZE999[/]\n"
        "[bold yellow]VERSION   : 2.0 MEGA[/]\n"
        f"[bold green]WAKTU     : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}[/]"
    )
    animate_text("© LICENSE : [ DIZFLYZE SHOP ]", style="bold yellow")
    console.print(Panel(panel_content, title="[bold green]INFO[/]", border_style="blue"))


def transition_message(message, style="bold green"):
    os.system('cls' if os.name == 'nt' else 'clear')
    typing_effect(message, style=style)
    time.sleep(1)


def show_summary(email, phone, owner_name, password, cookie):
    os.system('cls' if os.name == 'nt' else 'clear')
    table = Table(title="[bold yellow][ BERIKUT DATA REGISTRASI ANDA ]", title_style="bold green")
    table.add_column("[bold cyan]STATUS", style="bold cyan", justify="left")
    table.add_column("[bold yellow]BERHASIL", style="bold yellow", justify="left")
    table.add_row("EMAIL ANDA", email)
    table.add_row("NOMER ANDA", phone)
    table.add_row("NAMA ANDA", owner_name)
    table.add_row("PASSWORD ANDA ", password)
    table.add_row("COOKIE ANDA", cookie)
    console.print(table)


def registration_process():
    loading_animation()
    show_panel()

    
    console.print(f"\n[bold yellow]╭──────────────────────────────────")
    email = console.input("[bold yellow]╰─> [ EMAIL ] :")
    console.print(f"\n[bold yellow]╭──────────────────────────────────")
    phone_number = console.input("[bold yellow]╰─> [ NOMER 62-8XX ] :")
    console.print(f"\n[bold yellow]╭──────────────────────────────────")
    owner_name = console.input("[bold yellow]╰─> [ NAMA ANDA ] :")
    console.print(f"\n[bold yellow]╭──────────────────────────────────")
    password = console.input("[bold yellow]╰─> [ PASSWORD ] :")

    
    cookie = generate_random_cookie()

    
    transition_message(f"[ MENYIAPKAN DATA ANDA ]")
    show_summary(email, phone_number, owner_name, password, cookie)

    
    console.print("\n[bold cyan]TRANSFER DANA KE 081387603153 SEBANYAK 60.000 UNTUK PEMBELIAN 1 SCRIPT DAN\nKIRIMKAN BUKTI TRANSFER DANA ANDA")
    console.print("[bold yellow]https://link.dana.id/[/]")
    os.system("xdg-open https://link.dana.id/")

    
    confirm = console.input("\n[bold yellow][ KIRIMKAN BUKTI TRANSFER ] ?\n[bold red]? [bold yellow]y/n : [/]").lower()
    if confirm == "y":
        transition_message("[ KIRIMKAN BUKTI TRANSFER ]")
        order_details = f"🤑 SAYA SUDAH ORDER BANG DAN SUDAH TF🥰 BUKTINYA SEBAGAI BERIKUT INI BANG🤗"
        os.system(f"xdg-open 'https://wa.me/6288980724038?text={order_details}'")
    else:
        transition_message("FUCK YOU")

if __name__ == "__main__":
    registration_process()