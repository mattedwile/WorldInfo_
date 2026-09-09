from flask import Flask, request, render_template_string, jsonify, redirect
import sqlite3, requests, random, time
from datetime import datetime
from zoneinfo import ZoneInfo
app = Flask(__name__)
DB = "worldinfo.db"
CURRENCIES = [
("USD","US Dollar","$"),("INR","Indian Rupee","₹"),("EUR","Euro","€"),("GBP","British Pound","£"),("JPY","Japanese Yen","¥"),("CNY","Chinese Yuan","¥"),("AED","UAE Dirham","د.إ"),("AUD","Australian Dollar","A$"),("CAD","Canadian Dollar","C$"),("CHF","Swiss Franc","CHF"),("SGD","Singapore Dollar","S$"),("KRW","South Korean Won","₩"),("THB","Thai Baht","฿"),("MYR","Malaysian Ringgit","RM"),("NZD","New Zealand Dollar","NZ$"),("ZAR","South African Rand","R"),("SAR","Saudi Riyal","﷼"),("BRL","Brazilian Real","R$"),("RUB","Russian Ruble","₽"),("MXN","Mexican Peso","$")
]
COUNTRIES = [
("Afghanistan","Kabul",43800000,652230,"Asia","Southern Asia","Afghani","AFN","Asia/Kabul","+93","AF","🇦🇫"),
("Albania","Tirana",2800000,28748,"Europe","Southern Europe","Lek","ALL","Europe/Tirane","+355","AL","🇦🇱"),
("Algeria","Algiers",47000000,2381741,"Africa","Northern Africa","Algerian Dinar","DZD","Africa/Algiers","+213","DZ","🇩🇿"),
("Argentina","Buenos Aires",46000000,2780400,"South America","South America","Argentine Peso","ARS","America/Argentina/Buenos_Aires","+54","AR","🇦🇷"),
("Armenia","Yerevan",3000000,29743,"Asia","Western Asia","Dram","AMD","Asia/Yerevan","+374","AM","🇦🇲"),
("Australia","Canberra",27000000,7692024,"Oceania","Australia and New Zealand","Australian Dollar","AUD","Australia/Sydney","+61","AU","🇦🇺"),
("Austria","Vienna",9200000,83871,"Europe","Western Europe","Euro","EUR","Europe/Vienna","+43","AT","🇦🇹"),
("Azerbaijan","Baku",10400000,86600,"Asia","Western Asia","Manat","AZN","Asia/Baku","+994","AZ","🇦🇿"),
("Bahamas","Nassau",400000,13943,"North America","Caribbean","Bahamian Dollar","BSD","America/Nassau","+1","BS","🇧🇸"),
("Bahrain","Manama",1600000,765,"Asia","Western Asia","Bahraini Dinar","BHD","Asia/Bahrain","+973","BH","🇧🇭"),
("Bangladesh","Dhaka",174000000,147570,"Asia","Southern Asia","Taka","BDT","Asia/Dhaka","+880","BD","🇧🇩"),
("Belarus","Minsk",9100000,207600,"Europe","Eastern Europe","Belarusian Ruble","BYN","Europe/Minsk","+375","BY","🇧🇾"),
("Belgium","Brussels",11800000,30528,"Europe","Western Europe","Euro","EUR","Europe/Brussels","+32","BE","🇧🇪"),
("Bhutan","Thimphu",800000,38394,"Asia","Southern Asia","Ngultrum","BTN","Asia/Thimphu","+975","BT","🇧🇹"),
("Bolivia","Sucre",12500000,1098581,"South America","South America","Boliviano","BOB","America/La_Paz","+591","BO","🇧🇴"),
("Bosnia and Herzegovina","Sarajevo",3200000,51209,"Europe","Southern Europe","Convertible Mark","BAM","Europe/Sarajevo","+387","BA","🇧🇦"),
("Botswana","Gaborone",2700000,581730,"Africa","Southern Africa","Pula","BWP","Africa/Gaborone","+267","BW","🇧🇼"),
("Brazil","Brasilia",213000000,8515767,"South America","South America","Brazilian Real","BRL","America/Sao_Paulo","+55","BR","🇧🇷"),
("Bulgaria","Sofia",6400000,110879,"Europe","Eastern Europe","Lev","BGN","Europe/Sofia","+359","BG","🇧🇬"),
("Cambodia","Phnom Penh",18000000,181035,"Asia","South-Eastern Asia","Riel","KHR","Asia/Phnom_Penh","+855","KH","🇰🇭"),
("Canada","Ottawa",41000000,9984670,"North America","Northern America","Canadian Dollar","CAD","America/Toronto","+1","CA","🇨🇦"),
("Chile","Santiago",20000000,756102,"South America","South America","Chilean Peso","CLP","America/Santiago","+56","CL","🇨🇱"),
("China","Beijing",1410000000,9596960,"Asia","Eastern Asia","Yuan","CNY","Asia/Shanghai","+86","CN","🇨🇳"),
("Colombia","Bogota",53000000,1141748,"South America","South America","Colombian Peso","COP","America/Bogota","+57","CO","🇨🇴"),
("Costa Rica","San Jose",5300000,51100,"North America","Central America","Costa Rican Colon","CRC","America/Costa_Rica","+506","CR","🇨🇷"),
("Croatia","Zagreb",3800000,56594,"Europe","Southern Europe","Euro","EUR","Europe/Zagreb","+385","HR","🇭🇷"),
("Cuba","Havana",11000000,109884,"North America","Caribbean","Cuban Peso","CUP","America/Havana","+53","CU","🇨🇺"),
("Cyprus","Nicosia",1400000,9251,"Europe","Southern Europe","Euro","EUR","Asia/Nicosia","+357","CY","🇨🇾"),
("Czechia","Prague",10900000,78865,"Europe","Eastern Europe","Czech Koruna","CZK","Europe/Prague","+420","CZ","🇨🇿"),
("Denmark","Copenhagen",6000000,43094,"Europe","Northern Europe","Danish Krone","DKK","Europe/Copenhagen","+45","DK","🇩🇰"),
("Dominican Republic","Santo Domingo",11400000,48671,"North America","Caribbean","Dominican Peso","DOP","America/Santo_Domingo","+1","DO","🇩🇴"),
("Ecuador","Quito",18000000,276841,"South America","South America","US Dollar","USD","America/Guayaquil","+593","EC","🇪🇨"),
("Egypt","Cairo",118000000,1002450,"Africa","Northern Africa","Egyptian Pound","EGP","Africa/Cairo","+20","EG","🇪🇬"),
("Estonia","Tallinn",1400000,45227,"Europe","Northern Europe","Euro","EUR","Europe/Tallinn","+372","EE","🇪🇪"),
("Ethiopia","Addis Ababa",135000000,1104300,"Africa","Eastern Africa","Birr","ETB","Africa/Addis_Ababa","+251","ET","🇪🇹"),
("Fiji","Suva",940000,18272,"Oceania","Melanesia","Fijian Dollar","FJD","Pacific/Fiji","+679","FJ","🇫🇯"),
("Finland","Helsinki",5600000,338455,"Europe","Northern Europe","Euro","EUR","Europe/Helsinki","+358","FI","🇫🇮"),
("France","Paris",69000000,551695,"Europe","Western Europe","Euro","EUR","Europe/Paris","+33","FR","🇫🇷"),
("Georgia","Tbilisi",3700000,69700,"Asia","Western Asia","Lari","GEL","Asia/Tbilisi","+995","GE","🇬🇪"),
("Germany","Berlin",84000000,357022,"Europe","Western Europe","Euro","EUR","Europe/Berlin","+49","DE","🇩🇪"),
("Ghana","Accra",35000000,238533,"Africa","Western Africa","Ghanaian Cedi","GHS","Africa/Accra","+233","GH","🇬🇭"),
("Greece","Athens",10000000,131957,"Europe","Southern Europe","Euro","EUR","Europe/Athens","+30","GR","🇬🇷"),
("Guatemala","Guatemala City",19000000,108889,"North America","Central America","Quetzal","GTQ","America/Guatemala","+502","GT","🇬🇹"),
("Haiti","Port-au-Prince",12000000,27750,"North America","Caribbean","Gourde","HTG","America/Port-au-Prince","+509","HT","🇭🇹"),
("Honduras","Tegucigalpa",11000000,112492,"North America","Central America","Lempira","HNL","America/Tegucigalpa","+504","HN","🇭🇳"),
("Hungary","Budapest",9600000,93028,"Europe","Eastern Europe","Forint","HUF","Europe/Budapest","+36","HU","🇭🇺"),
("Iceland","Reykjavik",400000,103000,"Europe","Northern Europe","Icelandic Krona","ISK","Atlantic/Reykjavik","+354","IS","🇮🇸"),
("India","New Delhi",1460000000,3287263,"Asia","Southern Asia","Indian Rupee","INR","Asia/Kolkata","+91","IN","🇮🇳"),
("Indonesia","Jakarta",285000000,1904569,"Asia","South-Eastern Asia","Rupiah","IDR","Asia/Jakarta","+62","ID","🇮🇩"),
("Iran","Tehran",92000000,1648195,"Asia","Southern Asia","Iranian Rial","IRR","Asia/Tehran","+98","IR","🇮🇷"),
("Iraq","Baghdad",47000000,438317,"Asia","Western Asia","Iraqi Dinar","IQD","Asia/Baghdad","+964","IQ","🇮🇶"),
("Ireland","Dublin",5400000,70273,"Europe","Northern Europe","Euro","EUR","Europe/Dublin","+353","IE","🇮🇪"),
("Israel","Jerusalem",10000000,20770,"Asia","Western Asia","New Shekel","ILS","Asia/Jerusalem","+972","IL","🇮🇱"),
("Italy","Rome",59000000,301340,"Europe","Southern Europe","Euro","EUR","Europe/Rome","+39","IT","🇮🇹"),
("Jamaica","Kingston",2900000,10991,"North America","Caribbean","Jamaican Dollar","JMD","America/Jamaica","+1","JM","🇯🇲"),
("Japan","Tokyo",123000000,377975,"Asia","Eastern Asia","Yen","JPY","Asia/Tokyo","+81","JP","🇯🇵"),
("Jordan","Amman",12000000,89342,"Asia","Western Asia","Jordanian Dinar","JOD","Asia/Amman","+962","JO","🇯🇴"),
("Kazakhstan","Astana",21000000,2724900,"Asia","Central Asia","Tenge","KZT","Asia/Almaty","+7","KZ","🇰🇿"),
("Kenya","Nairobi",57000000,580367,"Africa","Eastern Africa","Kenyan Shilling","KES","Africa/Nairobi","+254","KE","🇰🇪"),
("Kuwait","Kuwait City",5000000,17818,"Asia","Western Asia","Kuwaiti Dinar","KWD","Asia/Kuwait","+965","KW","🇰🇼"),
("Latvia","Riga",1900000,64559,"Europe","Northern Europe","Euro","EUR","Europe/Riga","+371","LV","🇱🇻"),
("Lebanon","Beirut",5800000,10452,"Asia","Western Asia","Lebanese Pound","LBP","Asia/Beirut","+961","LB","🇱🇧"),
("Lithuania","Vilnius",2900000,65300,"Europe","Northern Europe","Euro","EUR","Europe/Vilnius","+370","LT","🇱🇹"),
("Luxembourg","Luxembourg",680000,2586,"Europe","Western Europe","Euro","EUR","Europe/Luxembourg","+352","LU","🇱🇺"),
("Malaysia","Kuala Lumpur",36000000,330803,"Asia","South-Eastern Asia","Ringgit","MYR","Asia/Kuala_Lumpur","+60","MY","🇲🇾"),
("Maldives","Male",530000,298,"Asia","Southern Asia","Rufiyaa","MVR","Indian/Maldives","+960","MV","🇲🇻"),
("Malta","Valletta",570000,316,"Europe","Southern Europe","Euro","EUR","Europe/Malta","+356","MT","🇲🇹"),
("Mexico","Mexico City",132000000,1964375,"North America","Central America","Mexican Peso","MXN","America/Mexico_City","+52","MX","🇲🇽"),
("Moldova","Chisinau",2500000,33846,"Europe","Eastern Europe","Moldovan Leu","MDL","Europe/Chisinau","+373","MD","🇲🇩"),
("Mongolia","Ulaanbaatar",3500000,1564110,"Asia","Eastern Asia","Tugrik","MNT","Asia/Ulaanbaatar","+976","MN","🇲🇳"),
("Montenegro","Podgorica",620000,13812,"Europe","Southern Europe","Euro","EUR","Europe/Podgorica","+382","ME","🇲🇪"),
("Morocco","Rabat",39000000,446550,"Africa","Northern Africa","Moroccan Dirham","MAD","Africa/Casablanca","+212","MA","🇲🇦"),
("Nepal","Kathmandu",30000000,147181,"Asia","Southern Asia","Nepalese Rupee","NPR","Asia/Kathmandu","+977","NP","🇳🇵"),
("Netherlands","Amsterdam",18000000,41850,"Europe","Western Europe","Euro","EUR","Europe/Amsterdam","+31","NL","🇳🇱"),
("New Zealand","Wellington",5300000,270467,"Oceania","Australia and New Zealand","New Zealand Dollar","NZD","Pacific/Auckland","+64","NZ","🇳🇿"),
("Nigeria","Abuja",238000000,923768,"Africa","Western Africa","Naira","NGN","Africa/Lagos","+234","NG","🇳🇬"),
("North Korea","Pyongyang",26000000,120538,"Asia","Eastern Asia","North Korean Won","KPW","Asia/Pyongyang","+850","KP","🇰🇵"),
("Norway","Oslo",5600000,385207,"Europe","Northern Europe","Norwegian Krone","NOK","Europe/Oslo","+47","NO","🇳🇴"),
("Oman","Muscat",5600000,309500,"Asia","Western Asia","Omani Rial","OMR","Asia/Muscat","+968","OM","🇴🇲"),
("Pakistan","Islamabad",260000000,881913,"Asia","Southern Asia","Pakistani Rupee","PKR","Asia/Karachi","+92","PK","🇵🇰"),
("Panama","Panama City",4500000,75417,"North America","Central America","Balboa","PAB","America/Panama","+507","PA","🇵🇦"),
("Papua New Guinea","Port Moresby",11000000,462840,"Oceania","Melanesia","Kina","PGK","Pacific/Port_Moresby","+675","PG","🇵🇬"),
("Paraguay","Asuncion",6800000,406752,"South America","South America","Guarani","PYG","America/Asuncion","+595","PY","🇵🇾"),
("Peru","Lima",34000000,1285216,"South America","South America","Sol","PEN","America/Lima","+51","PE","🇵🇪"),
("Philippines","Manila",117000000,300000,"Asia","South-Eastern Asia","Philippine Peso","PHP","Asia/Manila","+63","PH","🇵🇭"),
("Poland","Warsaw",38000000,312696,"Europe","Eastern Europe","Zloty","PLN","Europe/Warsaw","+48","PL","🇵🇱"),
("Portugal","Lisbon",10500000,92090,"Europe","Southern Europe","Euro","EUR","Europe/Lisbon","+351","PT","🇵🇹"),
("Qatar","Doha",3100000,11586,"Asia","Western Asia","Qatari Riyal","QAR","Asia/Qatar","+974","QA","🇶🇦"),
("Romania","Bucharest",19000000,238397,"Europe","Eastern Europe","Romanian Leu","RON","Europe/Bucharest","+40","RO","🇷🇴"),
("Russia","Moscow",144000000,17098242,"Europe/Asia","Eastern Europe","Russian Ruble","RUB","Europe/Moscow","+7","RU","🇷🇺"),
("Rwanda","Kigali",14000000,26338,"Africa","Eastern Africa","Rwandan Franc","RWF","Africa/Kigali","+250","RW","🇷🇼"),
("Saudi Arabia","Riyadh",35000000,2149690,"Asia","Western Asia","Saudi Riyal","SAR","Asia/Riyadh","+966","SA","🇸🇦"),
("Senegal","Dakar",19000000,196722,"Africa","Western Africa","West African CFA Franc","XOF","Africa/Dakar","+221","SN","🇸🇳"),
("Serbia","Belgrade",6500000,77474,"Europe","Southern Europe","Serbian Dinar","RSD","Europe/Belgrade","+381","RS","🇷🇸"),
("Singapore","Singapore",6100000,728,"Asia","South-Eastern Asia","Singapore Dollar","SGD","Asia/Singapore","+65","SG","🇸🇬"),
("Slovakia","Bratislava",5400000,49035,"Europe","Eastern Europe","Euro","EUR","Europe/Bratislava","+421","SK","🇸🇰"),
("Slovenia","Ljubljana",2100000,20273,"Europe","Southern Europe","Euro","EUR","Europe/Ljubljana","+386","SI","🇸🇮"),
("South Africa","Pretoria",65000000,1221037,"Africa","Southern Africa","Rand","ZAR","Africa/Johannesburg","+27","ZA","🇿🇦"),
("South Korea","Seoul",52000000,100210,"Asia","Eastern Asia","Won","KRW","Asia/Seoul","+82","KR","🇰🇷"),
("Spain","Madrid",49000000,505370,"Europe","Southern Europe","Euro","EUR","Europe/Madrid","+34","ES","🇪🇸"),
("Sri Lanka","Sri Jayawardenepura Kotte",22000000,65610,"Asia","Southern Asia","Sri Lankan Rupee","LKR","Asia/Colombo","+94","LK","🇱🇰"),
("Sudan","Khartoum",52000000,1861484,"Africa","Northern Africa","Sudanese Pound","SDG","Africa/Khartoum","+249","SD","🇸🇩"),
("Sweden","Stockholm",11000000,450295,"Europe","Northern Europe","Swedish Krona","SEK","Europe/Stockholm","+46","SE","🇸🇪"),
("Switzerland","Bern",9000000,41285,"Europe","Western Europe","Swiss Franc","CHF","Europe/Zurich","+41","CH","🇨🇭"),
("Taiwan","Taipei",23000000,36197,"Asia","Eastern Asia","New Taiwan Dollar","TWD","Asia/Taipei","+886","TW","🇹🇼"),
("Tanzania","Dodoma",71000000,945087,"Africa","Eastern Africa","Tanzanian Shilling","TZS","Africa/Dar_es_Salaam","+255","TZ","🇹🇿"),
("Thailand","Bangkok",72000000,513120,"Asia","South-Eastern Asia","Baht","THB","Asia/Bangkok","+66","TH","🇹🇭"),
("Tunisia","Tunis",12000000,163610,"Africa","Northern Africa","Tunisian Dinar","TND","Africa/Tunis","+216","TN","🇹🇳"),
("Turkey","Ankara",88000000,783562,"Asia/Europe","Western Asia","Turkish Lira","TRY","Europe/Istanbul","+90","TR","🇹🇷"),
("Uganda","Kampala",52000000,241038,"Africa","Eastern Africa","Ugandan Shilling","UGX","Africa/Kampala","+256","UG","🇺🇬"),
("Ukraine","Kyiv",39000000,603500,"Europe","Eastern Europe","Hryvnia","UAH","Europe/Kyiv","+380","UA","🇺🇦"),
("United Arab Emirates","Abu Dhabi",11000000,83600,"Asia","Western Asia","UAE Dirham","AED","Asia/Dubai","+971","AE","🇦🇪"),
("United Kingdom","London",70000000,243610,"Europe","Northern Europe","British Pound","GBP","Europe/London","+44","GB","🇬🇧"),
("United States","Washington, D.C.",347000000,9833517,"North America","Northern America","US Dollar","USD","America/New_York","+1","US","🇺🇸"),
("Uruguay","Montevideo",3500000,176215,"South America","South America","Uruguayan Peso","UYU","America/Montevideo","+598","UY","🇺🇾"),
("Uzbekistan","Tashkent",37000000,447400,"Asia","Central Asia","Som","UZS","Asia/Tashkent","+998","UZ","🇺🇿"),
("Venezuela","Caracas",29000000,916445,"South America","South America","Bolivar","VES","America/Caracas","+58","VE","🇻🇪"),
("Vietnam","Hanoi",102000000,331212,"Asia","South-Eastern Asia","Dong","VND","Asia/Ho_Chi_Minh","+84","VN","🇻🇳"),
("Zambia","Lusaka",22000000,752618,"Africa","Eastern Africa","Zambian Kwacha","ZMW","Africa/Lusaka","+260","ZM","🇿🇲"),
("Zimbabwe","Harare",17000000,390757,"Africa","Eastern Africa","Zimbabwean Dollar","ZWL","Africa/Harare","+263","ZW","🇿🇼")
]
CSS=""" :root{--bg:#eef3ff;--card:#ffffff;--text:#20242a;--muted:#69727d;--head:#172033;--accent:#4355df;--accent2:#11bf96;--border:#dfe4ec;--soft:#f5f7fa}body.dark{--bg:#0d1320;--card:#171e2c;--text:#edf1f7;--muted:#9da8ba;--head:#090d16;--accent:#7e8cff;--accent2:#35d9b0;--border:#2a3447;--soft:#202838}*{box-sizing:border-box}body{margin:0;font-family:Poppins,Arial,sans-serif;background:linear-gradient(135deg,var(--bg),#e8fff8);color:var(--text);transition:.2s}body.dark{background:linear-gradient(135deg,#0d1320,#0b1c18)}header{background:var(--head);color:white;padding:18px 6%;display:flex;justify-content:space-between;align-items:center;box-shadow:0 4px 20px #0003}.logo{font-size:25px;font-weight:700}nav a{color:#ccd4e5;text-decoration:none;margin-left:18px;font-size:14px}nav a:hover{color:white}.toggle{background:#ffffff20;border:1px solid #ffffff25;color:white;padding:9px 13px;border-radius:20px;cursor:pointer}.container{max-width:1100px;margin:30px auto;padding:0 18px}.card{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:23px;margin-bottom:20px;box-shadow:0 8px 25px #17203315}.search{display:flex;gap:10px;margin-bottom:20px}input,select,button{padding:12px 14px;border:1px solid var(--border);border-radius:9px;font:inherit;background:var(--card);color:var(--text)}input,select{width:100%}button{background:linear-gradient(135deg,var(--accent),var(--accent2));color:white;border:0;cursor:pointer;font-weight:600}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin-top:20px}.item{background:var(--soft);padding:14px;border-radius:10px}.item b{display:block;color:var(--muted);font-size:11px;text-transform:uppercase;margin-bottom:5px}.item span{font-size:16px;font-weight:500}.head{display:flex;align-items:center;gap:20px;padding-bottom:18px;border-bottom:1px solid var(--border)}.flag{width:130px;height:85px;object-fit:cover;border-radius:7px}.emoji{font-size:35px}h1{margin:0 0 5px}h2{margin-top:0}.dim{color:var(--muted)}.convert{display:grid;grid-template-columns:1fr 1fr 1fr 120px;gap:10px;align-items:end}.result{margin-top:15px;padding:16px;border-radius:10px;background:linear-gradient(135deg,#11bf9625,#4355df25);font-size:20px;font-weight:700}.compare{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:15px}table{width:100%;border-collapse:collapse}th,td{padding:11px;border-bottom:1px solid var(--border);text-align:left}th{background:var(--soft)}.error{background:#ff525215;color:#c0392b;padding:14px;border-radius:10px}.actions{display:flex;gap:10px;flex-wrap:wrap}a{color:var(--accent)}@media(max-width:700px){header{padding:15px 4%;display:block}nav{margin-top:10px}nav a{margin-left:0;margin-right:12px}.search,.convert{display:grid;grid-template-columns:1fr}.head{align-items:flex-start}.flag{width:95px;height:65px}} """
HEAD=f"""<meta name="viewport" content="width=device-width,initial-scale=1"><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet"><style>{CSS}</style>"""
HOME=HEAD+"""<title>WorldInfo</title><header><div class="logo">🌍 WorldInfo</div><nav><a href="/">Home</a><a href="/countries">Browse All</a><button class="toggle" onclick="theme()">🌓 Theme</button></nav></header><div class="container"><form class="search"><input list="countries" name="country" placeholder="Search any country..." value="{{country}}"><datalist id="countries">{% for n in names %}<option value="{{n}}">{% endfor %}</datalist><button>Search</button></form>{% if error %}<div class="card error">{{error}}</div>{% endif %}{% if d %}<div class="card"><div class="head"><img class="flag" src="{{d.flag}}"><div><div class="emoji">{{d.emoji}}</div><h1>{{d.name}}</h1><span class="dim">{{d.capital}} · {{d.region}}</span></div></div><div class="grid">{% for k,v in [("Population",d.population),("Area",d.area+" km²"),("Population Density",d.density+" / km²"),("Continent",d.continent),("Region",d.region),("Capital",d.capital),("Currency",d.currency),("Currency Code",d.currency_code),("Languages",d.languages),("Calling Code",d.calling),("Internet Domain",d.domain),("Time Zone",d.timezone),("Local Time",d.localtime),("Driving Side",d.driving),("Country Code",d.code),("UN Member",d.unmember),("Independence","Yes")] %}<div class="item"><b>{{k}}</b><span>{{v}}</span></div>{% endfor %}</div><a href="https://www.google.com/maps/search/?api=1&query={{d.capital}}+{{d.name}}" target="_blank">📍 View on Google Maps</a></div>{% if weather %}<div class="card"><h2>🌦 Weather Right Now</h2><div class="grid"><div class="item"><b>Temperature</b><span>{{weather.t}} °C</span></div><div class="item"><b>Wind</b><span>{{weather.w}} km/h</span></div><div class="item"><b>Condition</b><span>{{weather.c}}</span></div></div></div>{% endif %}{% endif %}<div class="card"><h2>💱 Currency Converter</h2><form id="convert" class="convert"><div><small class="dim">From</small><select id="from">{% for c in currencies %}<option value="{{c[0]}}">{{c[0]}} - {{c[1]}}</option>{% endfor %}</select></div><div><small class="dim">Amount</small><input id="amount" type="number" value="100" min="0"></div><div><small class="dim">To</small><select id="to">{% for c in currencies %}<option value="{{c[0]}}" {% if c[0]=="INR" %}selected{% endif %}>{{c[0]}} - {{c[1]}}</option>{% endfor %}</select></div><button>Convert</button></form><div id="result" class="result" style="display:none"></div></div><div class="card"><h2>⚖ Country Comparison</h2><form action="/compare"><div class="grid"><div><small class="dim">Country 1</small><select name="c">{% for n in names %}<option value="{{n}}">{{n}}</option>{% endfor %}</select></div><div><small class="dim">Country 2</small><select name="c">{% for n in names %}<option value="{{n}}" {% if n=="India" %}selected{% endif %}>{{n}}</option>{% endfor %}</select></div></div><br><button style="width:100%">Compare Countries</button></form></div><div class="card"><div class="actions"><a href="/random"><button type="button">🎲 Random Country</button></a><a href="/countries"><button type="button">📋 Browse All</button></a></div></div>{% if history %}<div class="card"><h2>Recent Searches</h2>{% for h in history %}<div style="padding:7px 0;border-bottom:1px solid var(--border)"><a href="/?country={{h[0]}}">{{h[0]}}</a><span class="dim"> — {{h[1]}}</span></div>{% endfor %}</div>{% endif %}</div><script>function theme(){document.body.classList.toggle("dark");localStorage.setItem("world-theme",document.body.classList.contains("dark")?"dark":"light")}if(localStorage.getItem("world-theme")==="dark")document.body.classList.add("dark");document.getElementById("convert").onsubmit=async function(e){e.preventDefault();let f=document.getElementById("from").value,t=document.getElementById("to").value,a=document.getElementById("amount").value,out=document.getElementById("result");out.style.display="block";out.innerText="Converting...";try{let r=await fetch(`/convert?from=${f}&to=${t}&amount=${a}`),d=await r.json();out.innerText=d.error?d.error:`${a} ${f} = ${Number(d.result).toFixed(2)} ${t}`}catch{out.innerText="Conversion unavailable right now."}};</script>"""
COMPARE=HEAD+"""<title>Country Comparison</title><header><div class="logo">🌍 WorldInfo</div><nav><a href="/">Home</a><a href="/countries">Browse All</a><button class="toggle" onclick="theme()">🌓 Theme</button></nav></header><div class="container"><h1>⚖ Country Comparison</h1>{% if error %}<div class="card error">{{error}}</div>{% else %}<div class="compare">{% for d in countries %}<div class="card"><div style="text-align:center"><img class="flag" src="{{d.flag}}"><div style="font-size:32px">{{d.emoji}}</div><h2>{{d.name}}</h2></div><table><tr><th>Capital</th><td>{{d.capital}}</td></tr><tr><th>Population</th><td>{{d.population}}</td></tr><tr><th>Area</th><td>{{d.area}} km²</td></tr><tr><th>Density</th><td>{{d.density}} / km²</td></tr><tr><th>Continent</th><td>{{d.continent}}</td></tr><tr><th>Region</th><td>{{d.region}}</td></tr><tr><th>Currency</th><td>{{d.currency}}</td></tr><tr><th>Languages</th><td>{{d.languages}}</td></tr><tr><th>Timezone</th><td>{{d.timezone}}</td></tr><tr><th>Calling Code</th><td>{{d.calling}}</td></tr><tr><th>Driving</th><td>{{d.driving}}</td></tr><tr><th>Country Code</th><td>{{d.code}}</td></tr></table></div>{% endfor %}</div>{% endif %}<br><a href="/">← Back to WorldInfo</a></div><script>function theme(){document.body.classList.toggle("dark");localStorage.setItem("world-theme",document.body.classList.contains("dark")?"dark":"light")}if(localStorage.getItem("world-theme")==="dark")document.body.classList.add("dark");</script>"""
BROWSE=HEAD+"""<title>Browse Countries</title><header><div class="logo">🌍 WorldInfo</div><nav><a href="/">Home</a><a href="/countries">Browse All</a><button class="toggle" onclick="theme()">🌓 Theme</button></nav></header><div class="container"><h1>🌍 Browse All Countries</h1><div class="card"><input id="search" placeholder="Search country..." onkeyup="filter()"><br><br><table id="table"><tr><th>Country</th><th>Capital</th><th>Continent</th><th>Population</th><th>Currency</th></tr>{% for r in rows %}<tr><td><a href="/?country={{r[0]}}">{{r[0]}}</a></td><td>{{r[1]}}</td><td>{{r[4]}}</td><td>{{"{:,}".format(r[2])}}</td><td>{{r[5]}}</td></tr>{% endfor %}</table></div><a href="/">← Back to WorldInfo</a></div><script>function theme(){document.body.classList.toggle("dark");localStorage.setItem("world-theme",document.body.classList.contains("dark")?"dark":"light")}if(localStorage.getItem("world-theme")==="dark")document.body.classList.add("dark");function filter(){let q=document.getElementById("search").value.toLowerCase();document.querySelectorAll("#table tr").forEach((r,i)=>{if(i===0)return;let name=r.children[0].innerText.toLowerCase();r.style.display=name.includes(q)?"":"none"})}</script>"""
def connect(): return sqlite3.connect(DB)
def init_db():
    c=connect()
    try:
        c.execute("PRAGMA journal_mode=WAL"); c.execute("PRAGMA foreign_keys = ON")
        c.execute("CREATE TABLE IF NOT EXISTS countries(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT UNIQUE,capital TEXT,population INTEGER,area REAL,continent TEXT,region TEXT,currency TEXT,currency_code TEXT,timezone TEXT,calling TEXT,code TEXT,emoji TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS currencies(code TEXT PRIMARY KEY,name TEXT,symbol TEXT)")
        c.execute("CREATE TABLE IF NOT EXISTS searches(country TEXT,time TEXT)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_countries_name ON countries(name)")
        c.execute("CREATE INDEX IF NOT EXISTS idx_searches_country ON searches(country)")
        c.executemany("INSERT OR IGNORE INTO currencies VALUES(?,?,?)",CURRENCIES)
        if c.execute("SELECT COUNT(*) FROM countries").fetchone()[0]==0:c.executemany("INSERT OR IGNORE INTO countries(name,capital,population,area,continent,region,currency,currency_code,timezone,calling,code,emoji) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",COUNTRIES)
        c.commit()
    finally:c.close()
