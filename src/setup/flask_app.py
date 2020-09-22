import logging

from config.config import (
    FLASK_PORT,
    FLASK_SSL_PORT,
    FLASK_DEBUG_MODE,
    FLASK_HOST,
    FLASK_SSL_CERT,
    FLASK_PRIVATE_KEY,
)

log = logging.getLogger(__name__)


def run_flask_app(app):
    """ Runs a webportal where the client is able to upload files or get data.

    Args :
        app
    """
    try:
        if FLASK_SSL_CERT and FLASK_PRIVATE_KEY:
            app.run(
                debug=FLASK_DEBUG_MODE,
                port=FLASK_SSL_PORT,
                ssl_context=(FLASK_SSL_CERT, FLASK_PRIVATE_KEY),
            )
            log.info("FLASK is running on %s on port %s", FLASK_HOST, FLASK_SSL_PORT)
        else:
            app.run(debug=FLASK_DEBUG_MODE, port=FLASK_PORT, host=FLASK_HOST)
            log.info("FLASK is running on %s on port %s", FLASK_HOST, FLASK_PORT)
    except Exception as exception:
        log.error("An error has occurred while trying to launch FLASK : %s", exception)
