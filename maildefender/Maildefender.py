# MailDefender: Herramienta OSINT defensiva para SOC

"""
MailDefender es una herramienta OSINT enfocada en Blue Team y SOC para analizar correos electrónicos sospechosos.
Incluye reputación (sin API), brechas de datos, WHOIS, DNS, análisis masivo, h8mail y theHarvester.
"""

import argparse
import requests
import json
import sys
import os
import socket
import whois
import dns.resolver
import subprocess
from email.utils import parseaddr
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from bs4 import BeautifulSoup

console = Console()

# ---------------------- FUNCIONES ---------------------- #

def validar_email(email):
    return '@' in parseaddr(email)[1]

def extraer_dominio(email):
    return email.split('@')[-1]

def consultar_reputacion_publica(dominio):
    return "[amarillo]Reputación pública omitida por configuración[/amarillo]"

def consultar_whois(dominio):
    try:
        return whois.whois(dominio)
    except Exception as e:
        return {"error": f"Error en WHOIS: {str(e)}"}

def consultar_dns(dominio):
    resultado = {"MX": [], "SPF": [], "DMARC": []}
    try:
        mx = dns.resolver.resolve(dominio, 'MX')
        resultado["MX"] = [str(r.exchange) for r in mx]
    except:
        resultado["MX"] = ["No encontrados"]
    try:
        txt = dns.resolver.resolve(dominio, 'TXT')
        for r in txt:
            t = r.to_text()
            if "v=spf1" in t:
                resultado["SPF"].append(t)
            if "v=DMARC1" in t:
                resultado["DMARC"].append(t)
    except:
        resultado["SPF"] = ["No encontrados"]
        resultado["DMARC"] = ["No encontrados"]
    return resultado

def ejecutar_h8mail(email):
    try:
        result = subprocess.run(["h8mail", "-t", email], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error ejecutando h8mail: {str(e)}"

def ejecutar_theharvester(dominio):
    try:
        result = subprocess.run([
            "python", "theHarvester/theHarvester.py", "-d", dominio, "-l", "100", "-b", "bing"
        ], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"[!] Error ejecutando theHarvester: {str(e)}"

# ---------------------- FORMATO RICH ---------------------- #

def mostrar_resultados(email, reputacion, whois_data, dns_data, h8, th):
    console.rule(f"[bold cyan]Análisis de: {email}")

    console.print(Panel.fit(reputacion, title="[white on blue] Reputación pública (Talos) ", border_style="blue"))

    console.print(Panel.fit("Información WHOIS", title="[white on magenta] WHOIS ", border_style="magenta"))
    if isinstance(whois_data, dict) and 'error' in whois_data:
        console.print(f"[red]{whois_data['error']}")
    else:
        tabla = Table(title="Dominio registrado")
        tabla.add_column("Campo", style="cyan")
        tabla.add_column("Valor", style="white")
        for k in ['name', 'org', 'country', 'creation_date']:
            tabla.add_row(k, str(whois_data.get(k, 'N/A')))
        console.print(tabla)

    console.print(Panel.fit("Registros DNS", title="[white on green] DNS Lookup ", border_style="green"))
    for t, v in dns_data.items():
        tabla_dns = Table(title=f"Registros {t}")
        tabla_dns.add_column("Valor", style="white")
        for val in v:
            tabla_dns.add_row(val)
        console.print(tabla_dns)

    console.print(Panel.fit(h8 or "Sin resultados", title="[white on red] Brechas públicas (H8mail) ", border_style="red"))
    console.print(Panel.fit(th or "Sin resultados", title="[white on purple] theHarvester ", border_style="purple"))

# ---------------------- EJECUCIÓN ---------------------- #

def analizar_correo(email):
    dominio = extraer_dominio(email)
    reputacion = consultar_reputacion_publica(dominio)
    whois_data = consultar_whois(dominio)
    dns_data = consultar_dns(dominio)
    h8 = ejecutar_h8mail(email)
    th = ejecutar_theharvester(dominio)
    mostrar_resultados(email, reputacion, whois_data, dns_data, h8, th)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--email", help="Correo a analizar")
    parser.add_argument("-f", "--file", help="Archivo con correos")
    parser.add_argument("--demo", action="store_true", help="Ejecutar prueba con correo comprometido")
    args = parser.parse_args()

    if args.demo:
        demo_email = "test@evilcorp.com"
        analizar_correo(demo_email)
        return

    if args.email:
        if not validar_email(args.email):
            console.print("[red][!] Correo no válido")
            sys.exit(1)
        analizar_correo(args.email)

    elif args.file:
        if not os.path.exists(args.file):
            console.print("[red][!] Archivo no encontrado")
            sys.exit(1)
        with open(args.file, "r") as f:
            correos = [line.strip() for line in f if line.strip() and '@' in line]
        for correo in correos:
            analizar_correo(correo)
    else:
        console.print("[yellow][!] Usa -e para un correo, -f para archivo o --demo para modo prueba")

if __name__ == "__main__":
    main()
