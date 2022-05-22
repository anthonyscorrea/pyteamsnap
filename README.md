<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is n optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div style="text-align:center;">
  <a href="https://github.com/anthonyscorrea/pyteamsnap">
    <img src="https://www.teamsnap.com/images/logo.svg" alt="Logo" width="160" height="80">
  </a>

<h3 style="text-align:center;">pyteamsnap</h3>

  <p style="text-align:center;">
    Unofficial TeamSnap API wrapper for python.
    <br />
    ·
    <a href="https://github.com/anthonyscorrea/pyteamsnap/issues">Report Bug</a>
    ·
    <a href="https://github.com/anthonyscorrea/pyteamsnap/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

An unoffical python wrapper for the [TeamSnap API](https://www.teamsnap.com/documentation/apiv3). A work in progress.

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>



### Built With

* [api-client](https://github.com/MikeWooster/api-client)
* [collection-json](https://github.com/ricardokirkner/collection-json.python)

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* [api-client](https://github.com/MikeWooster/api-client)
  ```shell
  pip install api-client
  ```
* [collection-json](https://github.com/ricardokirkner/collection-json.python)
  ```shell
  pip install json-collection
  ```

### Installation

1. Get OAuth 2 Credentials from TeamSnap at [https://auth.teamsnap.com/](https://auth.teamsnap.com/login) ([TeamSnap Documentation](https://www.teamsnap.com/documentation/apiv3/authorization))
2. Install pyteamsnap
      ```shell
      pip install git+https://github.com/anthonyscorrea/pyteamsnap
      ```

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage Example

  ```python
  from pyteamsnap.api import TeamSnap, Me, Event, EventLineupEntries, Member
  client = TeamSnap(token=TOKEN)
  
  # get authenticated user
  me = Me(client)
  
  # get a list of team_ids for the user
  managed_team_ids = me.data['managed_teams']
  
  # get a list of events for managed team
  managed_team_id = me.data['managed_teams'][0]
  events = Event.search(client, team_id=managed_team_id)
  
  # get an object with the object id of EVENT_ID 
  event = Event.get(client, id=EVENT_ID)
  
  # get some information about the event
  start_date = event.data['start_date']
  
  # create a new member
  member = Member.new(client)
  member.data['first_name'] = 'Ferguson'
  member.post()
  
  # update a Member with id of MEMBER_ID
  member = Member.get(client, id=MEMBER_ID)
  member.data['last_name'] = 'Jenkins'
  member.put()
  
  # delete a Member
  member.delete()
  
  # perform a bulk load
  list_of_ts_objects = client.bulk_load(team_id = TEAM_ID, types = [Event, Member], event__id=EVENT_ID)
  ```
  

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

Implemented objects
- [X] Me
- [X] User
- [X] Event
- [X] Team
- [X] Availability
- [X] Member
- [X] Location
- [X] Opponent
- [X] EventLineupEntry
- [X] EventLineup
- [X] AvailabilitySummary

Implemented Queries
- [x] search
- [x] bulk_load

Implemented Actions
- [x] create
- [x] read
- [x] update
- [x] destroy

Implemented objects, but not tested.
- [ ] Statistics
- [ ] MemberStatistics

See the [open issues](https://github.com/anthonyscorrea/pyteamsnap/issues) for a full list of proposed features (and known issues).

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@anthonyscorrea](https://twitter.com/anthonyscorrea) - a@correa.co

Project Link: [https://github.com/anthonyscorrea/pyteamsnap](https://github.com/anthonyscorrea/pyteamsnap)

<p style="text-align:right;">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/anthonyscorrea/pysteamsnap.svg?style=for-the-badge
[contributors-url]: https://github.com/anthonyscorrea/pyteamsnap/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/anthonyscorrea/pysteamsnap.svg?style=for-the-badge
[forks-url]: https://github.com/anthonyscorrea/pyteamsnap/network/members
[stars-shield]: https://img.shields.io/github/stars/anthonyscorrea/pysteamsnap.svg?style=for-the-badge
[stars-url]: https://github.com/anthonyscorrea/pyteamsnap/stargazers
[issues-shield]: https://img.shields.io/github/issues/anthonyscorrea/pysteamsnap.svg?style=for-the-badge
[issues-url]: https://github.com/anthonyscorrea/pyteamsnap/issues
[license-shield]: https://img.shields.io/github/license/anthonyscorrea/pysteamsnap.svg?style=for-the-badge
[license-url]: https://github.com/anthonyscorrea/pyteamsnap/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/anthonyscorrea
[product-screenshot]: images/screenshot.png