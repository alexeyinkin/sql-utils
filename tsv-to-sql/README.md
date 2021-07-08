# tsv-to-sql

Converts TSV to MySQL's INSERT ... ON DUPLICATE KEY UPDATE.

Usage:
```bash
python3 tsv-to-sql.py [-h] --tsv=FILE --table=TABLE --columns=COLUMNS --pk_columns=COLUMNS [--nullable_columns=COLUMNS]
```

Arguments:
-  `--tsv FILE`            Path to a TSV file.
-  `--table TABLE`         Table name.
-  `--columns COLUMNS`     Comma-separated column names.
-  `--pk_columns COLUMNS`  Comma-separated column names making up the primary key.
-  `--nullable_columns COLUMNS`
                        Comma-separated column names for which empty string should insert NULL.

Examples:
```bash
python3 tsv-to-sql.py \
    --tsv=../../geonames-utils/cities500.txt \
    --table=City \
    --column=0,id,pk,int \
    --column=1,name \
    --column=4,latitude \
    --column=5,longitude \
    --column=8,countryCode \
    --column=14,population \
    --column=17,timezone \
    --column=18,dateTime_update \
    > cities500.sql
```

```bash
python3 tsv-to-sql.py \
    --tsv=../../geonames-utils/extract-city-altnames/altnames.tsv \
    --table=CityName \
    --column=0,id,pk,int \
    --column=0,syncName \
    --column=1,id_nameCity \
    --column=2,lang \
    --column=3,name \
    --column=4,countryCode \
    --column=5,population \
    > altnames.sql
```
