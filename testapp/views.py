# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib
import xml
from urllib import urlopen
from xml.etree import ElementTree
from django.shortcuts import render
import urllib2
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


def urlconsume(url):
    try:
        import pdb
        # pdb.set_trace()
        url = url
        full_url = '{0}'.format(url)
        try:
            req = urllib2.Request(full_url, None, {})
            resp = urllib2.urlopen(req)
            rdata = resp.read()
            return json.loads(rdata)
        except urllib2.URLError as e:
            if hasattr(e, 'reason'):
                print e.reason
            elif hasattr(e, 'code'):
                print e.code
            return e.reason
    except Exception as e:
        print e.message
        return None


def testview(request, template="testview.html"):
    # https://api.alat.ng/Contact.WebApi/api/leaderboard/gettopleadershipboard?counter=10
    alat_url = 'https://api.alat.ng/Contact.WebApi/api/leaderboard/gettopleadershipboard?counter=10'
    url = urlconsume(alat_url)
    # url = webbrowser.open(alat_url)
    print url
    context = {'url': url}
    return render(request, context, template)


class LeaderBoard(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        alat_url = 'https://api.alat.ng/Contact.WebApi/api/leaderboard/gettopleadershipboard?counter=10'
        url = urlconsume(alat_url)
        return Response(url, status=200)
