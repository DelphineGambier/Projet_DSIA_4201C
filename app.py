

from flask import Flask, render_template, url_for
import subprocess
import pymongo

app = Flask(__name__)
@app.route('/')
def index():
    subprocess.check_output("scrapy crawl amazon")
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    db = connection["amazon"]
    collection = db["les3premier"]
    data = list(collection.find())

    data_ordre = {}
    for p in data:
        if p['departement'] in data_ordre.keys():
            data_ordre[p['departement']].append(p)
        else:
            data_ordre[p['departement']] = [p]

    departement = list(data_ordre.keys())
    return render_template('index.html', data=data_ordre, departement = departement, categories_url=categories_url)

@app.route('/afficheplus/<departement>')
def depart(departement):
    ll = "scrapy crawl departement -a category="+departement
    subprocess.check_output(ll)
    connection = pymongo.MongoClient("mongodb://localhost:27017")
    db = connection["amazon"]
    collection = db["produits"]
    data = list(collection.find())

    return render_template('detail.html', data=data, departement=list(categories_url.keys())[list(categories_url.values()).index(departement)])


categories_url = {'Amazon Launchpad': 'boost', 'Animalerie': 'pet-supplies',
                      'Appareils Amazon et Accessoires': 'amazon-devices',
                      'Applis et Jeux': 'mobile-apps', 'Auto et Moto': 'automotive',
                      'Bagages': 'luggage', 'Beauté et Parfum': 'beauty',
                      'Bijoux': 'jewelry', 'Boutique Kindle': 'digital-text',
                      'Boutique chèques-cadeaux': 'gift-cards', 'Bricolage': 'hi',
                      'Bébé et Puériculture': 'baby', 'CD et Vinyles': 'music',
                      'Chaussures et Sacs': 'shoes', 'Commerce, Industrie et Science': 'industrial',
                      'Cuisine et Maison': 'kitchen', 'DVD et Blu-ray': 'dvd',
                      'Epicerie': 'grocery', 'Fournitures de bureau': 'officeproduct',
                      'Gros électroménager': 'appliances', 'High-Tech': 'electronics',
                      'Hygiène et Santé': 'hpc', 'Informatique': 'computers',
                      'Instruments de musique et Sono': 'musical-instruments', 'Jardin': 'lawn-garden',
                      'Jeux et Jouets': 'toys', 'Jeux vidéo': 'videogames',
                      'Livres': 'books', 'Livres anglais et étrangers': 'english-books',
                      'Livres audio Audible & Originals': 'audible', 'Logiciels': 'software',
                      'Luminaires & Eclairage': 'lighting', 'Montres': 'watch',
                      'Produits Handmade': 'handmade', 'Sports et Loisirs': 'sports', 'Vêtements': 'apparel'}