def get_country(name):
    c=connect(); r=c.execute("SELECT * FROM countries WHERE lower(name)=lower(?)",(name,)).fetchone()
    if not r:r=c.execute("SELECT * FROM countries WHERE lower(name) LIKE lower(?) LIMIT 1",("%"+name+"%",)).fetchone()
    c.close()
    if not r:return None
    d=dict(zip(["id","name","capital","population","area","continent","region","currency","currency_code","timezone","calling","code","emoji"],r))
    d["flag"]=f"https://flagcdn.com/w320/{d['code'].lower()}.png"; d["domain"]="."+d["code"].lower(); d["languages"]=get_languages(d["name"]); pop,area=d["population"],d["area"]; d["density"]=f"{pop/area:,.1f}" if area else "N/A"; d["population"]=f"{pop:,}"; d["area"]=f"{area:,.0f}"
    try:d["localtime"]=datetime.now(ZoneInfo(d["timezone"])).strftime("%d %b %Y, %I:%M %p")
    except:d["localtime"]="Unavailable"
    d["driving"]=get_driving(d["name"]); d["unmember"]="Yes"; return d
def get_languages(country):
    languages={"India":"Hindi, English and other regional languages","United States":"English","United Kingdom":"English","Canada":"English, French","Australia":"English","Germany":"German","France":"French","Spain":"Spanish","Italy":"Italian","Japan":"Japanese","China":"Chinese","South Korea":"Korean","Russia":"Russian","Brazil":"Portuguese","Mexico":"Spanish","Portugal":"Portuguese","Netherlands":"Dutch","Switzerland":"German, French, Italian, Romansh","Belgium":"Dutch, French, German","Austria":"German","Pakistan":"Urdu, English","Bangladesh":"Bengali","Nepal":"Nepali","Sri Lanka":"Sinhala, Tamil","Thailand":"Thai","Vietnam":"Vietnamese","Indonesia":"Indonesian","Malaysia":"Malay","Singapore":"English, Malay, Mandarin, Tamil","Philippines":"Filipino, English","Saudi Arabia":"Arabic","United Arab Emirates":"Arabic, English","Egypt":"Arabic","Turkey":"Turkish","Israel":"Hebrew, Arabic","South Africa":"Multiple official languages"}
    return languages.get(country,"Local national languages")
