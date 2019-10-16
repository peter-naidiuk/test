
class ControllerRegistry:

    def add_controller(self, controller):
        setattr(self, controller.__name__, controller)
