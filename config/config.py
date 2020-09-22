import os
from distutils.util import strtobool
import platform

# ===================================DIRECTORIES==========================================

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_DIR = os.path.join(ROOT_DIR, "tests")
LIB_DIR = os.path.join(ROOT_DIR, "lib")
LOG_DIR = os.path.join(ROOT_DIR, "logs")

# ================================== FLASK ==============================================
FLASK_PORT = (
    os.getenv("FLASK_WINDOWS_PORT", 5000)
    if platform.system() == "Windows"
    else os.getenv("FLASK_DEFAULT_PORT", 5000)
)
FLASK_SSL_PORT = os.getenv("FLASK_SSL_PORT", 5000)
FLASK_SSL_PORT_WIN = (
    os.getenv("FLASK_WINDOW_SSL_PORT")
    if platform.system() == "Windows"
    else FLASK_SSL_PORT
)
FLASK_DEBUG_MODE = strtobool(os.getenv("FLASK_DEBUG_MODE", "true"))
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_SSL_CERT = os.getenv("FLASK_CERT", None)
FLASK_PRIVATE_KEY = os.getenv("FLASK_PRIVATE_KEY", None)

# ================================== MySQL ==============================================
MYSQL_ADMIN_PASSWORD = (os.getenv("MYSQL_ROOT_PASSWORD", "root"))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "opencellid")
MYSQL_USER = os.getenv("MYSQL_USER", "test")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "supersecret")
MYSQL_HOST = os.getenv("MYSQL_HOST", "database")

# ===================================PROGRAM OPTIONS==========================================
LOG_VERBOSITY = strtobool(os.getenv("LOG_VERBOSITY", "true"))
