![image](https://github.com/user-attachments/assets/69c6ded0-82d0-40f9-a45a-33f6e54c2495)
![image](https://github.com/user-attachments/assets/11b8eefc-38da-4a48-8816-2e5ed30b1455)
![image](https://github.com/user-attachments/assets/ae9facce-4a0f-47d7-b1a7-ef1ae77ae6be)
![image](https://github.com/user-attachments/assets/d052e5ee-d4cd-424b-b9fb-95db33669c66)
![image](https://github.com/user-attachments/assets/370437d7-65a7-47a7-b043-14a38f8090df)




# 🛡️ MailDefender (Multiplataforma: Windows y Linux)

**MailDefender** es una herramienta OSINT defensiva para Blue Team y SOC que analiza correos electrónicos sospechosos usando WHOIS, DNS, h8mail y theHarvester. Su objetivo es detectar indicios de phishing o exposición pública.

---

## 🚀 Funcionalidades principales

- ✔️ Análisis individual de correos (`-e`)
- 📁 Análisis masivo desde archivo (`-f`)
- 🔍 WHOIS del dominio
- 🌐 DNS Lookup: MX, SPF y DMARC
- 🔓 Verificación de filtraciones públicas con `h8mail`
- 🛰️ Recopilación OSINT con `theHarvester`
- 🧪 Modo demo (`--demo`)
- 🎨 Consola enriquecida con `rich`

---

# 🪟 Versión para Windows

### ✅ Requisitos

- Python 3.8 o superior
- Consola CMD o PowerShell
- Conexión a Internet

### 🧩 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/U7Dani/maildefender.git
cd maildefender
```

2. Instala las dependencias de Python:

```bash
pip install -r requirements.txt
```

3. Verifica que las herramientas estén disponibles:

- `h8mail`: `pip install h8mail`
- `theHarvester`: clónala en el directorio principal:
```bash
git clone https://github.com/laramies/theHarvester.git
```

### ▶️ Ejecución

Analizar un correo individual:
```bash
python maildefender.py -e correo@example.com
```

Analizar varios desde archivo:
```bash
python maildefender.py -f correos.txt
```

Modo demostración:
```bash
python maildefender.py --demo
```

---

# 🐧 Versión para Linux

### ✅ Requisitos

- Python 3.8 o superior
- Terminal Bash
- Conexión a Internet

### 🧩 Instalación

1. Instala herramientas del sistema:

```bash
sudo apt update
sudo apt install whois dnsutils
```

2. Clona el repositorio:

```bash
git clone https://github.com/U7Dani/maildefender.git
cd maildefender
```

3. Instala dependencias de Python:

```bash
pip install -r requirements.txt
```

4. Herramientas externas:

- `h8mail`: `pip install h8mail`
- `theHarvester`:
```bash
git clone https://github.com/laramies/theHarvester.git
```

### ▶️ Ejecución

Analizar un correo:
```bash
python maildefender.py -e correo@example.com
```

Analizar archivo de correos:
```bash
python maildefender.py -f correos.txt
```

Ejecutar modo demo:
```bash
python maildefender.py --demo
```

---

## 📄 Salida esperada

- Información WHOIS del dominio
- Registros DNS: MX, SPF, DMARC
- Resultados de exposición en bases de datos filtradas (`h8mail`)
- Emails/hosts públicos encontrados con `theHarvester`
- Consola clara y visual gracias a `rich`

---

## 📦 Estructura del proyecto

```
maildefender/
├── maildefender.py
├── requirements.txt
├── README.md
└── theHarvester/  ← (opcional si se integra)
```

---

## 👨‍💻 Autor

Desarrollado por [@U7Dani](https://github.com/U7Dani)

---

## 📘 Licencia

Distribuido bajo licencia MIT.