def get_driving(country):
    return "Left" if country in {"India","United Kingdom","Australia","New Zealand","Japan","Pakistan","Bangladesh","Nepal","Sri Lanka","Thailand","Malaysia","Indonesia","Singapore","South Africa","Kenya","Tanzania","Uganda"} else "Right"
def all_names():
    c=connect(); rows=c.execute("SELECT name FROM countries ORDER BY name").fetchall(); c.close(); return [x[0] for x in rows]
def weather(country):
    coords={"India":(28.61,77.21),"United States":(38.90,-77.03),"United Kingdom":(51.50,-0.12),"Japan":(35.68,139.69),"China":(39.90,116.40),"Germany":(52.52,13.40),"France":(48.85,2.35),"Australia":(-33.86,151.20),"Canada":(45.42,-75.69),"Brazil":(-15.79,-47.88),"Singapore":(1.35,103.82),"UAE":(24.45,54.37),"United Arab Emirates":(24.45,54.37),"Russia":(55.75,37.61),"South Korea":(37.56,126.97),"Italy":(41.90,12.49),"Spain":(40.41,-3.70),"Mexico":(19.43,-99.13),"Pakistan":(33.69,73.03),"Nepal":(27.71,85.32)}
    if country not in coords:return None
    lat,lon=coords[country]
    try:
        data=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,weather_code",timeout=8).json()["current"]
        codes={0:"Clear",1:"Mainly clear",2:"Partly cloudy",3:"Overcast",45:"Fog",51:"Drizzle",53:"Drizzle",61:"Rain",63:"Rain",65:"Heavy rain",71:"Snow",73:"Snow",75:"Heavy snow",80:"Showers",81:"Showers",82:"Heavy showers",95:"Thunderstorm",96:"Thunderstorm",99:"Thunderstorm"}
        return {"t":data["temperature_2m"],"w":data["wind_speed_10m"],"c":codes.get(data["weather_code"],"Unknown")}
    except:return None
