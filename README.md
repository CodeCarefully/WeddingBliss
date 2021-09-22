<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![maintenance][maintenance-shield]][maintenance-url]
[![python][python-shield]][python-url]
[![gpl][gpl-shield]][gpl-url]
[![coverage][coverage-shield]][coverage-url]
[<img src="https://gitpod.io/button/open-in-gitpod.svg" height="28px"/>](https://gitpod.io/#https://github.com/CodeCarefully/WeddingBliss)



 <h3 align="center">WeddingBliss</h3>

  <p align="center">
    Wedding invite system and manager
    <br />
    <a href="https://github.com/CodeCarefully/WeddingBliss/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/CodeCarefully/WeddingBliss/issues">Report Bug</a>
    ·
    <a href="https://github.com/CodeCarefully/WeddingBliss/issues">Request Feature</a>
  </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
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
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Weddings are supposed to be the "best part" of the relationship - the pinnacle of commitment.
It's a party you invite all your friends and family to.

But:

Weddings are a huge stressful mess - complicated by the lack of RSVPs, expensive markups and sheer inexperience at organizing huge parties.

I started building the original version of this site for my own wedding, years ago. Since then much has changed, including a global pandemic.
I've kept up, making many versions of this for all my friends.

The original PHP version had many flaws, including an utterly exhausting level of work required to build and design the backend pages.

I've been trying to make a Django version of the project for years, this is my latest, and hopefully last attempt at it.

### Built With

* [Django](https://www.djangoproject.com/)


<!-- GETTING STARTED -->
## Getting Started


### Prerequisites


### Installation


<!-- USAGE EXAMPLES -->
## Usage


_For more examples, please refer to the [Documentation](https://github.com/CodeCarefully/WeddingBliss)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/CodeCarefully/WeddingBliss/issues) for a list of proposed features (and known issues).

### Project Scope:

* Project Should be in Django, using the latest version
* Project should have the ability to send emails and SMS messages, with a configurable account. 
* Docker Deploy


### Flow:

#### For user:

	* User gets message, clicks link, is brought to site
	* Can see wedding info, including possible "zoom" or other meeting link
	* Given Options to RVSP and provide additional details
	* Get ICAL/Gcal links
	
	
#### For admin:

	* Add users with a range of details and permissions (email, phone number, who they can invite, etc..)
	* See stats like "Open rate"
	* Ability to auto-reach out based on stat criteria (people who didn't open, etc..)
	* see cute personalized messages as event approaches.
	* configure API keys for SMS and email sending service/SMTP
	* Customize template
	* secure backend login
	* ability to export site
	* Password Recovery
	* Seating arrangement?
	* Export people by various criteria to excel/CSV
	* Can set which meeting service they want (Zoom, etc..) and when it "starts"
	(to allow stateless services like Jitsi without losing moderator control)
	* Can change meeting links on the fly, since its just a redirector.
	* compliance with COVID regulations and TAV Yarok. Including fetching updates from COVID advisory sites.
	* save the date page, which lets you get basic info and add in your email? for updates.(simplepush?)
	* Populate data for Ical/Gcal links
	
	
	
### Random Thoughts:

I'd really like to use WebAuthN/social/djangoauth for the backend login to provide a range of options


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPLv3 Licence. See `LICENSE` for more information.



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

I'd like to thank my beautiful spouse for marrying me and giving me the idea.

Also Django. Thanks Django!




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[maintenance-shield]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
[maintenance-url]: https://github.com/CodeCarefully/WeddingBliss/graphs/commit-activity

[python-shield]: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
[python-url]: https://www.python.org/

[gpl-shield]: https://img.shields.io/badge/License-GPLv3-blue.svg
[gpl-url]: http://perso.crans.org/besson/LICENSE.html

[django-shield]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[django-url]: https://www.djangoproject.com/

[coverage-shield]: https://raw.githubusercontent.com/CodeCarefully/WeddingBliss/main/.github/badge/coverage.svg
[coverage-url]: https://github.com/CodeCarefully/WeddingBliss



