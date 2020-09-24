import logging
import multiprocessing as mp
import random
import time
import config.config as cfg

logger = logging.getLogger(__name__)


class Logger:
    """ Consumes objects from MotionVector & DetectionVector topics """

    def consume_motion_vector(self, motion_vector_queue: mp.Queue):
        """ Will take message from the motion_vector_queue and log them to standard output.
        If the message was not yet processed by other processes, it is put in a list and at the end of the while loop
        the process is put back to the queue.

        Args:
            motion_vector_queue (queue): contains all the message that must be printed

        """
        while cfg.continue_processing:
            not_yet_processed_by_ssd = []
            while not motion_vector_queue.empty():
                motion_vector = motion_vector_queue.get()
                if not motion_vector.read_by_logger:
                    motion_vector.read_by_logger = True
                    logger.info("\nMessage from the MotionVector Topic : \n")
                    logger.info(motion_vector)
                    print("\nMessage from the MotionVector Topic : \n", motion_vector)
                if not motion_vector.read_by_ssd:
                    not_yet_processed_by_ssd.append(motion_vector)
            for motion_vector in not_yet_processed_by_ssd:
                motion_vector_queue.put(motion_vector)
            time.sleep(random.randrange(1, 5))

    def consume_detection_vector(self, detection_vector_queue: mp.Queue):
        """ Will take message from the detection_vector_queue and log them to standard output.

        Args:
            detection_vector_queue (queue): contains all the message that must be printed

        """
        while cfg.continue_processing:
            while not detection_vector_queue.empty():
                detection_vector = detection_vector_queue.get()
                logger.info("\nMessage from the DetectionVector Topic : \n")
                logger.info(detection_vector)
                print("\nMessage from the DetectionVector Topic : \n", detection_vector)
            time.sleep(random.randrange(1, 5))
