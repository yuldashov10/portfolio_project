"""
This module defines reserved usernames, which contain predefined
keywords and phrases that are prohibited from being used as
usernames or any user-identifiable terms in publicly accessible systems.

The reserved names are categorized as follows:

- System-related and administrative terms.
- Network and protocol terms.
- Security-sensitive terms.
- Profane language.
- Terms with sexual connotations.
- Slang or crude language.
- Terms related to advertising, media, or other content.
"""

__all__ = ["RESTRICTED_USERNAMES"]

RESTRICTED_USERNAMES: dict[str, tuple[str, ...]] = {
    "SYSTEM_RESERVED_NAMES": (
        "about",
        "access",
        "account",
        "accounts",
        "add",
        "address",
        "adm",
        "admin",
        "administration",
        "administrator",
        "ajax",
        "analytics",
        "android",
        "api",
        "app",
        "apps",
        "archive",
        "atom",
        "backup",
        "billing",
        "bin",
        "blog",
        "blogs",
        "board",
        "business",
        "calendar",
        "campaign",
        "careers",
        "cgi",
        "client",
        "cliente",
        "code",
        "comercial",
        "compare",
        "compras",
        "config",
        "connect",
        "contact",
        "contest",
        "core",
        "create",
        "css",
        "dashboard",
        "data",
        "db",
        "delete",
        "demo",
        "dev",
        "devel",
        "developer",
        "dir",
        "directory",
        "directorydoc",
        "docs",
        "domain",
        "download",
        "downloads",
        "ecommerce",
        "edit",
        "editor",
        "email",
        "faq",
        "favorite",
        "feed",
        "file",
        "files",
        "free",
        "ftp",
        "games",
        "group",
        "groups",
        "help",
        "home",
        "homepage",
        "host",
        "hosting",
        "hostname",
        "html",
        "http",
        "https",
        "index",
        "info",
        "information",
        "intranet",
        "invite",
        "ipad",
        "iphone",
        "java",
        "javascript",
        "job",
        "jobs",
        "js",
        "knowledgebase",
        "list",
        "lists",
        "log",
        "login",
        "logout",
        "logs",
        "mail",
        "mail1",
        "mail2",
        "mail3",
        "mail4",
        "mail5",
        "mailer",
        "mailing",
        "manager",
        "marketing",
        "master",
        "media",
        "message",
        "microblog",
        "microblogs",
        "mobile",
        "mp3",
        "msg",
        "msn",
        "mysql",
        "network",
        "new",
        "news",
        "newsletter",
        "nick",
        "nickname",
        "notes",
        "noticias",
        "ns",
        "ns1",
        "ns2",
        "ns3",
        "ns4",
        "old",
        "operator",
        "owner",
        "page",
        "pager",
        "pages",
        "panel",
        "password",
        "perl",
        "php",
        "plugin",
        "plugins",
        "pop",
        "pop3",
        "post",
        "postmaster",
        "poweruser",
        "profile",
        "project",
        "projects",
        "promo",
        "pub",
        "public",
        "python",
        "random",
        "register",
        "registration",
        "root",
        "rss",
        "ruby",
        "sale",
        "sales",
        "sample",
        "samples",
        "script",
        "scripts",
        "secure",
        "send",
        "service",
        "setting",
        "settings",
        "setup",
        "shop",
        "signin",
        "signup",
        "site",
        "sitemap",
        "sites",
        "smtp",
        "sql",
        "ssh",
        "stage",
        "staging",
        "start",
        "stat",
        "static",
        "stats",
        "status",
        "store",
        "stores",
        "subdomain",
        "sudo",
        "support",
        "superuser",
        "sys",
        "system",
        "tablet",
        "tablets",
        "tech",
        "telnet",
        "test",
        "test1",
        "test2",
        "test3",
        "tests",
        "theme",
        "themes",
        "tmp",
        "tools",
        "update",
        "upload",
        "url",
        "usage",
        "user",
        "username",
        "usuario",
        "video",
        "videos",
        "visitor",
        "web",
        "webmail",
        "webmaster",
        "website",
        "websites",
        "win",
        "ww",
        "www",
        "www1",
        "www2",
        "www3",
        "www4",
        "www5",
        "www6",
        "www7",
        "wwws",
        "wwww",
    ),
    "NETWORK_RESERVED_NAMES": (
        "access",
        "anon",
        "anonymous",
        "avatar",
        "bin",
        "bot",
        "bots",
        "cache",
        "chat",
        "cookie",
        "designer",
        "dns",
        "feedback",
        "follow",
        "ftp",
        "guest",
        "hpg",
        "http",
        "httpd",
        "https",
        "imap",
        "indice",
        "ip",
        "irc",
        "log",
        "login",
        "mail",
        "mailbox",
        "me",
        "mx",
        "name",
        "named",
        "net",
        "online",
        "pic",
        "pics",
        "pop3",
        "postfix",
        "smtp",
        "ssh",
        "static",
        "talk",
        "tcp",
        "teste",
        "tv",
        "udp",
        "webmaster",
        "wws",
        "you",
        "yourdomain",
        "yourname",
        "yoursite",
        "yourusername",
    ),
    "SECURITY_RESERVED_NAMES": (
        "auth",
        "authentication",
        "cadastro",
        "encryption",
        "firewall",
        "order",
        "orders",
        "rootaccess",
        "secure",
        "security",
        "soporte",
        "ssl",
        "subscribe",
        "suporte",
    ),
    "PROFANE_RESERVED_NAMES": (
        "anal",
        "anus",
        "arse",
        "ass",
        "balls",
        "ballsack",
        "bastard",
        "biatch",
        "bitch",
        "bloody",
        "bollock",
        "bollok",
        "bugger",
        "bum",
        "butt",
        "clitoris",
        "cock",
        "crap",
        "cunt",
        "damn",
        "dick",
        "dyke",
        "fag",
        "feck",
        "fellate",
        "flange",
        "fuck",
        "god",
        "goddamn",
        "hell",
        "homo",
        "jerk",
        "jizz",
        "knob",
        "knobend",
        "lmao",
        "lmfao",
        "muff",
        "nigga",
        "nigger",
        "omg",
        "penis",
        "piss",
        "poop",
        "prick",
        "pube",
        "pussy",
        "queer",
        "scrotum",
        "sex",
        "sh1t",
        "shit",
        "slut",
        "smegma",
        "spunk",
        "tit",
        "tosser",
        "turd",
        "twat",
        "vagina",
        "wank",
        "whore",
        "wtf",
    ),
    "RACIAL_OFFENSIVE_NAMES": (
        "coon",
        "dyke",
        "fag",
        "nigga",
        "nigger",
        "spic",
        "wetback",
    ),
    "SEXUAL_OFFENSIVE_NAMES": (
        "adult",
        "ballsack",
        "blowjob",
        "boner",
        "boob",
        "buttplug",
        "clitoris",
        "cock",
        "cunt",
        "dick",
        "dildo",
        "felching",
        "fellatio",
        "fuck",
        "jizz",
        "labia",
        "muff",
        "penis",
        "pube",
        "pussy",
        "queer",
        "sex",
        "slut",
        "tit",
        "vagina",
        "wank",
        "whore",
        "xxx",
    ),
    "VULGAR_RESERVED_NAMES": (
        "arse",
        "balls",
        "bollocks",
        "bugger",
        "end",
        "fudge",
        "fudgepacker",
        "packer",
        "tosser",
        "turd",
        "wanker",
    ),
    "CONTENT_RESERVED_NAMES": (
        "advertising",
        "affiliate",
        "affiliates",
        "banner",
        "banners",
        "design",
        "flog",
        "forum",
        "forums",
        "ftpgadget",
        "gadgets",
        "image",
        "images",
        "img",
        "messenger",
        "mine",
        "mob",
        "movie",
        "movies",
        "music",
        "musicas",
        "my",
        "photo",
        "photoalbum",
        "photos",
        "posts",
        "search",
        "task",
        "tasks",
        "todo",
        "vendas",
        "workshop",
        "xpg",
    ),
}