def save_search(name):
    c=connect(); c.execute("INSERT INTO searches VALUES(?,?)",(name,datetime.now().strftime("%d %b %Y, %I:%M %p"))); c.commit(); c.close()
def history():
    c=connect(); r=c.execute("SELECT country,time FROM searches ORDER BY rowid DESC LIMIT 8").fetchall(); c.close(); return r
RATE_CACHE={}; CACHE_TIME=1800
def get_rates(base):
    now=time.time()
    if base in RATE_CACHE and now-RATE_CACHE[base][0]<CACHE_TIME:return RATE_CACHE[base][1]
    try:
        data=requests.get(f"https://open.er-api.com/v6/latest/{base}",timeout=10).json()
        if data.get("result")=="success":RATE_CACHE[base]=(now,data["rates"]); return data["rates"]
    except:pass
    try:
        data=requests.get(f"https://api.frankfurter.app/latest?from={base}",timeout=10).json(); rates=data.get("rates")
        if rates:rates[base]=1; RATE_CACHE[base]=(now,rates); return rates
    except:pass
    return RATE_CACHE.get(base,(None,None))[1] if base in RATE_CACHE else None
@app.route("/api/country/<name>")
def api_country(name):
    d=get_country(name); return jsonify({"success":False,"error":"Country not found"}),404 if not d else jsonify({"success":True,"source":"SQLite database: worldinfo.db","data":d})
