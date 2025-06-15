📦 Instrucciones para subir tu bot a Render

1. Sube estos archivos a un repositorio de GitHub (usa el botón "Add file" > "Upload files")
2. Entra a https://render.com
3. Inicia sesión con tu cuenta de GitHub
4. Crea un nuevo "Web Service" y conecta tu repositorio
5. Configura así:
   - Build Command: pip install -r requirements.txt
   - Start Command: python bot.py
   - Environment → añade una variable:
       BOT_TOKEN = tu_token_de_@BotFather
6. Haz clic en "Create Web Service"
7. Espera a que se instale todo y el bot estará activo 24/7

💡 Consejo: el horario del bot se puede cambiar dentro de bot.py
