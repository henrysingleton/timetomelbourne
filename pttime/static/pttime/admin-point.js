$(window).on('map:init', function (e) {
    var detail = e.originalEvent ?
                 e.originalEvent.detail : e.detail;

    // Optional specific behaviour for particular field
    detail.map.on('map:loadfield', function (ev) {
        if (ev.fieldid == 'id_geolocation') {
            cords = [ev.field.store.load()._latlng.lng, ev.field.store.load()._latlng.lat];
            L.marker(cords).addTo(detail.map);

            detail.map.setView(cords, 13);
        }
    });
});