from utils.dbconfig import dbconfig
from rich import print as printc
from rich.console import Console

console = Console()

def generateDeviceSecret(length = 10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))

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

        if maspass != getpass("Re-type: ") and maspass != "":
            break

        printc("[yellow][-] Please try again.[/yellow]")

    # Hash the master password.
    hashed_maspass = hashlib.sha256(masspass.encode()).hexdigest()

    printc("[green][+][/green] Generated hash of master password.")

    # Generate device secret.
    ds = generateDeviceSecret()

    printc("[green][+][/green] Device secret generated.")

    query = "INSERT INTO passman.secrets (masterkey_hash, device_secret) values (%s, %s)"
    val = (hashed_maspass, ds)
    cursor.execute(query, vals)

    db.commit()

    printc("[green][+][/green] Added to the database.")
    printc("[green][+] Configuration done![/green]")

    db.close()

config()
