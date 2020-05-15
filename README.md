# LSZGMovements
Website Scraper for LSZG Airport (Sion) arrivals/departures Table.
Serves the arrivals/departures Table as a JSON API (files).

---

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![volkswagen status](https://auchenberg.github.io/volkswagen/volkswargen_ci.svg?v=1)](https://github.com/auchenberg/volkswagen)

This script downloads the html table from the LSZG website: [sionaeroport.ch](https://www.sionaeroport.ch/en/flights/) and parses it into a `timetable.json` file.


### Usage

Use the `-o` parameter to specify the output directory.

```bash
python3 get-lszg.py -o sion/
```

### Example Output

```json
{
  "data": [
    {
      "aircraft": "OYCKK",
      "callsign": "MMD6616",
      "type": "F2TH",
      "lastinfo": "CANCEL",
      "destination": "Paris-Le-Bourget  (France)CANCEL",
      "time": "13:00",
      "stats": "departure"
    }
  ]
}
```

---

LICENSE

Apache License 2.0

(c) 2020 Simon Burkhardt