@app.route("/api/countries")
def api_countries():
    c=connect(); rows=c.execute("SELECT name,capital,population,area,continent,region,currency,currency_code,timezone,calling,code,emoji FROM countries ORDER BY name").fetchall(); c.close(); return jsonify({"success":True,"source":"SQLite database: worldinfo.db","count":len(rows),"data":[dict(zip(["name","capital","population","area","continent","region","currency","currency_code","timezone","calling","code","emoji"],r)) for r in rows]})
@app.route("/api/convert")
def api_convert():
    result=convert()
    if hasattr(result,"get_json"): data=result.get_json(); data["source"]="open.er-api.com (Frankfurter fallback)"; return jsonify(data)
    return result
@app.route("/api/weather/<name>")
def api_weather(name):
    d=get_country(name)
    if not d:return jsonify({"success":False,"error":"Country not found"}),404
    w=weather(d["name"]); return jsonify({"success":False,"error":"Weather unavailable for this country"}),503 if not w else jsonify({"success":True,"source":"Open-Meteo API","country":d["name"],"weather":w})
@app.route("/api/history")
def api_history(): return jsonify({"success":True,"source":"SQLite database: worldinfo.db","history":[dict(zip(["country","time"],r)) for r in history()]})
@app.route("/api/random")
def api_random_api():
    names=all_names()
    if not names:return jsonify({"success":False,"error":"Database is empty"}),404
    return jsonify({"success":True,"source":"SQLite database: worldinfo.db","data":get_country(random.choice(names))})
