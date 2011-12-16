import sys
import xbmcaddon
import xbmcgui

Addon = xbmcaddon.Addon('script.get_action_id')

__scriptname__ = Addon.getAddonInfo('name')
__path__ = Addon.getAddonInfo('path')

ACTION_UP = 3
ACTION_MOUSE_MOVEMENT = 107

class GUI(xbmcgui.WindowXMLDialog):

    def onInit(self):
        self.label = self.getControl(3300)

    def onAction(self, action):
        action_id = action.getId()
        if action_id != ACTION_MOUSE_MOVEMENT:  # skip mouse movement
            if action_id == ACTION_UP:
                self.closeDialog()
            else:
                self.label.setLabel('ID of last action was: "%s"' % action_id)

    def closeDialog(self):
        self.close()


if (__name__ == "__main__"):
    ui = GUI('script-Get action ID-main.xml', __path__, 'default')
    ui.doModal()
    del ui

sys.modules.clear()
