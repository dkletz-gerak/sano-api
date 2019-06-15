# SANO-API

### Backbone server of Gerak!

---

This server is created to serve the data (CRUD) which will be used for the view.
This server is also acts as search engine which will find best location for people to do activity in sports based on what they want to do.

---

This documentation will give some important URLs which is needed by client.

#### GET /search?lat=:lat&long=:long&preferences=:preferences

This API used to search best location based on the preferences. Preferences for this API is the list activities user wants to do. Response will give the location ordered by its weight which is calculated by location and preferences.

##### Example Response
```json5
{
  "data": [
    {
      "activities": [
        "JOGGING"
      ],
      "address": "Jl. Cikini Raya No.73, RT.8/RW.2, Cikini, Kec. Menteng, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10330",
      "calculated_weight": 107.01873773492926,
      "category": "JOGGING TRACK",
      "id": 2,
      "logo": "https://cdn.idntimes.com/content-images/post/20160725/dsc-0328-4ba81e64bff04ed12d3d0465f2d63274.JPG",
      "name": "Taman Ismail Marzuki",
      "normal_weight": 1,
      "price": 0
    },
    {
      "activities": [
        "WEIGHTLIFTING",
        "ZUMBA"
      ],
      "address": "Jl. Dago Asri No.8, Dago, Kecamatan Coblong, Kota Bandung, Jawa Barat 40135",
      "calculated_weight": 107.83504928376888,
      "category": "GYM",
      "id": 1,
      "logo": "https://www.cravendc.gov.uk/media/7104/view-from-free-weights.jpg",
      "name": "Urban Gym",
      "normal_weight": 1,
      "price": 0
    }
  ],
  "status": 200
}
```

#### POST /location/marathon

This route is used to save query from user which is bound to certain location (such as GYM, etc.). This url only need to be accessed after user clicks some location after search for it. This data will be used to tag the location with activities.

##### Request
```json5
{
	"preferences": "1",
	"location_id": 1,
	"lat": 0,
	"long": 0
}
```

##### Example Response
```json5
{
    "data": {
        "id": 2,
        "lat": 0,
        "location": 1,
        "long": 0,
        "preferences": "1"
    },
    "status": 201
}
```

#### GET /user/profile

This route is used to get profile data from user which includes membership of the user.

##### Header Request
```json5
{
  "Authorization": <String>
}
```

##### Example Response
```json5
{
    "data": {
        "created_at": "Sat, 15 Jun 2019 15:44:28 GMT",
        "email": "123@gmail.com",
        "id": 1,
        "membership": {
            "created_at": "Sat, 15 Jun 2019 21:22:04 GMT",
            "description": "Membership Super Keren!",
            "id": 1,
            "member_type": "silver",
            "name": "Membership Keren",
            "updated_at": "Sat, 15 Jun 2019 21:22:18 GMT",
            "user": 1
        },
        "name": "Gery Wahyu",
        "role": "user",
        "updated_at": "Sat, 15 Jun 2019 15:44:37 GMT"
    },
    "status": 200
}
```


#### Other CRUD

We also server read data for activity, category, event, routine, and schedule. But we won't put it here since it is just get data from URL.

Thank you!!