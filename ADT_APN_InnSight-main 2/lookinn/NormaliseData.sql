create table listings( id int not null, name char(100) not null) /* Archana Narayanan */
create table location (listing_id int not null, longitude text, latitude text, city text, neighbourhood text)  /* Preethi Sivakumar */
create table reviews (listing_id int not null, scores_rating int, scores_value int) /* Nidhi Galgali */
create table property_details (listing_id int not null, property_type text, room_type text, accomodate_count int, bedrooms int, price int, instant_bookable text)  /* Archana Narayanan */
create table amenities (listing_id int not null, amenities text)  /* Archana Narayanan */

 /* Archana Narayanan */
insert into listings (id, name)
select listing_id, name from locality_tt

/* Preethi Sivakumar */
insert into location (listing_id, longitude, latitude, city, neighbourhood)
select listing_id, longitude, latitude, city, neighbourhood from locality_tt

/* Nidhi Galgali */
insert into reviews (listing_id, scores_rating, scores_value)
select listing_id, review_scores_rating, review_scores_value from locality_tt

 /* Archana Narayanan */
insert into property_details (listing_id, property_type, room_type, accomodate_count, bedrooms, price, instant_bookable)
select listing_id, property_type, room_type,accommodates,bedrooms, price, instant_bookable from locality_tt

 /* Archana Narayanan */
insert into amenities (listing_id, amenities)
select listing_id, amenities from locality_tt