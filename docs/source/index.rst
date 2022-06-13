.. vimlib documentation master file, created by
   sphinx-quickstart on Mon May 23 23:22:07 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to vimlib's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Installation
============

``pip install vimlib``

**Recommended**: Using your chosen virtual environment, that's been setup for
Vim, or Neovim, to use, install ``vimlib`` using that.

Examples:

* ``~/vimfiles/.venv/bin/pip.exe install --upgrade vimlib``
* ``cd ~/vimfiles && poetry install vimlib``

Usage
=====

Current
-------

``vimlib`` offers a convenient way to interact with the current environment, much
like Vim's built-in current object.

.. code-block:: python
  from pyvim import current

Echo
----

`vimlib` offers a convenient way to print to Vim's stdout in a colorful, and
flexible, manner.

.. code-block:: python
  import pyvim


  # Print to STDOUT
  pyvim.echo("Hello!")
  # Print with chosen highlight group
  pyvim.echo("Hello!", "PyVimSuccess")  # Built-In Green
  pyvim.echo("Hello!", "PyVimCaution")  # Built-In Yellow
  pyvim.echo("Hello!", "PyVimDanger")   # Built-In Red

Highlight Groups
----------------

``vimlib`` offers a convenient way to interact with highlight groups.

.. code-block:: python
  from pyvim import current


  # Boolean. Check if a highlight group is available
  has_highlight = 'MyHighlightGroup' in pyvim.current.highlights

Visual Selection
----------------

``vimlib`` offers a convenient way to interact with highlighted text. Also
highlights the most recent highlighted text.

.. code-block:: python
  from pyvim import current


  # String with the current, or last, selection.
  # Support basic, linewise, and block visual highlights
  selection = pyvim.current.selection

Utilities
---------

``vimlib`` offers convenient utilities.

System Commands
===============

*Note: Chaining will stack ``<CR>`` and other tokens.*

.. code-block:: python
  from pyvim.utilities import wrap_vim_command


  wrapped_command: str = wrap_vim_command(
      command="!py %",
      silent=True,
      clear=True,
  )

  print(wrapped_command)
  # ":<C-U>silent !py %<CR>

Examples

.. code-block:: python
  >>> print(wrap_vim_command('w'))
  :<C-u>w<CR>

.. code-block:: python
  >>> print(wrap_vim_command('w!', silent=True))
  :<C-u>silent w!<CR>

Mappings
--------

``vimlib`` offers a convenient way to interact Vim mappings.

.. code-block:: python
  >>> import pyvim
  >>>
  >>>
  >>> # Set <Leader>r to write current buffer to disk.
  >>> # Equivalent to `:nmap <Leader>r :<C-u>silent w<CR>` in Vim.
  >>> set_mapping('nmap', '<Leader>r', ':<C-u>silent w<CR>')

Function
--------

**WARNING: Non-Working**

``vimlib`` offers a convenient way to interact Vim functions.

.. code-block:: python
  import pyvim


  vim_function = pyvim.Function(
      name="Foo",
      arguments=None,
      optional_arguments=True,
      overwrite=True,
  )

  result = vim_function(...)

Job
---

**WARNING: Non-Working**

``vimlib`` offers a convenient way to interact Vim jobs and channels.

.. code-block:: python
  import pyvim


  vim_job = pyvim.Job(
      cmd='python -m http.server',
  )

  vim_job.stop()
  vim_job.status

Registers
---------

``vimlib`` offers a convenient way to interact Vim registers.

.. code-block:: python
  >>> import pyvim.Register

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
