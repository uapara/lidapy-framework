from lidapy.framework.module import FrameworkModule
from lidapy.framework.msg import built_in_topics
from lidapy.framework.process import FrameworkTask

from lidapy.util import logger

# By default, the name of the module is the name of the ros node; however, this
# behavior can be overridden by passing a name to the initializer.
MODULE_NAME = "action_selection"

# Topics used by this module
SELECTED_BEHAVIORS_TOPIC = built_in_topics["selected_behaviors"]
CANDIDATE_BEHAVIORS_TOPIC = built_in_topics["candidate_behaviors"]
GLOBAL_BROADCAST_TOPIC = built_in_topics["global_broadcast"]


class ActionSelection(FrameworkModule):
    def __init__(self, name=MODULE_NAME, **kwargs):
        super(ActionSelection, self).__init__(name, **kwargs)

    @classmethod
    def get_module_name(cls):
        return MODULE_NAME

    def add_publishers(self):
        self.add_publisher(SELECTED_BEHAVIORS_TOPIC)

    def add_subscribers(self):
        self.add_subscriber(CANDIDATE_BEHAVIORS_TOPIC)
        self.add_subscriber(GLOBAL_BROADCAST_TOPIC)

    def call(self):
        candidate_behaviors = self.get_next_msg(CANDIDATE_BEHAVIORS_TOPIC)

        if candidate_behaviors is not None:
            selected_behaviors = candidate_behaviors

            self.publish(SELECTED_BEHAVIORS_TOPIC, selected_behaviors)
