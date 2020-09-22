import datetime


class DetectionVector:
    """ Topic """
    frames = 0

    def __init__(self, message):
        DetectionVector.frames += 1
        self.creation_date = datetime.datetime.utcnow()
        self.frame_id = DetectionVector.frames
        self.message_content = message

    def __str__(self):
        """ Method return the object as a string """
        return "\nTimestamp : {}\nFrame ID : {}\nMessage content : {} ".format(
            str(self.creation_date), str(self.frame_id), self.message_content)

    def __repr__(self):
        return self.__str__()
