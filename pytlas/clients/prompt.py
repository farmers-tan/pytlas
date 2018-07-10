
import cmd
from ..version import __version__
from ..agent import Agent
from ..skill import handlers

class PromptClient(cmd.Cmd):
  intro = 'pytlas prompt v%s' % __version__
  prompt = '> '

  def __init__(self, interpreter):
    super(PromptClient, self).__init__()

    self._agent = Agent(interpreter, self, handlers)
  
  def ask(self):
    pass

  def answer(self):
    pass

  def end(self):
    pass

  def do_exit(self, msg):
    return True

  def default(self, msg):
    self._agent.parse(msg)