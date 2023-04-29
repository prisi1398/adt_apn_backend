alter table listings add primary key (id)  /* Archana Narayanan */
alter table location add constraint FK_Listing FOREIGN KEY (listing_id) references listings(id); /* Preethi Sivakumar */
alter table reviews add constraint FK_Listing_reviews FOREIGN KEY (listing_id) references listings(id); /* Nidhi Galgali */
alter table property_details add constraint FK_Listing_property FOREIGN KEY (listing_id) references listings(id); /* Archana Narayanan */
alter table amenities add constraint FK_Listing_amenities FOREIGN KEY (listing_id) references listings(id); /* Archana Narayanan */