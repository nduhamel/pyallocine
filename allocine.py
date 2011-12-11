#encoding:utf-8
#       allocine.py
#
#       Copyright 2011 nicolas <nicolas@jombi.fr>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
import urllib
import urllib2
import json


PARTNER = 'YW5kcm9pZC12M3M'

def search(q, format=None, filter=None, count=None, page=None):
    """
    URL : http://api.allocine.fr/rest/v3/search
    Paramètres
        partner : code partenaire (YW5kcm9pZC12M3M pour l'application Android)
        q : chaîne à chercher (chaîne de caractères)
        format (optionnel) : renvoie le résultat au format JSON ou XML (json ou xml)
        filter (optionnel) : filtrer selon un type de résultat (énumeration de termes séparés par des virgules)
            movie : afficher les films correspondant à la recherche
            theater : afficher les cinémas
            person : afficher les acteurs, réalisateurs, etc. (personnes)
            news : afficher les news
            tvseries : afficher les séries TV
        count (optionnel) : nombre de résultats à renvoyer (entier)
        page (optionnel) : numéro de la page de résultats à afficher (10 résultats par page par défaut)
    """
    format = format or 'json'
    count = count or 10
    page = page or 1
    filter = filter or ['movie','tvseries']
    filter = ','.join(filter)
    dataget = urllib.urlencode({ 'q':q,
                             'partner': PARTNER,
                             'format': format,
                             'filter': filter,
                             'count': count,
                             'page': page,
                            })
    rep = urllib2.urlopen('http://api.allocine.fr/rest/v3/search?'+dataget)
    if format == 'json':
        return json.loads(rep.read())
    else:
        return rep.read()

def tvseries(code, profile=None, mediafmt=None, format=None, striptags=None):
    """
    URL : http://api.allocine.fr/rest/v3/tvseries
    Paramètres

        partner : code partenaire (YW5kcm9pZC12M3M pour l'application Android)
        code : identifiant de la saison (entier)
        profile (optionnel) : degré d'informations renvoyées (valeurs possibles : small, medium, large)
        mediafmt (optionnel) : format vidéo
            flv : FLV / H.264
            mp4-lc : MP4 / H.264 Baseline Profile, Low Complexity, with splashscreen
            mp4-hip : H264 High Profile, with splashscreen
            mp4-archive : MP4 / H.264 High Profile, for archive
            mpeg2-theater : MPEG-2 720p
            mpeg2 : MPEG-2 Main Profile
            et sûrement d'autres mais je n'ai pas le code correspondant …
        format (optionnel) : renvoie le résultat au format JSON ou XML (json ou xml)
        striptags (optionnel) : supprime les tags HTML des paramètres valeurs passées en paramètre
    """
    profile= profile or 'large'
    mediafmt= mediafmt or 'mpeg2'
    format= format or 'json'
    striptags= striptags or []

    striptags = ','.join(striptags)

    dataget = urllib.urlencode({ 'code': code,
                             'partner': PARTNER,
                             'format': format,
                             'profile': profile,
                             'mediafmt': mediafmt,
                             'striptags': striptags,
                            })
    rep = urllib2.urlopen('http://api.allocine.fr/rest/v3/tvseries?'+dataget)
    if format == 'json':
        return json.loads(rep.read())
    else:
        return rep.read()

