==========
pyteamsnap
==========


.. image:: media/pyteamsnap_logo.svg
    :width: 75%
    :align: center
    :alt: TeamSnap Logo


An unofficial python wrapper for the `TeamSnap API <https://www.teamsnap.com/documentation/apiv3>`_. A work in progress.

Installation
------------

Install **pyteamsnap** from GitHub

.. code-block:: console

    $ pip install git+https://github.com/anthonyscorrea/pyteamsnap

Getting Started
---------------

To connect to TeamSnap, get OAuth 2 Credentials from TeamSnap at `https://auth.teamsnap.com/ <https://auth.teamsnap.com/login>`_ (`TeamSnap Documentation <https://www.teamsnap.com/documentation/apiv3/authorization>`_)

.. code-block:: python

    from pyteamsnap.client import TeamSnap
    client = TeamSnap(token=TOKEN)

You can use pyteamsnap constructors in pyteamsnap models to create instances.

Getting the user object for the authenticated user.

.. code-block:: python

    >>> from pyteamsnap.models import Me

    >>> me = Me(client)

    >>> me
    TeamSnap<User:00000000> "FirstName LastName"

There is only one "Me" for a session, so no searching required.

Information can be accessed using keys just like a dictionary. See `documentation <https://anthonyscorrea.github.io/pyteamsnap/>`_ for each models' ``data`` property for a list of available keys.

A few examples:

.. code-block:: python

    >>> managed_teams = me['managed_teams']

    >>> managed_teams
    [TeamSnap<Team:00000000> "TeamName"]

    >>> team = managed_teams[0]

    >>> team['name']
    TeamName

Objects have a search function, where search criteria is passed as keyword arguments

.. code-block:: python

    >>> from pyteamsnap.models import Event

    >>> events = Event.search(client, team_id=team['id'])

    >>> events
    [Teamsnap<Event:00000000> "Event Title", TeamSnap<Event:00000001> "Event Title"]

    >>> event = events[0]

    >>> event['start_date']
    datetime.datetime(2000, 1, 1, 12, 00, 00, 0)

Objects can be retrieved singularly with an id.

.. code-block:: python

    >>> event = Event.get(client, 00000000)

    >>> event
    TeamSnap<Event:00000000> "Event Title"

Objects can be created, updated, and deleted (as permissions allow).

.. code-block:: python

    >>> from pyteamsnap import Member

    >>> new_member = Member.new(client)

    >>> new_member['first_name'] = 'Ferguson'

    >>> new_member['last_name'] = 'Jenkins'

    >>> member.post()
    TeamSnap<Member:00000001> "Ferguson Jenkins"

    >>> member['jersey_number'] = 31

    >>> member.put()

    >>> member.delete()

To load a hetereogeneous list of objects given parameters, the ``bulk_load`` function can be used

.. code-block:: python

    >> list_of_ts_objects = client.bulk_load(team_id = TEAM_ID, types = [Event, Member], event__id=00000001)
    [TeamSnap<Event:00000001> "Event Title", TeamSnap<Member:00000000> "Ferguson Jenkins"]

Documentation
-------------

`Documentation can be found here. <https://anthonyscorrea.github.io/pyteamsnap/>`_
