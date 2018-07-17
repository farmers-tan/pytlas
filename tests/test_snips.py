import unittest
from unittest.mock import patch, mock_open

snips_imported = True

try:
  from pytlas.interpreters.snips import SnipsInterpreter
except ImportError:
  snips_imported = False

def snips_available(func):
  """Check if snips is imported before executing the test
  """

  def new(*args, **kwargs):
    if not snips_imported:
      return args[0].skipTest('snips could not be imported')

    return func(*args, **kwargs)

  return new
    

class SnipsTests(unittest.TestCase):

  @snips_available
  @patch('builtins.open')
  def test_parse(self, open_mock):
    interp = self._prepare_interpreter(open_mock)
    intents = interp.parse('will it rain on Paris tomorrow')

    self.assertEqual(1, len(intents))

  @snips_available
  @patch('builtins.open')
  def test_parse_slot(self, open_mock):
    interp = self._prepare_interpreter(open_mock)

  def _prepare_interpreter(self, open_mock):
    open_mock.side_effect = [
      mock_open(read_data="""
{
  "intents": {
    "lights_on": {
      "utterances": [
        {"data": [{"text": "turn lights on please"}]},
        {"data": [{"text": "i want some lights"}]},
        {"data": [{"text": "lights on"}]},
        {"data": [{"text": "turn the lights on please"}]}
      ]
    },
    "lights_off": {
      "utterances": [
        {"data": [{"text": "please turn the lights off"}]},
        {"data": [{"text": "turn lights off please"}]},
        {"data": [{"text": "can you turn the lights off"}]},
        {"data": [{"text": "turn the lights off please"}]},
        {"data": [{"text": "gimme some obscurity"}]}
      ]
    },
    "get_forecast": {
      "utterances": [
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "London", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "London", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "London", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "London", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "London", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "what's the weather like in "},
            {"text": "London", "slot_name": "city", "entity": "location"},
            {"text": " on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "London", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Rouen", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "monday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "London", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it be sunny on "},
            {"text": "sunday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "Paris", "slot_name": "city", "entity": "location"}
          ]
        },
        {
          "data": [
            {"text": "will it rain on "},
            {"text": "tuesday", "slot_name": "date", "entity": "snips/datetime"},
            {"text": " in "},
            {"text": "London", "slot_name": "city", "entity": "location"}
          ]
        }
      ]
    }
  },
  "entities": {"snips/datetime": {}, "location": { "use_synonyms": true, "automatically_extensible": true, "data": [] }},
  "language": "en"
}
""").return_value,
      mock_open(read_data='').return_value,
    ]

    interp = SnipsInterpreter('example', False)
    interp.fit_as_needed()

    return interp