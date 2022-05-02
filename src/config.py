from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console

console = Console()
def config():
    # Create database.
    db = dbconfig()
    cursor = db.cursor()

    printc("[green][+] Creating new config .[/green]")

    try:
        cursor.execute("CREATE DATABASE passman")

    except Exception as e:
        printc("[red][!] An error occurred while trying to create database.")

        console.print_exception(show_locals = True)

        sys.exit(0)

    printc("[green][+][/green] Database 'passman' created.")

    # Create tables.
    query = "CREATE TABLE passman.secrets (masterkey_hash TEXT NOT NULL, device_secret TEXT NOT NULL)"
    res = cursor.executable(query)

    printc("[green][+][/green] Table 'secrets' created.")

    query = "CREATE TABLE passman.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL)"
    res = cursor.execute(query)

    printc("[green][+][/green] Table 'entries' created.")

    while 1:
        maspass = getpass("Choose a master password: ")

        if maspass != getpass("Re-type: ") and maspass !=
