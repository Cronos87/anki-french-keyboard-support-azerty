# Author: Cronos87
from aqt import mw
from aqt.reviewer import Reviewer
from anki.hooks import wrap


__version__ = "0.0.1"

def shortcutKeys(self, _old):
    return [
            ("&", lambda: self._answerCard(1)),
            ("é", lambda: self._answerCard(2)),
            ('"', lambda: self._answerCard(3)),
            ("'", lambda: self._answerCard(4))
        ] + _old(self)


def answerCard(self, ease, _old):
    # Don't do nothing if the user select a button not available
    if ease <= self.mw.col.sched.answerButtons(self.card):
        _old(self, ease)


Reviewer._shortcutKeys = wrap(Reviewer._shortcutKeys, shortcutKeys, "around")
Reviewer._answerCard = wrap(Reviewer._answerCard, answerCard, "around")
