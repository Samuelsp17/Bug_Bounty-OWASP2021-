import requests


files = [
    ".env", ".env.local", ".env.production", ".env.development", "config.php", "wp-config.php",
    "database.yml", "local.xml", "config.json", "config.ini", "settings.py", "settings.xml",
    "application.yml", "parameters.yml", ".env.example", ".env.bak", "config.old",
    "backup.sql", "db.sql", "database.sql", "dump.sql", "db_backup.sql", "backup.zip",
    "backup.tar.gz", "database.db", "database.sqlite", "mysql.dump", "mongodb.dump",
    "users.json", "users.csv", "debug.log", "error.log", "access.log", "server.log",
    "logs.txt", "laravel.log", "nohup.out", "database.log", "apache.log", "nginx.log",
    "mail.log", ".git/config", ".git/HEAD", ".git/logs/HEAD", ".svn/entries", ".hg/hgrc",
    "CVS/Root", "id_rsa", "id_rsa.pub", "authorized_keys", "private.key", "public.key",
    "jwt.secret", "jwt.private", "jwt.public", "ssh_config", "cert.pem", "cert.key",
    "server.key", "google_api_key.txt", "aws_secret.txt", "aws_credentials",
    ".htaccess", ".htpasswd", "web.config", "nginx.conf", "php.ini", "docker-compose.yml",
    "dockerfile", "vhost.conf", "apache2.conf", "my.cnf", "redis.conf", "ftpconfig",
    "admin.json", "admin.xml", "admin.ini", "admin.yml", "admin_panel.log",
    "superuser.txt", "root_access.log", "sysadmin.log"
]

site = "https://target.com/"

for file in files:
    url = site + file
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            print(f"[+] Encontrado: {url}")
            
        elif response.status_code == 403:
            print(f"[-] Acesso negado: {url}")
        else:
            print(f"[!] Não encontrado ({response.status_code}): {url}")

    except requests.exceptions.RequestException as e:
        print(f"[x] Erro ao acessar {url}: {e}")