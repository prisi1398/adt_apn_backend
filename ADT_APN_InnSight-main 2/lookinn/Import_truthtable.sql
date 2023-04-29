use Final_ADT;
drop table locality_tt 

create table locality_tt (
listing_id int not null,
name varchar(100),
host_id text,
host_is_superhost text,
host_identity_verified text,
neighbourhood text,
city text,
latitude text,
longitude text,
property_type text,
room_type text,
accommodates int,
bedrooms int,
amenities text,
price int,
review_scores_rating int,
review_scores_value int,
instant_bookable text
)

LOAD DATA LOCAL INFILE 'C:\\Users\\archa\\OneDrive\\Documents\\ADT\\Airbnb\\Airbnb Data\\Listings_Cleaned_Iti1.csv' INTO TABLE `final_adt`.`locality_tt` 
FIELDS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES
