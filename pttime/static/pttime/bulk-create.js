window.markers = [];
window.markerExport = function() {
    console.log(JSON.stringify(window.markers));
}

var myIcon = L.divIcon({className: 'my-div-icon'}),

save_markers = function(e) {
    points = window.markers.map(format_point);

    var data = {
        data: points
    };

    $.ajax({
        url: '/pttime/bulk-list/',
        type: 'POST',
        contentType: "application/json",
        data: JSON.stringify(data)
    });
},

format_point = function(latlng) {
    return {
        "geolocation": {
            "coordinates": latlng,
            "type": "Point"
        }
    };
},

map_points = function(data) {
    data.map(function(point) {
        create_point(point.geolocation.coordinates);
    })
},

create_point = function(latlng, map) {
    marker = L.marker(latlng, {icon: myIcon});
    marker.on('click',function(e) {
        window.maps[0].removeLayer(e.target);
    });
    marker.addTo(window.maps[0]);

    return marker;
},

generate_point_array = function(e) {
    var latInc = ($('#lat_spacing').val() * 0.004), //0.016 Y
        lngInc = ($('#lng_spacing').val() * 0.005),  //0.02  X (to handle the fact that spacing is slightly different between lng and lat
        latLimit = $('#grid_width').val() * 1,
        lngLimit = $('#grid_height').val() * 1;

    var startingLat = e.latlng.lat,
        startingLng = e.latlng.lng;

    for (lat = startingLat; lat > startingLat - (latInc * latLimit); lat = lat - latInc) {
        for (lng = startingLng; lng < startingLng + (lngInc * lngLimit); lng = lng + lngInc) {
            create_point([lat, lng])
            window.markers.push([lat, lng]);
        }
    }

    return true;
},

// Restore points from the DB, normally happens on page load.
restore_points = function() {
    $.ajax({
        dataType: "json",
        url: '/pttime/points/list/',
        success: map_points
    });
},

onMapClick = function(e) {
    if ($('#tool').val() == 'add') {
        return generate_point_array(e);
    }
    return true;
};


function main_map_init (map, options) {

    // set default position
    map.setView([-37.81044510305556, 144.9629044532776], 13);

    // hydrate the  map
    restore_points();

    // Main map event
    map.on('click', onMapClick);

    // Save markers event
    document.getElementsByClassName('create-points')[0].addEventListener('click',save_markers);


}