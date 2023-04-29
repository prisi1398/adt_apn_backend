from lookinnApp.models import Location, Listings, Reviews, Property_Details, Amenities
import csv
from pathlib import Path


def run():
    path = Path(__file__).parent/"../Listings_Cleaned_Iti1.csv"
    with path.open(errors='ignore') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Listings.objects.all().delete()
        Location.objects.all().delete()
        Reviews.objects.all().delete()
        Property_Details.objects.all().delete()
        Amenities.objects.all().delete()

        count = 0

        for row in reader:
            
            count = count + 1
            # if count < 105000:
            #     continue

            if count > 463:
                break

            print(row)

            listing, _ = Listings.objects.get_or_create(name=row[1])

            location = Location(longitude=row[8],
                        latitude=row[7],
                        city=row[6],
                        neighbourhood=row[5],
                        listing_id=listing)
            
            review = Reviews(score_rating= row[15],
                             score_value= row[16] ,
                             listing_id = listing)
            
            propertyDetail = Property_Details(property_type=row[9],
                        room_type=row[10],
                        accomodate_count=row[11],
                        bedrooms=row[12],
                        price= row[14],
                        instant_bookable= row[17],
                        listing_id= listing)
            
            amenity = Amenities(amenities= row[13] ,
                             listing_id = listing)
            

            propertyDetail.save()
            review.save()
            location.save()
            amenity.save()
