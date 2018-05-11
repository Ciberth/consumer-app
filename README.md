# Consumer app

This charm is an example of a consumer application using the generic-database interface (TODO LINK) and the generic-database charm (TODO LINK). It makes uses of the apache layer, setting up and deploying a website, a few php pages, simulating a webshop (TODO LINK) making use of databases through a generic-database.

## Overview of interesting/used links & documentation

(TODO updating LINKS)

- [Consumer-app](https://github.com/Ciberth/consumer-app) (this repository)
- [Generic-database charm](https://github.com/Ciberth/generic-database)
- [Generic-database interface](https://github.com/Ciberth/generic-database-layer)
- [Charms reactive / endpoint pattern](https://charmsreactive.readthedocs.io/en/latest/charms.reactive.relations.html?#charms.reactive.endpoints.Endpoint)



## Concept of a generic-database

The idea behind the generic-database is that it acts as a proxy between the requesting/requiring charm and a providing charm for a database. Imagine a webshop in need of a mysql database and the mysql charm. The generic-database charm would be the intermediate charm to make this connection happen.

For more details about the concepts/ideas and use cases refer to the generic-database charm (TODO LINK)

## An exploratory example

This charm also functions as a charm following the recent concepts and patterns of modern (anno May 2018) charm development. It uses the reactive framework, more specifically the [Endpoint pattern](https://charmsreactive.readthedocs.io/en/latest/charms.reactive.relations.html?#charms.reactive.endpoints.Endpoint). This charm should therefore be a good example in using and working with Endpoints and flags (previously states).


## Concrete information of the consumer app

Todo



