#Inheritance_and_method_overriding

class logger:
    def log(self,message):
        print(f"Log: {message}")


class advancedlogger(logger):
    def log(self,message):
        super().log(message)
        print(f"Advanced Log: {message.upper()}")

logger = advancedlogger()
logger.log("system error")


