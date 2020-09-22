import logging
import multiprocessing as mp
import time
import random
from src.DetectionVector import DetectionVector

logger = logging.getLogger(__name__)


class SingleShotDetector:
    """ Publisher and Subscriber """

    def write_detection_vector(self, motion_vector_queue: mp.Queue, detection_vector_queue: mp.Queue):
        """ Function takes messages from the motion_vector_queue,
        process them and puts them in the detection vector queue.
        Both queues are shared between processes, so messages must be
        deleted only when every process worked with the message already.
        To be sure that on message was not already processed by the same process, flags are used.


        Args:
            motion_vector_queue (queue): where to get data
            detection_vector_queue (queue): where to write data

        """
        while True:
            not_yet_processed_by_logger = []
            while not motion_vector_queue.empty():
                motion_vector = motion_vector_queue.get()
                if not motion_vector.read_by_ssd:
                    detection_vector = DetectionVector(motion_vector.message_content)
                    detection_vector_queue.put(detection_vector)
                if not motion_vector.read_by_logger:
                    motion_vector.read_by_ssd = True
                    not_yet_processed_by_logger.append(motion_vector)
            for motion_vector in not_yet_processed_by_logger:
                motion_vector_queue.put(motion_vector)
            time.sleep(random.randrange(1, 5))
