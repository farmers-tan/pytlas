.. _interpreter:

Interpreter
===========

Interpreter allow pytlas to categorize user intents and to extract slots from raw text. Whatever interpreter you decide to use, it will need training data to be able to understand what's the user intent behind an input sentence.

Intent
------

An intent represents a user intention.

For example, when I say *what's the weather like?*, my intent is something as *get weather*. When I say *please tell me what's the weather like today*, it maps to the same intent *get weather*.

Slot
----

A slot is like a parameter value for a function. It represents an entity in the context of an intent.

So when I say *what's the weather like in Paris?*, my intent is *get weather* and the slot *city* should be *Paris*.

Implementing a custom interpreter
---------------------------------

If you wish to implement your own interpreter, you must at least extends from `pytlas.interpreters.Interpreter` and implement those methods.

.. note::

  When creating `SlotValue` instance to represent a slot, always remember to sets a value in a meaningfull python representation. See :ref:`retrieving_slots` to see what's expected by developers.

.. py:function:: fit(data)

  Fit the interpreter with training data.

.. py:function:: parse(msg, scopes=None)
  :noindex:

  Parse a raw message and returns an intents list. *scopes* is an optional list of allowed intent names.

.. py:function:: parse_slot(intent, slot, msg)

  Parse a slot for a given context.
