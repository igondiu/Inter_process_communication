from src.MotionVector import MotionVector


class MotionDetector:
    """ Publisher """

    def post_message(self, message, motion_vector_queue):
        """ Creates a new instance of class MotionVector and adds it to the queue """
        motion_vector = MotionVector(message)
        motion_vector_queue.put(motion_vector)
