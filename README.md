# Projet d'évaluation de l'unité DSIA_4201C Data Engineering 

## Table of Contents

- [Introduction](#introduction)
- [Installer](#installer)
- [Usage](#usage)
- [Structure du projet](#structure-du-projet)
   * [Scraping](#scraping)
   * [Base de données](#base-de-données)
   * [Scraping](#scraping)

## Introduction 

Ce projet consiste en la création d'une application avec Flask qui présente les meilleurs produits du site [Amazon](http://www.amazon.com) par catégorie. Pour cela nous avons d'abord scrappé les données à partir du site puis nous les avons stockées dans une base de données à laquelle accède l'application.

## Installer

Environment et Packages: Tous les détails sont dans Pipfile et Pipfile.lock.

Clonez le git repo avec la commande suivante:

```
git clone https://github.com/DelphineGambier/Projet_DSIA_4201C.git
```

## Usage

Exécutez "flask run" dans le terminal, normalement c'est comme suit après l'exécution.

```
E:\documents\DSIA_4201C - Data engineering\Projet>flask run
 * Environment: development
 * Debug mode: on
 * Restarting with windowsapi reloader
 * Debugger is active!
 * Debugger PIN: 808-186-928
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```
Entrez http://127.0.0.1:5000/, puis vous pouvez voir la page d'accueil.

## Structure du projet 

[setting.py](https://github.com/DelphineGambier/Projet_DSIA_4201C/blob/main/amazonSpider/settings.py) -> toutes les variables  et parametres utilisés

### Scraping

Nous avons scrapé le site [Amazon](http://www.amazon.com) à l'aide de Scrapy.
Le scraping s'effectue à l'aide des scripts :
 - [items.py](https://github.com/DelphineGambier/Projet_DSIA_4201C/blob/main/amazonSpider/items.py) qui défini le modèle pour les items qui seront scrappés.
 - [middlewares.py](https://github.com/DelphineGambier/Projet_DSIA_4201C/blob/main/amazonSpider/middlewares.py) qui permet de définir les méthodes dont nous avons besoin.
 - [pipelines.py](https://github.com/DelphineGambier/Projet_DSIA_4201C/blob/main/amazonSpider/pipelines.py) qui permet de définir la pipeline qui traîtera les items scrappés.

### Base de données

Nous avons utilisé une base de données Mongo pour stocker les données scrappées et pour pouvoir y accéder.

### Flask
