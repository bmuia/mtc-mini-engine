from rich.console import Console
from rich.panel import Panel
import time
import webbrowser

console = Console()

class Zapper:
    def __init__(self, default_url='http://localhost:8000/register/'):
        self.default_url = default_url

    def openbrowserregister(self, url=None):
        final_url = url or self.default_url
        console.print(Panel("[bold green]Welcome to Zipper CLI! Let's create your account[/bold green]", title="Zipper CLI"))
        console.print(Panel(f"[yellow]Opening your browser for registration at: {final_url}[/yellow]", title="Zipper CLI"))
        time.sleep(2)
        webbrowser.open(final_url)
        console.print(Panel("[bold blue]Browser opened! Complete your registration there.[/bold blue]", title="Zipper CLI"))

    def openbrowserlogin(self, url=None):
        final_url = url or self.default_url
        console.print(Panel("[bold green]Welcome back to Zipper CLI! Please log in[/bold green]", title="Zipper CLI"))
        console.print(Panel(f"[yellow]Opening your browser for login at: {final_url}[/yellow]", title="Zipper CLI"))
        time.sleep(2)
        webbrowser.open(final_url)
        console.print(Panel("[bold blue]Browser opened! Complete your login there.[/bold blue]", title="Zipper CLI"))
