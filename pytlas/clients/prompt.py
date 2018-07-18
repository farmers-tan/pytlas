
import cmd
from ..version import __version__
from ..agent import Agent

class PromptClient(cmd.Cmd):
  intro = 'pytlas prompt v%s' % __version__
  prompt = '> '

  def __init__(self, interpreter, refresh_handler=None):
    super(PromptClient, self).__init__()

    self._agent = Agent(interpreter, self)
    self._refresh_handler = refresh_handler
  
  def ask(self, slot, text, choices):
    print (text)

  def answer(self, text):
    print (text)

  def done(self):
    pass

  def do_exit(self, msg):
    return True

  def do_refresh(self, msg):
    if self._refresh_handler:
      self._refresh_handler()

  def default(self, msg):
    self._agent.parse(msg)