# Capstone Proposal  
#### Scott Harvey

## Name

**Insight**

## Project Overview

Combine security data platforms into one view to aid in research.

Shodan + SecurityTrails (formerly DNStrails) initially, with other inputs to be added if time allows.

## Functionality

Primary functionality will allow a user to input an IP address and search. Results from Shodan and SecurityTrails will be presented on the main page at the time of the search.

Certain data in the search results may be presented in link form to allow the user to repeat the search with that IP address.

Additional search criteria may be added if time allows.

The other idea behind this is to gather information about who is searching for which IPs. This will be used later, should that IP address be later associated with an attack. Providing a platform malicious actors could easily use for pre-attack reconnaissance could provide valuable intel for attribution.

## Data Model

- Primary model is the IP address. IP will be linked via foreign key to individual searches.

- Searches will contain the results of the search from all outside sources, will be linked to Sessions

- Sessions will contain info on the user performing the search. This will aid in later research.

## Schedule

January 

- Mon 14 / Tue 15 - Be familiar with API search results and have fields/data selected for presentation to the user.

- Wed 16 / Thur 17 - Have data models built in django and view(s) needed.

- Fri 18 / Sat 19 - Have completed templates and working site.

- Sun 20 / Mon 21 - Apply CSS and finalize
