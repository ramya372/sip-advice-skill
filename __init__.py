from mycroft import MycroftSkill, intent_file_handler


class SipAdvice(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('advice.sip.intent')
    def handle_advice_sip(self, message):
        self.speak_dialog('advice.sip')


def create_skill():
    return SipAdvice()

