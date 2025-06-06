from Implementation.goal_model import GoalModel
from Implementation.enums import LinkType

def create_model():
    model = GoalModel()

    model.add_task("T1")
    model.add_task("T2")
    model.add_task("T3")
    model.add_task("T4")
    model.add_task("T5")
    model.add_task("T6")
    model.add_task("T7")
    model.add_task("T8")

    model.add_goal("G1")
    model.add_goal("G2")
    model.add_goal("G3")

    model.add_quality("Q1")

    model.add_link("G3", "T8", LinkType.AND)
    model.add_link("T1", "T6", LinkType.AND)
    model.add_link("G1", "T2", LinkType.OR)
    model.add_link("Q1", "G2", LinkType.BREAK)
    model.add_link("Q1", "G1", LinkType.MAKE)
    model.add_link("G1", "T1", LinkType.OR)
    model.add_link("G3", "T1", LinkType.AND)
    model.add_link("T1", "T7", LinkType.AND)
    model.add_link("G2", "T3", LinkType.AND)
    model.add_link("G2", "T5", LinkType.AND)
    model.add_link("G2", "T4", LinkType.AND)

    model.requirements = {
        "G3": [['T8', 'T1']],
        "T1": [['T6', 'T7']],
        "G1": [['T2'], ['T1']],
        "G2": [['T3', 'T5', 'T4']],
    }

    model.add_event_mapping("e1", "T1")
    model.add_event_mapping("e2", "T2")
    model.add_event_mapping("e3", ["T3", "G3"])
    model.add_event_mapping("e4", "T4")
    model.add_event_mapping("e5", "T5")
    model.add_event_mapping("e6", "T6")
    model.add_event_mapping("e7", "T7")
    model.add_event_mapping("e8", "G1")


    return model
