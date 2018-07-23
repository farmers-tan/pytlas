class Client:
  """Base interface for a client to implement.
  """

  def __init__(self, agent=None):
    """Instantiates a new Client for the given agent.

    Args:
      agent (Agent): Agent tied to this client
    """

    self._agent = agent

  def parse(self, msg):
    """Parses the given message.

    Args:
      msg (str): Raw message to parse
    
    """

    if self._agent:
      self._agent.parse(msg)

  def ask(self, slot, text, choices):
    """Ask will be called by the agent when a skill needs more information to go on.

    Args:
      slot (str): Slot to fill
      text (str): Text to show to the user
      choices (list): Optional list of choices to restrict user values

    """

    pass

  def answer(self, text):
    """Answer will be called by the agent to display informations to the user.

    Args:
      text (str): Text to show to the user

    """
    
    pass

  def done(self):
    """Done will be called by the agent when a skill has ended its work. This is
    usefull when you are displaying some activity indicator upon an agent.parse call
    
    """

    pass