@app.route("/")
def home():
    name=request.args.get("country","").strip(); d=None; err=None; w=None
    if name:
        d=get_country(name)
        if d:save_search(d["name"]); w=weather(d["name"])
        else:err="Country not found. Try another country."
    c=connect(); currencies=c.execute("SELECT * FROM currencies ORDER BY code").fetchall(); c.close()
    return render_template_string(HOME,country=name,d=d,error=err,weather=w,currencies=currencies,names=all_names(),history=history())
@app.route("/countries")
def countries_page():
    c=connect(); rows=c.execute("SELECT name,capital,population,area,continent,currency_code FROM countries ORDER BY name").fetchall(); c.close()
    return render_template_string(BROWSE,rows=rows)
@app.route("/compare")
def compare():
    names=[x.strip() for x in request.args.getlist("c") if x.strip()]
    if len(names)<2:return render_template_string(COMPARE,error="Please select two countries.",countries=[])
    countries=[get_country(x) for x in names[:5]]
    if any(x is None for x in countries):return render_template_string(COMPARE,error="One or more countries were not found.",countries=[])
    return render_template_string(COMPARE,error=None,countries=countries)
@app.route("/convert")
def convert():
    try:
        f=request.args.get("from","USD").upper(); t=request.args.get("to","INR").upper(); amount=float(request.args.get("amount","1"))
        if amount<0:return jsonify(error="Amount cannot be negative.")
        if f==t:return jsonify(result=amount)
        rates=get_rates(f)
        if not rates or t not in rates:return jsonify(error="Currency not supported right now.")
        return jsonify(result=amount*rates[t])
    except:return jsonify(error="Conversion failed.")
@app.route("/random")
def random_country():
    names=all_names()
    if not names:return redirect("/")
    return redirect("/?country="+requests.utils.quote(random.choice(names)))
@app.route("/health")
def health():
    c=connect(); count=c.execute("SELECT COUNT(*) FROM countries").fetchone()[0]; c.close()
    return f"WorldInfo is running! Countries in database: {count}"
init_db()
if __name__=="__main__":app.run(host="0.0.0.0",port=5000,debug=True)
