import logging
from multiprocessing import Process
from src.MotionVector import MotionVector
from src.SingleShotDetector import SingleShotDetector
from src.Logger import Logger

logger = logging.getLogger(__name__)

logger_instance = Logger()
ssd = SingleShotDetector()


class MotionDetector:
    """ Publisher """
    exec_once = False

    def post_message(self, message, motion_vector_queue, detection_vector_queue):
        """ Creates a new instance of class MotionVector and adds it to the queue """
        motion_vector = MotionVector(message)
        motion_vector_queue.put(motion_vector)
        logger.debug("Starting all processes ...")
        if not MotionDetector.exec_once:
            MotionDetector.exec_once = True
            single_shot_detector_process = Process(
                target=ssd.write_detection_vector, args=(motion_vector_queue, detection_vector_queue))
            single_shot_detector_process.start()
            logger_vector_process_1 = Process(target=logger_instance.consume_motion_vector, args=(motion_vector_queue,))
            logger_vector_process_1.start()
            logger_vector_process_2 = Process(
                target=logger_instance.consume_detection_vector, args=(detection_vector_queue,))
            logger_vector_process_2.start()
            logger.debug("All processes where started.")
