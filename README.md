![image](https://github.com/user-attachments/assets/69c6ded0-82d0-40f9-a45a-33f6e54c2495)
![image](https://github.com/user-attachments/assets/11b8eefc-38da-4a48-8816-2e5ed30b1455)
![image](https://github.com/user-attachments/assets/ae9facce-4a0f-47d7-b1a7-ef1ae77ae6be)
![image](https://github.com/user-attachments/assets/d052e5ee-d4cd-424b-b9fb-95db33669c66)
![image](https://github.com/user-attachments/assets/370437d7-65a7-47a7-b043-14a38f8090df)




# 🛡️ MailDefender

**MailDefender** es una herramienta OSINT defensiva para Blue Team y SOC diseñada para analizar correos electrónicos sospechosos. Verifica exposición pública en brechas, datos WHOIS y registros DNS, e integra herramientas como `h8mail` y `theHarvester`.

---

## 🚀 Funcionalidades

- ✔️ Análisis de un solo correo electrónico (`-e`)
- 📁 Análisis masivo desde archivo (`-f`)
- 🔍 WHOIS del dominio
- 🌐 DNS Lookup: MX, SPF y DMARC
- 🔓 Verificación de filtraciones públicas con `h8mail`
- 🛰️ Recopilación de correos y hosts con `theHarvester`
- 🧪 Modo demo (`--demo`) para pruebas rápidas

---

## 📦 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/maildefender.git
cd maildefender
```

2. Instala dependencias:

```bash
pip install -r requirements.txt
```

3. Asegúrate de tener instaladas estas herramientas:
   - [`h8mail`](https://github.com/khast3x/h8mail): `pip install h8mail`
   - [`theHarvester`](https://github.com/laramies/theHarvester): clónala en `maildefender/theHarvester/`

---

## 🧪 Ejemplos de uso

### Análisis individual
```bash
python maildefender.py -e correo@example.com
```

### Análisis masivo
```bash
python maildefender.py -f correos.txt
```

### Modo demo (correo comprometido de prueba)
```bash
python maildefender.py --demo
```

---

## 📄 Salida esperada

- Datos WHOIS (nombre, país, creación)
- Registros MX, SPF y DMARC
- Resultado de `h8mail` (correos relacionados o comprometidos)
- Resultado de `theHarvester` (correos/hosts públicos)
- Consola enriquecida con `rich`

---

## 🛠 Requisitos

- Python 3.7+
- Conexión a Internet
- Acceso a consola

---

## 📘 Licencia

Proyecto open-source bajo licencia MIT.
