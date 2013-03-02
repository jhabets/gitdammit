from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from git import *


class DammitGame(Widget):
    untracked = NumericProperty(0)
    tracked = NumericProperty(0)

    #TODO setup methods for setting path
    localPath = "C:/Projects/ChubbyDragons"
    repo = None

    #called by Clock to update graphics
    def update(self, dt):
        if self.repo is None:
            self.repo = self.getRepo()
        self.untracked = self.getUntracked()
        self.tracked = self.getTracked()

    #utility methods
    def getRepo(self):
        return Repo(self.localPath)

    def getUntracked(self):
        gitString = ""
        gitString = self.repo.git.ls_files(o=True, exclude_standard=True)
        numUntracked = 0
        if len(gitString) > 0:
            numUntracked = len(gitString.split('\n'))
        return numUntracked

    def getTracked(self):
        gitString = ""
        gitString = self.repo.git.diff(staged=True, name_only=True)
        numUntracked = 0
        if len(gitString) > 0:
            numUntracked = len(gitString.split('\n'))
        return numUntracked


class DammitApp(App):
    def build(self):
        game = DammitGame()
        Clock.schedule_interval(game.update, 1.0 / 2.0)
        return game


if __name__ == '__main__':
    DammitApp().run()
