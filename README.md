# cf-ugliest-route-service
Showing what you shouldn't do


http://docs.cloudfoundry.org/services/api.html#catalog-mgmt

fguichard@home:~$ cf push -f manifest.yml

fguichard@home:~$ cf create-user-provided-service myrouterservice -r https://routeservice-proxy.cfy-app.dev.paascfy.s0.p.fti.net

fguichard@home:~$ cf bind-route-service cfy-app.dev.paascfy.s0.p.fti.net myrouterservice --hostname mySuperApp


Le repertoire vendor contient le module flask et le dependance enfin de permettre
d'etre installe sur un runner/cell offline :

pip install --download vendor -r requirements.txt avant de faire le cf push.
