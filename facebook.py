import urllib, urllib2, cookielib, re, os, sys

class Acc:
    jar = cookielib.CookieJar()
    cookie = urllib2.HTTPCookieProcessor(jar)       
    opener = urllib2.build_opener(cookie)

    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14",
        "Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
        "Accept-Language" : "en-us,en;q=0.5",
        "Accept-Charset" : "ISO-8859-1",
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "m.facebook.com"
    }

    def login(self):
        try:
            params = urllib.urlencode({'email':'walid_achach@yahoo.fr','pass':'75869200','login':'Log+In'})
            req = urllib2.Request('http://m.facebook.com/login.php?m=m&refsrc=m.facebook.com%2F', params, self.headers)
            res = self.opener.open(req)
            html = res.read()
      #print html
      print "XXXXXXXXXXXYX"
      res.close()
      #match=re.compile('"pronoun-link participant" href="/(.+?)>(.+?)</a>(.+?)<a(.+?)>(.+?)</a>(.+?)img src="(.+?)"').findall(html)
      match=re.compile('"actor">(.+?)<').findall(html)
          
      #match2=html.replace("\n","ss")
      #match2=html.replace('"actor">',"\n")
      #match2=html.split('>')
      
      #for i in range(60):
      #	if match2[i]:
  	#   print match2[i]
  	
      #print match2[0]
      
      
      #print match[0]
  
    
      
            #print res.getheader('location').split('/')[3]

        except urllib2.HTTPError, e:
            print e.msg
        except urllib2.URLError, e:
            print e.reason[1]
        return False

    def fetch(self,url):
        req = urllib2.Request(url,None,self.headers)
        res = self.opener.open(req)
        return res.read()

bla = Acc()
bla.login()
