from configparser import ConfigParser
from functools import wraps
import os

DEFAULT_SECTION = 'pytlas'

config = ConfigParser()

# Needed to keep track of the settings file that has been loaded
config_loaded_from_path = None

# Here are builtin settings used by the library
SETTING_VERBOSE = 'verbose'
SETTING_DEBUG = 'debug'
SETTING_LANG = 'lang'
DEFAULT_SETTING_LANG = 'en'
SETTING_SKILLS = 'skills'
DEFAULT_SETTING_SKILLS = 'skills'
SETTING_CACHE = 'cache'
SETTING_DRY = 'dry'
SETTING_PARSE = 'parse'
SETTING_WATCH = 'watch'
SETTING_TRAINING_FILE = 'training_file'
SETTING_GRAPH_FILE = 'graph'

# Default parameters value
config[DEFAULT_SECTION] = {
  SETTING_LANG: DEFAULT_SETTING_LANG,
  SETTING_SKILLS: DEFAULT_SETTING_SKILLS,
}

def write_to_settings(section=DEFAULT_SECTION):
  """Simple decorator used to write each argument value to the settings
  if they're set and call the wrapped func without arguments.

  Args:
    section (str): Section to write the settings

  """

  def new(f):
    @wraps(f)
    def func(**kwargs):
      # Config is a specific key used to read the config from a file
      conf = kwargs.get('config')

      # And read it if it exists
      if conf and os.path.isfile(conf):
        global config_loaded_from_path
        config_loaded_from_path = os.path.abspath(conf)
        config.read(config_loaded_from_path)

      # And then, for each argument, write its value in the config object
      for (k, v) in kwargs.items():
        if v:
          config.set(section, k, str(v))

      return f()
    
    return func
  
  return new

def to_env_key(section, setting):
  """Convert a section and a setting to an environment key.

  Args:
    section (str): Section of the configuration
    setting (str): Setting key to look for

  Returns:
    str: Environment variable name

  Examples:
    >>> to_env_key('pytlas', 'lang')
    'PYTLAS_LANG'

  """

  return ('%s_%s' % (section, setting)).upper()

def set(setting, value, section=DEFAULT_SECTION):
  """Sets a setting value in the inner config.

  Value should be a string (since all value can be read from env variables).

  Args:
    setting (str): Setting key to write
    value (str): Value to write
    section (str): Section to write to

  """

  if section not in config:
    config[section] = {}

  config[section][setting] = value

  config.set(section, setting, value)

def get(setting, default=None, section=DEFAULT_SECTION):
  """Gets a setting value, if an environment variable is defined, it will take
  precedence over the value hold in the inner config object.

  For example, if you got a setting 'lang' in the 'pytlas' section, defining the
  environment varialbe PYTLAS_LANG will take precedence.

  Args:
    setting (str): Name of the configuration option
    default (str): Fallback value
    section (str): Section to look in

  Returns:
    str: Value of the setting

  """

  return os.environ.get(to_env_key(section, setting), config.get(section, setting, fallback=default))

def getbool(setting, default=False, section=DEFAULT_SECTION):
  """Gets a boolean value for a setting. It uses the get under the hood so the same
  rules applies.

  Args:
    setting (str): Name of the configuration option
    default (bool): Fallback value
    section (str): Section to look in

  Returns:
    bool: Value of the setting

  """

  v = get(setting, section=section)

  return config._convert_to_boolean(v) if v else default

def getint(setting, default=0, section=DEFAULT_SECTION):
  """Gets a int value for a setting. It uses the get under the hood so the same
  rules applies.

  Args:
    setting (str): Name of the configuration option
    default (int): Fallback value
    section (str): Section to look in

  Returns:
    int: Value of the setting

  """

  v = get(setting, section=section)

  return int(v) if v else default

def getfloat(setting, default=0.0, section=DEFAULT_SECTION):
  """Gets a float value for a setting. It uses the get under the hood so the same
  rules applies.

  Args:
    setting (str): Name of the configuration option
    default (float): Fallback value
    section (str): Section to look in

  Returns:
    float: Value of the setting

  """

  v = get(setting, section=section)

  return float(v) if v else default