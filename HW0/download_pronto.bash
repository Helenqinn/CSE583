mkdir pronto
cd pronto
echo "These are the pronto data from 2015" > README.txt
mkdir data
curl -o data/open_data_year_one.zip https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip -o data/open_data_year_one.zip -d data
head data/2015_trip_data.csv
