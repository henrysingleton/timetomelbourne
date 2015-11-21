window.markers = [];
window.markerExport = function() {
    console.log(JSON.stringify(window.markers));
}

function main_map_init (map, options) {

    // set default position
    map.setView([-37.81044510305556, 144.9629044532776], 13);

    L.tileLayer('http://192.168.56.101/osm/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors, Running from PTTIME mirror'
    }).addTo(map);

    var onMapClick = function(e) {
        var latInc = (1 * 0.004), //0.016 Y
            lngInc = (1 * 0.005),  //0.02  X
            latLimit = 50,
            lngLimit = 50,
            myIcon = L.divIcon({className: 'my-div-icon'});

        var startingLat = e.latlng.lat,
            startingLng = e.latlng.lng;

        for (lat = startingLat; lat > startingLat - (latInc * latLimit); lat = lat - latInc) {

            for (lng = startingLng; lng < startingLng + (lngInc * lngLimit); lng = lng + lngInc) {


                var marker = L.marker([lat, lng], {icon: myIcon});

                //markers.push(marker.toGeoJSON());
                window.markers.push([lat, lng]);

                marker.on('click',function(e) {
                    map.removeLayer(e.target);
                });
                marker.addTo(map);
            }
        }

        // then do something like JSON.stringify(window.markers) to export your lovely data!


    };

    map.on('click', onMapClick);

}