def season(code, profile=None, mediafmt=None, format=None, striptags=None):
    """
    URL : http://api.allocine.fr/rest/v3/season
    Paramètres

        partner : code partenaire (YW5kcm9pZC12M3M pour l'application Android)
        code : identifiant de la saison (entier)
        profile (optionnel) : degré d'informations renvoyées (valeurs possibles : small, medium, large)
        mediafmt (optionnel) : format vidéo
            flv : FLV / H.264
            mp4-lc : MP4 / H.264 Baseline Profile, Low Complexity, with splashscreen
            mp4-hip : H264 High Profile, with splashscreen
            mp4-archive : MP4 / H.264 High Profile, for archive
            mpeg2-theater : MPEG-2 720p
            mpeg2 : MPEG-2 Main Profile
            et sûrement d'autres mais je n'ai pas le code correspondant …
        format (optionnel) : renvoie le résultat au format JSON ou XML (json ou xml)
        striptags (optionnel) : supprime les tags HTML des paramètres valeurs passées en paramètre
    """
    profile= profile or 'large'
    mediafmt= mediafmt or 'mpeg2'
    format= format or 'json'
    striptags= striptags or []

    striptags = ','.join(striptags)

    dataget = urllib.urlencode({ 'code': code,
                             'partner': PARTNER,
                             'format': format,
                             'profile': profile,
                             'mediafmt': mediafmt,
                             'striptags': striptags,
                            })
    rep = urllib2.urlopen('http://api.allocine.fr/rest/v3/season?'+dataget)
    if format == 'json':
        return json.loads(rep.read())
    else:
        return rep.read()

def media(code, profile=None, mediafmt=None, format=None):
    """
    URL : http://api.allocine.fr/rest/v3/media

    * Paramètres
        partner : code partenaire (YW5kcm9pZC12M3M pour l'application Android)
        code : identifiant de la vidéo (entier)
        profile (optionnel) : degré d'informations renvoyées (valeurs possibles : small, medium, large)
        mediafmt (optionnel) : format vidéo
            flv : FLV / H.264
            mp4-lc : MP4 / H.264 Baseline Profile, Low Complexity, with splashscreen
            mp4-hip : H264 High Profile, with splashscreen
            mp4-archive : MP4 / H.264 High Profile, for archive
            mpeg2-theater : MPEG-2 720p
            mpeg2 : MPEG-2 Main Profile
            et sûrement d'autres mais je n'ai pas le code correspondant …
        format (optionnel) : renvoie le résultat au format JSON ou XML (json ou xml)
    """
    profile= profile or 'large'
    mediafmt= mediafmt or 'mpeg2'
    format= format or 'json'
    dataget = urllib.urlencode({ 'code': code,
                     'partner': PARTNER,
                     'format': format,
                     'profile': profile,
                     'mediafmt': mediafmt,
                    })

    rep = urllib2.urlopen('http://api.allocine.fr/rest/v3/media?'+dataget)
    if format == 'json':
        return json.loads(rep.read())
    else:
        return rep.read()

def tvseriesList(count=None, page=None, profile=None, filter=None, order=None, format=None):
    """
    URL : http://api.allocine.fr/rest/v3/tvseriesList

    * Paramètres
        partner : code partenaire (YW5kcm9pZC12M3M pour l'application Android)
        count (optionnel) : nombre de séries à renvoyer (entier)
        page (optionnel) : numéro de la page de résultats à afficher (10 résultats par page par défaut)
        profile (optionnel) : degré d'informations renvoyées (valeurs possibles : small, medium, large)
        filter (optionnel) : filtrer selon un type de résultat (énumeration de termes séparés par des virgules)
            commingsoon
            top
        order (optionnel) : ordre de tri des résultats
            toprank : classement par popularité
        format (optionnel) : renvoie le résultat au format JSON ou XML (json ou xml)
    """
    data = {'partner':PARTNER}
    if count is not None:
        data['count'] = count
    if page is not None:
        data['page'] = page
    if profile is not None and profile in ('small','medium','large'):
        data['profile'] = profile
    if filter is not None and filter in ('commingsoon', 'top'):
        data['filter'] = filter
    else:
        data['filter'] = 'top'
    if order is not None and order == 'toprank':
        data['order'] = order
    if format is not None and format in ('json','xml'):
        data['format'] = format
    else:
        data['format'] = 'json'

    dataget = urllib.urlencode(data)

    rep = urllib2.urlopen('http://api.allocine.fr/rest/v3/tvseriesList?'+dataget)
    if data['format'] == 'json':
        return json.loads(rep.read())
    else:
        return rep.read()
