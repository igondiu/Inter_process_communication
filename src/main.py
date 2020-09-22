import logging
import multiprocessing
import os
import sys

from flask import Flask, request, make_response, jsonify
from flask_restx import Api, Resource

sys.path.append(os.path.dirname(os.path.abspath("./app")))
import config.config as cfg
from src.setup.setup import logger_setup
from src.setup.flask_app import run_flask_app

from src.MotionDetector import MotionDetector

motion_detector = MotionDetector()
motion_vector_queue = multiprocessing.Queue()
detection_vector_queue = multiprocessing.Queue()

logger = logging.getLogger(__name__)

app = Flask(__name__)
API = Api(
    app,
    title="Inter-process communication",
    description="Documentation of the API of the inter-process communication module",
    doc="/doc",
    prefix="/test_upciti/api/v1",
)

STATUS_NS = API.namespace("STATUS", path="/")
POST_MESSAGE = API.namespace("Post message", path="/")


@app.route("/")
@app.route("/test_upciti/api/v1/")
def home():
    """ Default method : returns a simple page """
    return "<h1>TEST INTER-PROCESS  COMMUNICATION</h1><p>This is the first version of the API! Enjoy :).</p>"


@POST_MESSAGE.route('/post_message', methods=["POST"])
class PostMessage(Resource):
    @POST_MESSAGE.response(201, "Success")
    @POST_MESSAGE.response(400, "Bad input parameter")
    @POST_MESSAGE.response(500, "Internal server error")
    @POST_MESSAGE.doc(description="Creates a new message in the topic MotionVector")
    @POST_MESSAGE.param(
        "message", "The message to POST", "formData", required=True, type="string"
    )
    def post(self):
        """ Insert into the database rows from input file """
        if request.method == "POST":
            logger.info("POST request on [/test_upciti/api/v1/post_message] received")
            try:
                message = request.form.get("message")
                motion_detector_process = multiprocessing.Process(
                    target=motion_detector.post_message, args=(message, motion_vector_queue, detection_vector_queue))
                motion_detector_process.start()
                return make_response(jsonify({"Info": "created"}), 201)
            except Exception as e:
                logger.exception("An error has occurred in the function POST() of the class PostMessage : ".format(e))
                return make_response(jsonify({"ERROR": "Internal server error"}), 500)


@app.errorhandler(404)
def not_found(error):
    """ Function is called when the requested page was not found.

        Args:
            error: http_error (404 not found)
        Returns:
            http_response (404 not found)
    """
    return make_response(jsonify({'ERROR': '{}'.format(error)}), 404)


def main(config, flask_app):
    """Run the flask web application

        Args:
            flask_app (app): Flask application
            config (config file)
        """
    logger_setup(config)
    run_flask_app(flask_app)


if __name__ == '__main__':
    main(cfg, app)
