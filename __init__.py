from mycroft import MycroftSkill, intent_file_handler


class LupeTheRobot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('robot.the.lupe.intent')
    def handle_robot_the_lupe(self, message):
        self.speak_dialog('robot.the.lupe')


def create_skill():
    return LupeTheRobot()

